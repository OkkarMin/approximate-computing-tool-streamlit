import streamlit as st

type_of_verilog_code = [
    "ASIC Verilog Adder",
    "FPGA Verilog Adder",
    "ASIC Verilog Multiplier",
]

type_of_hardware_modules = {
    "ASIC Verilog Adder": ["HEAA", "HOERAA", "HOAANED", "M-HERLOA"],
    "FPGA Verilog Adder": ["Accurate Adder", "HEAA", "HOERAA", "HOAANED", "M-HERLOA"],
    "ASIC Verilog Multiplier": [
        "MxN Accurate Multiplier",
        "MxN Accurate Binary Array Multiplier",
        "MxN PAAM01 with V-cut",
    ],
}


def show():
    st.title("Verilog Code Generator")

    st.subheader("1. Select type of verilog code to generate")
    selected_type_of_code = st.radio(
        "Type of verilog code",
        type_of_verilog_code,
    )

    st.subheader("2. Select type of hardware module")
    selected_type_of_hardware_module = st.radio(
        "Type of hardware modules", type_of_hardware_modules[selected_type_of_code]
    )

    st.subheader("3. Select number of Total bits and Inaccurate bits")
    col1, col2 = st.columns(2)

    with col1:
        total_bits = st.slider(
            "Total bits",
            min_value=4,
            max_value=32,
            value=4,
        )

    with col2:
        if not selected_type_of_hardware_module == "Accurate Adder":
            if total_bits == 4:
                inacc_bits = 3
            else:
                inacc_bits = st.slider(
                    "Inaccurate bits",
                    min_value=3,
                    max_value=total_bits - 1,
                )

    st.subheader("4. Review and generate")
    chosen_options = {
        "type_of_verilog_code": selected_type_of_code,
        "type_of_hardware_module": selected_type_of_hardware_module,
        "total_bits": total_bits,
        "accurate_bits": total_bits - inacc_bits
        if not selected_type_of_hardware_module == "Accurate Adder"
        else 0,
        "inaccurate_bits": inacc_bits
        if not selected_type_of_hardware_module == "Accurate Adder"
        else 0,
    }

    st.write(chosen_options)

    if st.button("Click to Generate"):
        print("clicked")
