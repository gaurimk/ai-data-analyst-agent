from langgraph.graph import StateGraph, END
from typing import TypedDict

from agents.data_agent import DataAgent
from agents.viz_agent import VisualizationAgent
from agents.insight_agent import InsightAgent


class AgentState(TypedDict):
    df: object
    analysis: dict
    insights: str


# ---------- Nodes ----------

def data_node(state: AgentState):

    df = state["df"]

    agent = DataAgent(df)

    analysis = agent.run_analysis()

    return {"analysis": analysis}


def visualization_node(state: AgentState):

    df = state["df"]

    agent = VisualizationAgent(df)

    chart_path = agent.create_bar_chart("product")

    return {"df": df}


def insight_node(state: AgentState):

    analysis = state["analysis"]

    agent = InsightAgent()

    insights = agent.generate_insights(analysis)

    return {"insights": insights}


# ---------- Build Graph ----------

def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("data_analysis", data_node)

    graph.add_node("visualization", visualization_node)

    graph.add_node("insight_generation", insight_node)

    graph.set_entry_point("data_analysis")

    graph.add_edge("data_analysis", "visualization")

    graph.add_edge("visualization", "insight_generation")

    graph.add_edge("insight_generation", END)

    return graph.compile()