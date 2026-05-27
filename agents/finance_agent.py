from langchain_groq import ChatGroq
from tools.tavily_search import search_news
from prompts.finance_prompt import FINANCE_PROMPT

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def finance_agent(state):
    """
    Finance News Agent

    Responsibilities:
    - Search latest finance news
    - Analyze stock market trends
    - Summarize economic insights
    - Return structured finance briefing
    """

    query = state["query"]
    model="llama-3.3-70b-versatile",
    # Enhanced finance-focused search query
    finance_query = f"""
    {query}
    latest finance news
    stock market
    economy
    business trends
    investments
    """

    # Search news using Tavily
    search_results = search_news(finance_query)

    # Extract news content
    articles = []

    for result in search_results:
        articles.append(
            f"""
            Title: {result.get('title')}
            Content: {result.get('content')}
            URL: {result.get('url')}
            """
        )

    combined_articles = "\n\n".join(articles)

    # Generate finance summary
    response = llm.invoke(
        FINANCE_PROMPT.format(
            query=query,
            articles=combined_articles
        )
    )

    return {
        "finance_results": [
            {
                "agent": "Finance Agent",
                "summary": response.content,
                "sources": [
                    r.get("url") for r in search_results
                ]
            }
        ]
    }