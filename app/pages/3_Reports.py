import streamlit as st
from pathlib import Path

st.title("Reports")

reports_dir = Path("reports")

if not reports_dir.exists():
    st.warning("No reports found")
    st.stop()

files = sorted(reports_dir.glob("report_*.txt"))

if not files:
    st.warning("No reports generated yet")
    st.stop()

selected = st.selectbox("Select a report",files,format_func=lambda x: x.name)

st.text(selected.read_text())
