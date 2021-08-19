import streamlit as st
from pages import verilog_code_generator, error_analysis, accuracy_analysis

tool_pages = {
    "Verilog Code Generator": verilog_code_generator,
    "Error Analysis": error_analysis,
    "Accuracy Analysis": accuracy_analysis,
}

st.set_page_config(
    page_title="Approximate Computing Tool",
    page_icon="https://www.ntu.edu.sg/ResourcePackages/NTU/assets/images/favicon.png",
)

st.sidebar.title("Approximate Computing Tool")

selected_tool_choice = st.sidebar.selectbox(
    "Select tool",
    tool_pages.keys(),
)

st.sidebar.text("Read Documentation Here:")
documentation_link = (
    "[https://tool-documentation.vercel.app](https://tool-documentation.vercel.app)"
)
st.sidebar.markdown(documentation_link, unsafe_allow_html=True)

# displays selected tool page
tool_pages[selected_tool_choice].show()
