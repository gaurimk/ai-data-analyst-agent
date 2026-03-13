import sys
import os

# allow imports from parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd

from agents.data_agent import DataAgent
from agents.viz_agent import VisualizationAgent
from agents.insight_agent import InsightAgent
from agents.chat_agent import ChatAgent
from agents.chart_agent import ChartAgent


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Data Analyst Agent",
    layout="wide"
)

st.title("AI Data Analyst Agent")
st.write("Upload a dataset and let AI analyze it automatically.")


# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv"]
)


# ---------------------------------------------------
# DATASET LOADING
# ---------------------------------------------------

if uploaded_file:

    try:
        df = pd.read_csv(uploaded_file, encoding="latin1")
    except:
        df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)


    # ---------------------------------------------------
    # RUN AI ANALYSIS
    # ---------------------------------------------------

    if st.button("Run AI Analysis"):

        st.write("Running AI analysis...")

        data_agent = DataAgent(df)
        analysis = data_agent.run_analysis()

        viz_agent = VisualizationAgent()
        charts = viz_agent.run(df)

        insight_agent = InsightAgent()
        insights = insight_agent.generate_insights(analysis)

        st.subheader("AI Insights")
        st.write(insights)

        st.subheader("Generated Charts")

        for chart in charts:

            st.markdown(f"### {chart['title']}")

            st.image(chart["path"], width=500)

            st.markdown(
                f"""
**X-axis:** {chart['x']}  
**Y-axis:** {chart['y']}
"""
            )

            st.write(chart["explanation"])


    # ---------------------------------------------------
    # CHAT SECTION
    # ---------------------------------------------------

    st.subheader("Chat with your Dataset")

    chat_agent = ChatAgent()
    chart_agent = ChartAgent()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_question = st.text_input(
        "Ask a question about your dataset:"
    )


    if st.button("Ask AI"):

        if user_question:

            st.session_state.chat_history.append(("You", user_question))

            # ---------------------------------
            # STEP 1 → TEXT ANSWER FIRST
            # ---------------------------------

            response = chat_agent.answer_question(df, user_question)

            if isinstance(response, dict):
                content = response.get("content", "")
            else:
                content = response

            st.session_state.chat_history.append(("AI", content))


            # ---------------------------------
            # STEP 2 → Detect chart request
            # ---------------------------------

            question_lower = user_question.lower()

            chart_keywords = [
                "chart",
                "graph",
                "plot",
                "visualize",
                "distribution",
                "scatter",
                "bar chart",
                "line chart",
                "histogram"
            ]

            wants_chart = any(word in question_lower for word in chart_keywords)


            # ---------------------------------
            # STEP 3 → Generate chart
            # ---------------------------------

            if wants_chart:

                fig = chart_agent.generate_chart(df, user_question)

                if fig:
                    st.session_state.chat_history.append(("AI_CHART", fig))


    # ---------------------------------------------------
    # DISPLAY CHAT HISTORY
    # ---------------------------------------------------

    for role, message in st.session_state.chat_history:

        if role == "You":
            st.markdown(f"**You:** {message}")

        elif role == "AI":
            st.markdown(f"**AI:** {message}")

        elif role == "AI_CHART":
            st.pyplot(message, clear_figure=True)