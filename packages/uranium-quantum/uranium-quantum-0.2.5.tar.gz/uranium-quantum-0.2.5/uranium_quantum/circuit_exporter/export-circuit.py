import click
import importlib
import yaml

QiskitExporter = importlib.import_module("uranium_quantum.circuit_exporter.qiskit-exporter")
PyquilExporter = importlib.import_module("uranium_quantum.circuit_exporter.pyquil-exporter")
QuilExporter = importlib.import_module("uranium_quantum.circuit_exporter.quil-exporter")
CirqExporter = importlib.import_module("uranium_quantum.circuit_exporter.cirq-exporter")


def get_number_qubits(yaml):
    """Extract the number of qubits in yaml circuit."""
    qubits = 0
    if "steps" in yaml.keys():
        for step in yaml["steps"]:
            if "gates" in step:
                for gate in step["gates"]:
                    if "controls" in gate:
                        for ctrl_info in gate["controls"]:
                            qubits = max(qubits, ctrl_info["target"] + 1)
                    if "targets" in gate:
                        for target in gate["targets"]:
                            qubits = max(qubits, target + 1)
                    if "gates" in gate:
                        for gate in gate["gates"]:
                            for target in gate["targets"]:
                                qubits = max(qubits, target + 1)
    return qubits


def get_number_bits(yaml):
    """Extract the numebr of bits in yaml circuit."""
    bits = 0
    if "steps" in yaml.keys():
        for step in yaml["steps"]:
            if "gates" in step:
                for gate in step["gates"]:
                    if "bit" in gate:
                        bits = max(bits, gate["bit"] + 1)
    return bits


def process_yaml(yaml_data, exporter, export_format, add_comments):
    """Export quantium circuit from YAML format to target language."""
    code = exporter.start_code()
    if "steps" in yaml_data.keys():
        for step in yaml_data["steps"]:
            step_index = step["index"]
            if export_format == "qiskit":
                if add_comments:
                    code += f"\n############ New circuit step no: {step_index} ############\n\n"
            elif export_format == "openqasm":
                if add_comments:
                    code += f"\n//////////// New circuit step no: {step_index} ////////////\n\n"
            elif export_format == "pyquil":
                if add_comments:
                    code += f"\n############ New circuit step no: {step_index} ############\n\n"
            elif export_format == "quil":
                if add_comments:
                    code += f"\n############ New circuit step no: {step_index} ############\n\n"
            elif export_format == "cirq":
                if add_comments:
                    code += f"\n############ New circuit step no: {step_index} ############\n\n"
            code += exporter.process_step(step, add_comments)
    code += exporter.end_code()
    return code


def get_exported_code(file, export_format, comments):
    """Get circuit code in exported format"""

    exporter = None
    if export_format.lower() == "qiskit":
        exporter = QiskitExporter.Exporter()
    elif export_format.lower() == "openqasm":
        exporter = QiskitExporter.Exporter()
    elif export_format.lower() == "pyquil":
        exporter = PyquilExporter.Exporter()
    elif export_format.lower() == "quil":
        exporter = QuilExporter.Exporter()
    elif export_format.lower() == "cirq":
        exporter = CirqExporter.Exporter()
    else:
        raise Exception(f"Export format {export_format} is not supported.")

    quantum_code = ""
    with open(file, "r") as stream:
        try:
            yaml_data = yaml.safe_load(stream)
            no_qubits = get_number_qubits(yaml_data)
            exporter.set_number_qubits(no_qubits)
            no_bits = get_number_bits(yaml_data)
            exporter.set_number_bits(no_bits)
            if comments:
                quantum_code = process_yaml(yaml_data, exporter, export_format, add_comments=True)
            else:
                quantum_code = process_yaml(yaml_data, exporter, export_format, add_comments=False)
        except yaml.YAMLError as ex:
            quantum_code = str(ex)

    # openqasm uses QiskitExporter
    if export_format.lower() == "openqasm":
        exec(quantum_code)
        try:
            quantum_code = eval('qc.qasm()')
        except Exception as ex:
            quantum_code = "QASM translation exception: \n"
            quantum_code += str(ex)
            quantum_code += "\n"

    return quantum_code


@click.command()
@click.option(
    "--file", "-f", required=True, help="A file with quantum circuit in yaml format."
)
@click.option(
    "--export_format",
    "-e",
    required=True,
    help="Specific format for exporting the circuit into: 'qiskit', 'openqasm', 'pyquil', 'quil' or 'cirq'.",
)
@click.option(
    "-comments", "-c", required=False, help="Add comments with step index gate names in exported code."
)
def main(file, export_format, comments = False):

    output_file = file.replace(".yaml", f"_{export_format}.py")

    if not file.endswith(".yaml"):
        print("A yaml file is required as input for this script.")
        return

    if export_format.lower() == "qiskit":
        pass
    elif export_format.lower() == "openqasm":
        output_file = file.replace(".yaml", ".qasm")
    elif export_format.lower() == "pyquil":
        raise Exception("The pyquil exporter is not yet implemented.")
    elif export_format.lower() == "quil":
        output_file = file.replace(".yaml", ".quil")
        raise Exception("The quil exporter is not yet implemented.")
    elif export_format.lower() == "cirq":
        raise Exception("The cirq exporter is not yet implemented.")

    quantum_code = get_exported_code(file, export_format, comments and comments.lower() in ['true', '1', 't', 'y', 'yes'])

    if export_format.lower() == "openqasm":
        exec(quantum_code)
        try:
            quantum_code = eval('qc.qasm()')
        except Exception as ex:
            quantum_code = "QASM translation exception: \n"
            quantum_code += str(ex)
            quantum_code += "\n"

    with open(output_file, "w") as outfile:
        outfile.write(quantum_code)


if __name__ == "__main__":
    main()
