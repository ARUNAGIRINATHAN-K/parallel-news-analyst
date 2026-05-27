from langchain_groq import ChatGroq
from tools.tavily_search import search_news
from prompts.cyber_prompt import CYBER_PROMPT

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def cyber_agent(state):
    """
    Cybersecurity News Agent

    Responsibilities:
    - Search latest cybersecurity news
    - Monitor cyberattacks and data breaches
    - Track malware/ransomware campaigns
    - Analyze threat intelligence trends
    """

    query = state["query"]
    model="llama-3.3-70b-versatile",
    # Cybersecurity-focused search query
    cyber_query = f"""
    {query}
    cybersecurity
    cyber attack
    ransomware
    malware
    data breach
    zero day vulnerability
    threat intelligence
    phishing
    cloud security
    """

    # Search latest cybersecurity news
    search_results = search_news(cyber_query)

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

    # Generate cybersecurity analysis summary
    response = llm.invoke(
        CYBER_PROMPT.format(
            query=query,
            articles=combined_articles
        )
    )

    return {
        "cyber_results": [
            {
                "agent": "Cybersecurity Agent",
                "summary": response.content,
                "sources": [
                    r.get("url") for r in search_results
                ]
            }
        ]
    }