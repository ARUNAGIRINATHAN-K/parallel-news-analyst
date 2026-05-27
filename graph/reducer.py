from graph.state import NewsState


def _latest_summary(items):
    if not items:
        return "No results available."

    summary = items[-1].get("summary")
    return summary or "No summary available."


def reducer(state: NewsState):
    """
    Merge the parallel agent outputs into a single final report.
    """

    finance_summary = _latest_summary(state.get("finance_results", []))
    ai_summary = _latest_summary(state.get("ai_results", []))
    cyber_summary = _latest_summary(state.get("cyber_results", []))
    startup_summary = _latest_summary(state.get("startup_results", []))

    final_report = f"""## Final Intelligence Briefing

### Finance
{finance_summary}

### AI
{ai_summary}

### Cybersecurity
{cyber_summary}

### Startups
{startup_summary}
"""

    return {
        "final_report": final_report.strip()
    }