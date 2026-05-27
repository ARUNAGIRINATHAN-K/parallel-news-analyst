import os
from tavily import TavilyClient
from dotenv import load_dotenv

# =========================================================
# LOAD ENV VARIABLES
# =========================================================

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError(
        "TAVILY_API_KEY not found in environment variables."
    )

# =========================================================
# INITIALIZE TAVILY CLIENT
# =========================================================

client = TavilyClient(
    api_key=TAVILY_API_KEY
)


# =========================================================
# SEARCH FUNCTION
# =========================================================

def search_news(
    query: str,
    max_results: int = 5
):
    """
    Search real-time news using Tavily.

    Args:
        query (str):
            Search query

        max_results (int):
            Number of search results

    Returns:
        list:
            List of news articles
    """

    try:

        response = client.search(
            query=query,
            topic="news",
            search_depth="advanced",
            max_results=max_results,
            include_answer=True,
            include_raw_content=False
        )

        return response.get("results", [])

    except Exception as e:

        print(f"[TAVILY ERROR]: {e}")

        return []


# =========================================================
# OPTIONAL HELPER FUNCTION
# =========================================================

def format_search_results(results):
    """
    Convert Tavily results into readable text
    for LLM summarization.
    """

    formatted = []

    for idx, result in enumerate(results, start=1):

        formatted.append(
            f"""
            Article {idx}

            Title:
            {result.get('title', 'N/A')}

            Content:
            {result.get('content', 'N/A')}

            URL:
            {result.get('url', 'N/A')}
            """
        )

    return "\n\n".join(formatted)


# =========================================================
# TEST RUN
# =========================================================

if __name__ == "__main__":

    news = search_news(
        "Latest AI and cybersecurity news"
    )

    print("\n" + "=" * 60)
    print("TAVILY SEARCH RESULTS")
    print("=" * 60)

    for article in news:

        print(f"\nTITLE: {article.get('title')}")
        print(f"URL: {article.get('url')}")
        print(f"CONTENT: {article.get('content')[:200]}...")