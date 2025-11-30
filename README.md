#  TCS Financial Forecasting Agent  
A FastAPI + LangChain AI agent for financial PDF extraction, RAG-based transcript analysis, and structured forecasting.

---

## 1. Project Overview

This project implements an **AI-powered financial forecasting agent** for **Tata Consultancy Services (TCS)**.  
It performs multi-step reasoning by:

- Extracting metrics from **quarterly financial reports (PDF)**
- Running **RAG-based semantic search** on earnings call transcripts
- Analyzing management sentiment, risks, and opportunities
- Generating a **qualitative forward-looking business forecast**
- Returning output as **strict JSON**
- Logging all requests + forecasts into **MySQL**

The architecture combines FastAPI, LangChain, OpenAI LLMs, FAISS vector search, and SQL logging.

---

## 2. Architecture

```
POST /forecast
      │
      ▼
 ForecastAgent (Orchestrator)
      │
      ├── FinancialDataExtractorTool
      │       └── Extract metrics from PDFs
      │
      ├── TranscriptAnalysisTool (RAG)
      │       ├── Chunk transcripts
      │       ├── Embed text (OpenAI)
      │       ├── FAISS vectorstore
      │       └── Semantic retrieval + summary
      │
      └── (Optional) MarketDataTool
              └── Live stock price

Final JSON Forecast → Logged to MySQL
```

---

## 3. Agent & Tools

### 3.1 ForecastAgent
Central controller that:

- Calls tools for metrics + transcript insights
- Combines data using an LLM
- Forces JSON output
- Logs to MySQL

**JSON output schema:**

```json
{
  "financial_trends": {},
  "management_sentiment": {},
  "forecast": {},
  "risks": [],
  "opportunities": []
}
```

---

### 3.2 FinancialDataExtractorTool
Extracts:

- Revenue  
- Net Profit  
- Operating Margin  
- EPS  

Uses pdfplumber + regex + fuzzy matching.

---

### 3.3 TranscriptAnalysisTool (RAG)
RAG pipeline:

1. Load transcripts  
2. Chunk text  
3. Generate embeddings  
4. Build FAISS vectorstore  
5. Retrieve top semantic matches  
6. Summarize management sentiment + risks + opportunities  

---

## 4. Setup Instructions (Exact Steps)

### 4.1 Clone
```bash
git clone https://github.com/yourusername/tcs-forecast-agent.git
cd tcs-forecast-agent
```

---

### 4.2 Create venv
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 4.3 Install dependencies
```bash
pip install -r requirements.txt
```

---

### 4.4 Create `.env`
```
OPENAI_API_KEY=sk-xxxx
MYSQL_URL=mysql+pymysql://root:password@localhost:3306/tcs_agent

EMBEDDING_MODEL=text-embedding-3-small
LLM_MODEL=gpt-4o-mini

DATA_REPORT_DIR=data/reports
DATA_TRANSCRIPT_DIR=data/transcripts
```

---

### 4.5 Add data
Place PDFs:

```
data/reports/*.pdf
data/transcripts/*.pdf
```

---

### 4.6 Create MySQL DB
```bash
mysql -u root -p
```

```sql
CREATE DATABASE tcs_agent;
```

---

### 4.7 Run server
```bash
uvicorn app.main:app --reload
```

Open docs:

 http://127.0.0.1:8000/docs

---

## 5. How to Run Forecast

POST → `/forecast`

Example payload:

```json
{
  "quarters": 2
}
```

---

## 6. Example Output

```json
{
  "financial_trends": {
    "revenue": "Improving QoQ...",
    "margin": "Slight expansion...",
    "profitability": "Stable..."
  },
  "management_sentiment": {
    "tone": "Cautiously optimistic",
    "themes": ["Deal pipeline stabilizing", "GenAI interest rising"]
  },
  "forecast": {
    "revenue_growth_next_quarter": "1.8% - 2.4%",
    "margin_outlook": "Flat to slight expansion"
  },
  "risks": ["Currency volatility", "Macro slowdown"],
  "opportunities": ["GenAI adoption", "Large BFSI deals"]
}
```

---

## 7. Requirements

Includes:

- FastAPI  
- LangChain  
- LangChain OpenAI  
- pdfplumber  
- FAISS  
- SQLAlchemy  
- PyMySQL  

---

## 8. Summary

This Agent demonstrates:

- Multi-step agentic reasoning  
- PDF financial metric extraction  
- Transcript RAG pipeline  
- Structured forecasting with LLM  
- Full MySQL logging  
- Reproducible setup with a clean architecture  


