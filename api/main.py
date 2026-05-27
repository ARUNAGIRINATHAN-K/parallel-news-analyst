from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Import workflow runner
from graph.workflow import run_news_analysis

# =========================================================
# INITIALIZE FASTAPI
# =========================================================

app = FastAPI(
    title="Parallel Multi-Agent News Analyst",
    description="""
    Real-time Multi-Agent AI News Analysis System
    powered by LangGraph, Groq, and Tavily.
    """,
    version="1.0.0"
)

# =========================================================
# REQUEST MODEL
# =========================================================

class NewsRequest(BaseModel):
    query: str


# =========================================================
# ROOT ENDPOINT
# =========================================================

@app.get("/")
def home():

    return {
        "message": "Parallel Multi-Agent News Analyst API",
        "status": "running",
        "framework": "LangGraph",
        "llm": "Groq",
    }


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


# =========================================================
# NEWS ANALYSIS ENDPOINT
# =========================================================

@app.post("/analyze")
def analyze_news(request: NewsRequest):

    try:

        result = run_news_analysis(
            query=request.query
        )

        return {
            "success": True,
            "query": request.query,
            "final_report": result.get("final_report"),
            "finance_results": result.get("finance_results"),
            "ai_results": result.get("ai_results"),
            "cyber_results": result.get("cyber_results"),
            "startup_results": result.get("startup_results"),
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# =========================================================
# RUN SERVER
# =========================================================

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )