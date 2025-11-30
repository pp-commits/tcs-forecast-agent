import json
from langchain_openai import ChatOpenAI
from app.agent.tools import FinancialDataExtractorTool, TranscriptAnalysisTool
from app.config import settings

class ForecastAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model=settings.LLM_MODEL, temperature=0.2)

        self.fin_tool = FinancialDataExtractorTool()
        self.qual_tool = TranscriptAnalysisTool()

    def generate_forecast(self):
        financials = self.fin_tool.extract()
        qualitative = self.qual_tool.analyze()

        prompt = f"""
You are a financial forecasting expert.

Using the data below:

FINANCIAL METRICS:
{json.dumps(financials, indent=2)}

QUALITATIVE INSIGHTS:
{qualitative}

Provide a structured business outlook for TCS. Include:

- financial_trends
- management_sentiment
- forecast
- risks
- opportunities

Return ONLY valid JSON.
"""

        response = self.llm.invoke(prompt)
        return json.loads(response.content)
