import streamlit as st
from tools.VerilogGenerators.VerilogGenerator import VerilogGenerator

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
        "MxN AAM01 with V-cut",
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

    st.subheader("3. Select number of bits")
    col1, col2 = st.columns(2)

    with col1:
        if not selected_type_of_code == "ASIC Verilog Multiplier":
            total_bits = st.slider(
                "Total bits",
                min_value=4,
                max_value=32,
                value=4,
            )
        else:
            multiplicand_bits = st.slider(
                "Multiplicand bits",
                min_value=3,
                max_value=32,
                value=3,
            )

    with col2:
        if not selected_type_of_code == "ASIC Verilog Multiplier":
            if not selected_type_of_hardware_module == "Accurate Adder":
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
                min_value=3,
                max_value=32,
                value=3,
            )

    if selected_type_of_hardware_module == "MxN AAM01 with V-cut":
        v_cut = st.slider(
            "V Cut",
            min_value=0,
            max_value=multiplicand_bits+multiplier_bits-3,
            value=3,
        )

    st.subheader("4. Review and generate")
    chosen_options = {
        "type_of_verilog_code": selected_type_of_code,
        "type_of_hardware_module": selected_type_of_hardware_module,
        "total_bits": total_bits
        if not selected_type_of_code == "ASIC Verilog Multiplier"
        else 0,
        "accurate_bits": total_bits - inacc_bits
        if not selected_type_of_hardware_module == "Accurate Adder"
        and not selected_type_of_code == "ASIC Verilog Multiplier"
        else 0,
        "inaccurate_bits": inacc_bits
        if not selected_type_of_hardware_module == "Accurate Adder"
        and not selected_type_of_code == "ASIC Verilog Multiplier"
        else 0,
        "multiplicand_bits": multiplicand_bits
        if selected_type_of_code == "ASIC Verilog Multiplier"
        else 0,
        "multiplier_bits": multiplier_bits
        if selected_type_of_code == "ASIC Verilog Multiplier"
        else 0,
        "v_cut": v_cut
        if selected_type_of_hardware_module == "MxN AAM01 with V-cut"
        else 0,
    }

    st.write(chosen_options)

    if st.button("Click to Generate"):
        st.subheader("5. Generated Code")
        verilog_code = VerilogGenerator.generate_verilog(chosen_options)

        st.text(verilog_code)
