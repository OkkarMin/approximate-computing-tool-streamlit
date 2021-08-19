import streamlit as st
from tools.ErrorAnalyzers import AdderErrorAnalyzer, MultiplierErrorAnalyzer

type_of_error_analysis = [
    "Adder Error Analysis",
    "Multiplier Error Analysis",
]


type_of_hardware_modules = {
    "Adder Error Analysis": ["HEAA", "HOERAA", "HOAANED", "M-HERLOA"],
    "Multiplier Error Analysis": ["MxN PAAM01 with V-cut"],
}


def show():
    st.title("Error Analysis")

    st.subheader("1. Select type of error analysis")
    selected_type_of_error_analysis = st.radio(
        "Type of error analysis",
        type_of_error_analysis,
    )

    st.subheader("2. Select type of hardware module")
    selected_type_of_hardware_module = st.radio(
        "Type of hardware modules",
        type_of_hardware_modules[selected_type_of_error_analysis],
    )

    st.subheader("3. Select number of bits")
    col1, col2 = st.columns(2)

    with col1:
        if not selected_type_of_error_analysis == "Multiplier Error Analysis":
            total_bits = st.slider(
                "Total bits",
                min_value=4,
                max_value=32,
                value=4,
            )
        else:
            multiplicand_bits = st.slider(
                "Multiplicand bits",
                min_value=4,
                max_value=32,
                value=4,
            )

    with col2:
        if not selected_type_of_error_analysis == "Multiplier Error Analysis":
            if total_bits == 4:
                inacc_bits = 3
            else:
                inacc_bits = st.slider(
                    "Inaccurate bits",
                    min_value=3,
                    max_value=total_bits - 1,
                )
        else:
            multiplier_bits = st.slider(
                "Multiplier bits",
                min_value=4,
                max_value=32,
                value=4,
            )

    if selected_type_of_hardware_module == "MxN PAAM01 with V-cut":
        v_cut = st.slider(
            "V Cut",
            min_value=0,
            max_value=multiplicand_bits,
            value=3,
        )

    st.subheader("4. Review and analyse")
    chosen_options = {
        "type_of_error_analysis": selected_type_of_error_analysis,
        "type_of_hardware_module": selected_type_of_hardware_module,
        "total_bits": total_bits
        if not selected_type_of_error_analysis == "Multiplier Error Analysis"
        else 0,
        "accurate_bits": total_bits - inacc_bits
        if not selected_type_of_hardware_module == "Accurate Adder"
        and not selected_type_of_error_analysis == "Multiplier Error Analysis"
        else 0,
        "inaccurate_bits": inacc_bits
        if not selected_type_of_hardware_module == "Accurate Adder"
        and not selected_type_of_error_analysis == "Multiplier Error Analysis"
        else 0,
        "multiplicand_bits": multiplicand_bits
        if selected_type_of_error_analysis == "Multiplier Error Analysis"
        else 0,
        "multiplier_bits": multiplier_bits
        if selected_type_of_error_analysis == "Multiplier Error Analysis"
        else 0,
        "v_cut": v_cut
        if selected_type_of_hardware_module == "MxN PAAM01 with V-cut"
        else 0,
    }
    st.write(chosen_options)

    if st.button("Click to analyze"):

        st.subheader("5. Result of analysis")
        with st.spinner("Analyzing..."):
            if selected_type_of_error_analysis == "Adder Error Analysis":
                average_error, mean_absolute_error, root_mean_square_error = getattr(
                    AdderErrorAnalyzer, selected_type_of_hardware_module
                )(total_bits, inacc_bits)
            else:  # Multiplier Error Analysis
                (
                    average_error,
                    mean_absolute_error,
                    root_mean_square_error,
                ) = MultiplierErrorAnalyzer.PAAM01_VCut(
                    multiplicand_bits, multiplier_bits, v_cut
                )

            result = {
                "Average Error": average_error,
                "Mean Absolute Error": mean_absolute_error,
                "Root Mean Square Error": root_mean_square_error,
            }
            st.write(result)
