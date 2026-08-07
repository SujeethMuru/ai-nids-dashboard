import streamlit as st
import pandas as pd

st.title("AI-Powered Network Intrusion Detection Dashboard")

st.write(
    "Welcome! This dashboard is being developed to analyze network traffic, "
    "visualize security data, and serve as the foundation for an AI-powered "
    "intrusion detection system."
)

st.header("Project Overview")

st.markdown(
    """
    - Analyze network traffic data
    - Identify patterns that may indicate suspicious behavior
    - Visualize important cybersecurity metrics
    - Build toward an AI-assisted intrusion detection workflow
    """
)

st.header("Network Traffic Data")

traffic_data = pd.read_csv("data/raw/sample_network_traffic.csv")

st.dataframe(traffic_data)