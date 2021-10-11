import streamlit as st
from tools.AccuracyAnalyzers import AdderAccuracyAnalyzer, MultiplierAccuracyAnalyzer

type_of_accuracy_analysis = [
    "Adder Accuracy Analysis",
    "Multiplier Accuracy Analysis",
]

type_of_hardware_modules = {
    "Adder Accuracy Analysis": ["HEAA", "HOERAA", "HOAANED", "M_HERLOA"],
    "Multiplier Accuracy Analysis": ["MxN AAM01 with V-cut"],
}


def show():
    st.title("Accuracy Analysis")

    st.subheader("1. Select type of accuracy analysis")
    selected_type_of_accuracy_analysis = st.radio(
        "Type of accuracy analysis",
        type_of_accuracy_analysis,
    )

    st.subheader("2. Select type of hardware module")
    selected_type_of_hardware_module = st.radio(
        "Type of hardware modules",
        type_of_hardware_modules[selected_type_of_accuracy_analysis],
    )

    st.subheader("3. Select number of bits")
    col1, col2 = st.columns(2)

    with col1:
        if not selected_type_of_accuracy_analysis == "Multiplier Accuracy Analysis":
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
        if not selected_type_of_accuracy_analysis == "Multiplier Accuracy Analysis":
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

    if selected_type_of_hardware_module == "MxN AAM01 with V-cut":
        v_cut = st.slider(
            "V Cut",
            min_value=0,
            max_value=multiplicand_bits,
            value=3,
        )

    st.subheader("4. Select first and second numbers")
    col1, col2 = st.columns(2)

    if not selected_type_of_accuracy_analysis == "Multiplier Accuracy Analysis":
        with col1:  # Adder Accuracy Analysis
            first_number_to_add = st.number_input(
                f"First number to be added (unsigned) 0 to {2**(total_bits-1)}",
                min_value=0,
                max_value=2 ** (total_bits - 1),
                value=4,
            )
        with col2:
            second_number_to_add = st.number_input(
                f"Second number to be added (unsigned) 0 to {2**(total_bits-1)}",
                min_value=0,
                max_value=2 ** (total_bits - 1),
                value=4,
            )
    else:  # Multiplier Accuracy Analysis
        with col1:
            first_number_to_multiply = st.number_input(
                f"First number to be multiplied (unsigned) 0 to {2**(multiplicand_bits)-1}",
                min_value=0,
                max_value=2 ** (multiplicand_bits) - 1,
                value=12,
            )
        with col2:
            second_number_to_multiply = st.number_input(
                f"Second number to be multiplied (unsigned) 0 to {2**(multiplicand_bits)-1}",
                min_value=0,
                max_value=2 ** (multiplicand_bits) - 1,
                value=12,
            )

    st.subheader("5. Review and analyse")
    chosen_options = {
        "type_of_accuracy_analysis": selected_type_of_accuracy_analysis,
        "type_of_hardware_module": selected_type_of_hardware_module,
        "total_bits": total_bits
        if not selected_type_of_accuracy_analysis == "Multiplier Accuracy Analysis"
        else 0,
        "accurate_bits": total_bits - inacc_bits
        if not selected_type_of_hardware_module == "Accurate Adder"
        and not selected_type_of_accuracy_analysis == "Multiplier Accuracy Analysis"
        else 0,
        "inaccurate_bits": inacc_bits
        if not selected_type_of_hardware_module == "Accurate Adder"
        and not selected_type_of_accuracy_analysis == "Multiplier Accuracy Analysis"
        else 0,
        "multiplicand_bits": multiplicand_bits
        if selected_type_of_accuracy_analysis == "Multiplier Accuracy Analysis"
        else 0,
        "multiplier_bits": multiplier_bits
        if selected_type_of_accuracy_analysis == "Multiplier Accuracy Analysis"
        else 0,
        "v_cut": v_cut
        if selected_type_of_hardware_module == "MxN AAM01 with V-cut"
        else 0,
        "adder_first_unsigned_number": first_number_to_add
        if selected_type_of_accuracy_analysis == "Adder Accuracy Analysis"
        else 0,
        "adder_second_unsigned_number": second_number_to_add
        if selected_type_of_accuracy_analysis == "Adder Accuracy Analysis"
        else 0,
        "multiplier_first_unsigned_number": first_number_to_multiply
        if selected_type_of_accuracy_analysis == "Multiplier Accuracy Analysis"
        else 0,
        "multiplier_second_unsigned_number": second_number_to_multiply
        if selected_type_of_accuracy_analysis == "Multiplier Accuracy Analysis"
        else 0,
    }
    st.write(chosen_options)

    if st.button("Click to analyze"):
        st.subheader("6. Result of analysis")
        with st.spinner("Analyzing... It may take up to 2-3 mins"):
            if selected_type_of_accuracy_analysis == "Adder Accuracy Analysis":
                (
                    accurate_adder_sum,
                    inaccurate_adder_sum,
                    inaccurate_adder_accuracy,
                ) = AdderAccuracyAnalyzer.analyze(
                    {
                        "total_bits": total_bits,
                        "inacc_bits": inacc_bits,
                        "adder_first_unsigned_number": first_number_to_add,
                        "adder_second_unsigned_number": second_number_to_add,
                        "type_of_accuracy_analysis_hardware": selected_type_of_hardware_module,
                    }
                )

                result = {
                    "Accurate Value": accurate_adder_sum,
                    "Approximated Value": inaccurate_adder_sum,
                    "Accuracy": f"{inaccurate_adder_accuracy}%",
                }
            else:  # Multiplier Error Analysis
                (
                    accurate_multiplier_product,
                    inaccurate_multiplier_product,
                    inaccurate_multiplier_accuracy,
                ) = MultiplierAccuracyAnalyzer.analyze(
                    {
                        "multiplicand_bits": multiplicand_bits,
                        "multiplier_bits": multiplier_bits,
                        "multiplier_first_unsigned_number": first_number_to_multiply,
                        "multiplier_second_unsigned_number": second_number_to_multiply,
                        "v_cut": v_cut,
                    }
                )

                result = {
                    "Accurate Value": accurate_multiplier_product,
                    "Approximated Value": inaccurate_multiplier_product,
                    "Accuracy": f"{inaccurate_multiplier_accuracy}%",
                }

            st.write(result)
