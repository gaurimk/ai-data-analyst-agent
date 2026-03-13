AI Data Analyst Agent

An AI-powered data analysis platform that allows users to upload datasets, automatically generate insights, visualize relationships, and interact with the data through a conversational AI interface.

This project combines Large Language Models (LLMs), AI agents, automated exploratory data analysis (EDA), and vector search to build an intelligent system capable of performing analytics tasks similar to modern business intelligence tools.

Features

Upload datasets and automatically analyze them
Generate automated charts and visualizations
Detect correlations between variables
Produce AI-generated insights from datasets
Conversational chatbot for dataset queries
Generate charts directly from natural language queries
Export processed datasets for Tableau dashboards
Modular multi-agent architecture
Retrieval Augmented Generation (RAG) support

Technologies Used
Python
Streamlit
LangChain
LangGraph
ChromaDB (Vector Database)
Ollama (Local LLM)
Pandas
Matplotlib
Seaborn

Project Architecture
User
 ↓
Streamlit Interface
 ↓
LangGraph Orchestrator
 ↓
AI Agents
   ├── Data Agent
   ├── Visualization Agent
   ├── Insight Agent
   └── Chat Agent
 ↓
MCP Tool Layer
 ↓
Analytics Tools
   ├── Data Analysis Tool
   ├── Visualization Tool
   ├── RAG Search Tool
   └── Tableau Export Tool
 ↓
Vector Database (ChromaDB)
 ↓
LLM (Ollama)

Project Structure
ai-data-analyst-agent
│
├── agents
│   ├── chart_agent.py
│   ├── chat_agent.py
│   ├── data_agent.py
│   ├── insight_agent.py
│   ├── orchestrator_agent.py
│   ├── rag_agent.py
│   └── viz_agent.py
│
├── tools
│   ├── data_analysis_tool.py
│   ├── visualization_tool.py
│   ├── rag_search_tool.py
│   └── tableau_export_tool.py
│
├── rag
│   ├── document_loader.py
│   ├── embeddings.py
│   └── vector_store.py
│
├── models
│   └── ollama_client.py
│
├── graph
│   └── agent_graph.py
│
├── mcp
│   └── mcp_server.py
│
├── app
│   └── streamlit_app.py
│
├── assets
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│   ├── 6.png
│   └── 7.png
│
├── config
│   └── settings.py
│
├── data
│   └── docs
│
├── requirements.txt
└── README.md

How It Works
1 Upload Dataset
Users upload a CSV dataset through the Streamlit interface.

2 Automated Analysis
The DataAgent performs exploratory data analysis including:
dataset summary
statistical metrics
column structure analysis

3 Visualization Generation
The VisualizationAgent automatically detects data types and generates charts such as:
Histograms
Scatter plots
Category distributions
Correlation heatmaps

4 Insight Generation
The InsightAgent uses a Large Language Model to generate meaningful insights from the dataset.

5 Conversational Data Analysis
Users can interact with the dataset using natural language.

Example Workflow

1 Upload a dataset
2 Click Run AI Analysis
3 Review generated charts and insights
4 Ask questions about the dataset through the chatbot

Example Workflow

1 Upload a dataset
2 Click Run AI Analysis
3 Review generated charts and insights
4 Ask questions about the dataset through the chatbot

## Project Demo

### Application Interface
![Application Dashboard](assets/1.png)

### Dataset Preview
![Dataset Preview](assets/2.png)

### AI Generated Insights
![Insights](assets/3.png)

### Generated Charts
![Charts](assets/4.png)

### Visualization Output
![Visualization](assets/5.png)

### Chat Interface
![Chatbot](assets/6.png)

### Correlation Heatmap
![Heatmap](assets/7.png)

