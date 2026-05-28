import streamlit as st
import requests
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Parallel Multi-Agent News Analyst",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.block-container {
    padding-top: 2rem;
}

.agent-card {
    padding: 1rem;
    border-radius: 12px;
    border: 1px solid #333;
    margin-bottom: 1rem;
}

.report-box {
    padding: 1.5rem;
    border-radius: 12px;
    background-color: #111;
    border: 1px solid #444;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.title("🧠 Parallel Multi-Agent News Analyst")

st.markdown("""
Real-time AI-powered news intelligence system built with:

- LangGraph Send API
- Groq LLM
- Tavily Search
- FastAPI
- Streamlit
""")

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("⚙️ Settings")

    api_url = st.text_input(
        "FastAPI URL",
        value="http://localhost:8000/analyze"
    )

    st.markdown("---")

    st.markdown("""
    ### 🤖 Active Agents

    - Finance Agent
    - AI Agent
    - Cybersecurity Agent
    - Startup Agent
    """)

    st.markdown("---")

    st.caption(
        f"Updated: {datetime.now().strftime('%d %b %Y %H:%M:%S')}"
    )

# =========================================================
# QUERY INPUT
# =========================================================

query = st.text_area(
    "🔍 Enter News Analysis Query",
    placeholder="""
Example:
- Latest AI and startup ecosystem news
- Global cybersecurity threats this week
- AI impact on financial markets
""",
    height=120
)

# =========================================================
# ANALYZE BUTTON
# =========================================================

analyze_button = st.button(
    "🚀 Run Parallel Analysis",
    use_container_width=True
)

# =========================================================
# RUN ANALYSIS
# =========================================================

if analyze_button:

    if not query.strip():

        st.warning("Please enter a query.")

    else:

        with st.spinner(
            "Running parallel multi-agent analysis..."
        ):

            try:

                response = requests.post(
                    api_url,
                    json={"query": query},
                    timeout=120
                )

                data = response.json()

                if data.get("success"):

                    st.success(
                        "Parallel analysis completed successfully!"
                    )

                    # =================================================
                    # FINAL REPORT
                    # =================================================

                    st.markdown("## 📋 Final Intelligence Report")

                    st.markdown(data.get("final_report") or "No final report available.")

                    st.markdown("---")

                    # =================================================
                    # AGENT OUTPUTS
                    # =================================================

                    col1, col2 = st.columns(2)

                    # =============================================
                    # FINANCE AGENT
                    # =============================================

                    with col1:

                        st.markdown("## 💰 Finance Agent")

                        for item in data.get("finance_results", []):

                            st.markdown(item.get("summary") or "No finance summary available.")

                            # Sources (if any)
                            sources = item.get("sources") or []
                            if sources:
                                st.markdown("**Sources:**")
                                for s in sources:
                                    st.markdown(f"- [{s}]({s})")

                    # =============================================
                    # AI AGENT
                    # =============================================

                    with col2:

                        st.markdown("## 🤖 AI Agent")

                        for item in data.get("ai_results", []):

                            st.markdown(item.get("summary") or "No AI summary available.")

                            sources = item.get("sources") or []
                            if sources:
                                st.markdown("**Sources:**")
                                for s in sources:
                                    st.markdown(f"- [{s}]({s})")

                    # =============================================
                    # CYBER AGENT
                    # =============================================

                    col3, col4 = st.columns(2)

                    with col3:

                        st.markdown("## 🛡️ Cybersecurity Agent")

                        for item in data.get("cyber_results", []):

                            st.markdown(item.get("summary") or "No cybersecurity summary available.")

                            sources = item.get("sources") or []
                            if sources:
                                st.markdown("**Sources:**")
                                for s in sources:
                                    st.markdown(f"- [{s}]({s})")

                    # =============================================
                    # STARTUP AGENT
                    # =============================================

                    with col4:

                        st.markdown("## 🚀 Startup Agent")

                        for item in data.get("startup_results", []):

                            st.markdown(item.get("summary") or "No startup summary available.")

                            sources = item.get("sources") or []
                            if sources:
                                st.markdown("**Sources:**")
                                for s in sources:
                                    st.markdown(f"- [{s}]({s})")

                    # =================================================
                    # RAW JSON OUTPUT
                    # =================================================

                    with st.expander(
                        "📦 View Raw API Response"
                    ):

                        st.json(data)

                else:

                    st.error(
                        f"API Error: {data.get('error')}"
                    )

            except Exception as e:

                st.error(
                    f"Connection Error: {str(e)}"
                )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Built with ❤️ using LangGraph, Groq, Tavily, FastAPI, and Streamlit
""")