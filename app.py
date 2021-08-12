import streamlit as st
from pages import verilog_code_generator, error_analysis, accuracy_analysis

tool_pages = {
    "Verilog Code Generator": verilog_code_generator,
    "Error Analysis": error_analysis,
    "Accuracy Analysis": accuracy_analysis,
}

st.sidebar.title("Approximate Computing Tool")

tool_choice = st.sidebar.selectbox(
    "Select tool",
    tool_pages.keys(),
)

tool_pages[tool_choice].show()
