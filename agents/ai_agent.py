from langchain_groq import ChatGroq
from tools.tavily_search import search_news
from prompts.ai_prompt import AI_PROMPT

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def ai_agent(state):
    """
    AI News Agent

    Responsibilities:
    - Search latest AI/LLM news
    - Track foundation model updates
    - Monitor AI startups and releases
    - Summarize AI industry trends
    """

    query = state["query"]
    model="llama-3.3-70b-versatile",
    # AI-focused search query
    ai_query = f"""
    {query}
    artificial intelligence
    generative AI
    LLM
    machine learning
    OpenAI
    Anthropic
    Google DeepMind
    AI startups
    """

    # Search latest AI news
    search_results = search_news(ai_query)

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

    # Generate AI analysis summary
    response = llm.invoke(
        AI_PROMPT.format(
            query=query,
            articles=combined_articles
        )
    )

    return {
        "ai_results": [
            {
                "agent": "AI Agent",
                "summary": response.content,
                "sources": [
                    r.get("url") for r in search_results
                ]
            }
        ]
    }