import os
import pdfplumber 
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_openai import OpenAIEmbeddings, ChatOpenAI  
from langchain_community.vectorstores import FAISS

from app.config import settings

class RAGPipeline:
    def __init__(self):
        self.vectorstore = None
        self.embeddings = OpenAIEmbeddings(model=settings.EMBEDDING_MODEL)
        self.llm = ChatOpenAI(model=settings.LLM_MODEL, temperature=0.2)

        self._build_vectorstore()

    def _build_vectorstore(self):
        folder = settings.DATA_TRANSCRIPT_DIR
        documents = []

        for file in os.listdir(folder):
            if not file.lower().endswith(".pdf"):
                continue
            
            text = ""
            with pdfplumber.open(os.path.join(folder, file)) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""

            documents.append(text)

        splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
        chunks = splitter.create_documents(documents)

        self.vectorstore = FAISS.from_documents(chunks, self.embeddings)

    def query(self, question):
        docs = self.vectorstore.similarity_search(question, k=5)
        context = "\n".join([d.page_content for d in docs])

        prompt = f"""
You are an expert financial analyst.
Using ONLY the context below, extract management commentary, sentiment, themes, risks & opportunities.

CONTEXT:
{context}

Return a structured JSON.
"""

        response = self.llm.invoke(prompt)
        return response.content
