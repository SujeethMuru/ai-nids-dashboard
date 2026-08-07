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

total_records = len(traffic_data)

suspicious_records = len(
    traffic_data[traffic_data["status"] == "Suspicious"]
)

normal_records = len(
    traffic_data[traffic_data["status"] == "Normal"]
)

total_bytes = traffic_data["bytes_transferred"].sum()
total_kb = total_bytes / 1024

st.subheader("Traffic Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", total_records)
col2.metric("Suspicious Records", suspicious_records)
col3.metric("Normal Records", normal_records)
col4.metric("Total Bytes Transferred", f"{total_kb:.1f} KB")

st.dataframe(traffic_data)