from langchain_groq import ChatGroq
from tools.tavily_search import search_news
from prompts.startup_prompt import STARTUP_PROMPT

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def startup_agent(state):
    """
    Startup & Venture Capital News Agent

    Responsibilities:
    - Search startup ecosystem news
    - Track funding rounds and acquisitions
    - Monitor emerging tech startups
    - Analyze venture capital trends
    """

    query = state["query"]
    model="llama-3.3-70b-versatile",
    # Startup-focused search query
    startup_query = f"""
    {query}
    startups
    venture capital
    funding rounds
    acquisitions
    unicorn startups
    SaaS
    AI startups
    tech founders
    startup ecosystem
    """

    # Search latest startup news
    search_results = search_news(startup_query)

    # Extract article information
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

    # Generate startup ecosystem summary
    response = llm.invoke(
        STARTUP_PROMPT.format(
            query=query,
            articles=combined_articles
        )
    )

    return {
        "startup_results": [
            {
                "agent": "Startup Agent",
                "summary": response.content,
                "sources": [
                    r.get("url") for r in search_results
                ]
            }
        ]
    }