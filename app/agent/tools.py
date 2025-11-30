import os
import re
import pdfplumber  
from rapidfuzz import fuzz, process  
from langchain_openai import OpenAIEmbeddings  
from app.config import settings
from app.agent.rag_pipeline import RAGPipeline

class FinancialDataExtractorTool:
    def extract(self):
        folder = settings.DATA_REPORT_DIR
        results = []

        for file in os.listdir(folder):
            if not file.lower().endswith(".pdf"):
                continue

            data = self._extract_from_pdf(os.path.join(folder, file))
            results.append({
                "file": file,
                "metrics": data
            })

        return results

    def _extract_from_pdf(self, path):
        text = ""
        try:
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
        except:
            return {}

        return {
            "revenue": self._search_metric(text, ["Revenue", "Total Income"]),
            "net_profit": self._search_metric(text, ["Net Profit", "Profit After Tax"]),
            "operating_margin": self._search_metric(text, ["Operating Margin", "EBIT Margin", "OPM"]),
        }

    def _search_metric(self, text, keys):
        lines = text.split("\n")

        best_match = process.extractOne(
            query=keys[0],
            choices=lines,
            scorer=fuzz.partial_ratio
        )

        if best_match and best_match[1] > 70:
            return best_match[0]

        return "Not found"


class TranscriptAnalysisTool:
    def __init__(self):
        self.rag = RAGPipeline()

    def analyze(self, query="Identify sentiment and management commentary"):
        return self.rag.query(query)
