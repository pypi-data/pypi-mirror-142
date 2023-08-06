class ExportException(Exception):
    pass


class BaseExporter:

    """Base class for exporting circuits from YAML format.
    to Qiskit, OpenQasm, Pyquil, Quil and Cirq."""

    def __init__(self):
        self._qubits = None

    def set_number_qubits(self, qubits):
        """Set the number of qubits in this circuit."""
        self._qubits = qubits

    def set_number_bits(self, bits):
        """Set the number of classical bits in this circuit."""
        self._bits = bits

    def process_step(self, step, add_comments):
        """Export gates present in one step from the input YAML file."""
        output = ""
        if "gates" in step:
            for gate in step["gates"]:

                controls, targets, gates, root, theta_radians, phi_radians, lambda_radians, bit = (
                    [],
                    [],
                    [],
                    None,
                    None,
                    None,
                    None,
                    None
                )
                if "controls" in gate:
                    controls = gate["controls"]
                if "targets" in gate:
                    targets = gate["targets"]
                if "gates" in gate:
                    gates = gate["gates"]
                if "root" in gate:
                    root = gate["root"]
                if "theta" in gate:
                    theta_radians = gate["theta"]
                if "phi" in gate:
                    phi_radians = gate["phi"]
                if "lambda" in gate:
                    lambda_radians = gate["lambda"]
                if "bit" in gate:
                    bit = gate["bit"]

                name = gate["name"]
                output += self.process_gate(
                    name,
                    controls,
                    targets,
                    gates,
                    root,
                    theta_radians,
                    phi_radians,
                    lambda_radians,
                    bit,
                    add_comments,
                )
                output += "\n"
        return output

    def process_gate(
        self,
        name,
        controls,
        targets,
        gates,
        root,
        theta_radians,
        phi_radians,
        lambda_radians,
        bit,
        add_comments,
    ):
        """Create export code corresponding to a gate in yaml circuit."""
        if name == "u3":
            return self._gate_u3(
                controls, targets, theta_radians, phi_radians, lambda_radians, add_comments,
            )
        elif name == "u2":
            return self._gate_u2(
                controls, targets, phi_radians, lambda_radians, add_comments
            )
        elif name == "u1":
            return self._gate_u1(
                controls, targets, lambda_radians, add_comments
            )
        elif name == "identity":
            return self._gate_identity(
                targets, add_comments)
        elif name == "hadamard":
            return self._gate_hadamard(
                controls, targets, add_comments
            )
        elif name == "hadamard-xy":
            return self._gate_hadamard_xy(
                controls, targets, add_comments
            )
        elif name == "hadamard-yz":
            return self._gate_hadamard_yz(
                controls, targets, add_comments
            )
        elif name == "hadamard-zx":
            return self._gate_hadamard_zx(
                controls, targets, add_comments
            )
        elif name == "pauli-x":
            return self._gate_pauli_x(
                controls, targets, add_comments
            )
        elif name == "pauli-y":
            return self._gate_pauli_y(
                controls, targets, add_comments
            )
        elif name == "pauli-z":
            return self._gate_pauli_z(
                controls, targets, add_comments
            )
        elif name == "pauli-x-root":
            return self._gate_pauli_x_root(
                controls, targets, root, add_comments
            )
        elif name == "pauli-y-root":
            return self._gate_pauli_y_root(
                controls, targets, root, add_comments
            )
        elif name == "pauli-z-root":
            return self._gate_pauli_z_root(
                controls, targets, root, add_comments
            )
        elif name == "pauli-x-root-dagger":
            return self._gate_pauli_x_root_dagger(
                controls, targets, root, add_comments
            )
        elif name == "pauli-y-root-dagger":
            return self._gate_pauli_y_root_dagger(
                controls, targets, root, add_comments
            )
        elif name == "pauli-z-root-dagger":
            return self._gate_pauli_z_root_dagger(
                controls, targets, root, add_comments
            )
        elif name == "t":
            return self._gate_t(
                controls, targets, add_comments
            )
        elif name == "t-dagger":
            return self._gate_t_dagger(
                controls, targets, add_comments
            )
        elif name == "s":
            return self._gate_s(
                controls, targets, add_comments
            )
        elif name == "s-dagger":
            return self._gate_s_dagger(
                controls, targets, add_comments
            )
        elif name == "rx-theta":
            return self._gate_rx_theta(
                controls, targets, theta_radians, add_comments
            )
        elif name == "ry-theta":
            return self._gate_ry_theta(
                controls, targets, theta_radians, add_comments
            )
        elif name == "rz-theta":
            return self._gate_rz_theta(
                controls, targets, theta_radians, add_comments
            )
        elif name == "v":
            return self._gate_v(
                controls, targets, add_comments
            )
        elif name == "v-dagger":
            return self._gate_v_dagger(
                controls, targets, add_comments
            )
        elif name == "h":
            return self._gate_h(
                controls, targets, add_comments
            )
        elif name == "h-dagger":
            return self._gate_h_dagger(
                controls, targets, add_comments
            )
        elif name == "c":
            return self._gate_c(
                controls, targets, add_comments
            )
        elif name == "c-dagger":
            return self._gate_c_dagger(
                controls, targets, add_comments
            )
        elif name == "p":
            return self._gate_p(
                controls, targets, theta_radians, add_comments
            )
        elif name == "swap":
            return self._gate_swap(
                controls, targets, add_comments
            )
        elif name == "swap-root":
            return self._gate_swap_root(
                controls, targets, root, add_comments
            )
        elif name == "swap-root-dagger":
            return self._gate_swap_root_dagger(
                controls, targets, root, add_comments
            )
        elif name == "iswap":
            return self._gate_iswap(
                controls, targets, add_comments
            )
        elif name == "fswap":
            return self._gate_fswap(
                controls, targets, add_comments
            )
        elif name == "sqrt-swap":
            return self._gate_sqrt_swap(
                controls, targets, add_comments
            )
        elif name == "sqrt-swap-dagger":
            return self._gate_sqrt_swap_dagger(
                controls, targets, add_comments
            )
        elif name == "swap-theta":
            return self._gate_swap_theta(
                controls, targets, theta_radians, add_comments
            )
        elif name == "xx":
            return self._gate_xx(
                controls, targets, theta_radians, add_comments
            )
        elif name == "yy":
            return self._gate_yy(
                controls, targets, theta_radians, add_comments
            )
        elif name == "zz":
            return self._gate_zz(
                controls, targets, theta_radians, add_comments
            )
        elif name == "xy":
            return self._gate_xy(
                controls, targets, theta_radians, add_comments
            )
        elif name == "molmer-sorensen":
            return self._gate_molmer_sorensen(
                controls, targets, add_comments
            )
        elif name == "molmer-sorensen-dagger":
            return self._gate_molmer_sorensen_dagger(
                controls, targets, add_comments
            )
        elif name == "berkeley":
            return self._gate_berkeley(
                controls, targets, add_comments
            )
        elif name == "berkeley-dagger":
            return self._gate_berkeley_dagger(
                controls, targets, add_comments
            )
        elif name == "ecp":
            return self._gate_ecp(
                controls, targets, add_comments
            )
        elif name == "ecp-dagger":
            return self._gate_ecp_dagger(
                controls, targets, add_comments
            )
        elif name == "w":
            return self._gate_w(
                controls, targets, add_comments
            )
        elif name == "a":
            return self._gate_a(
                controls, targets, theta_radians, phi_radians, add_comments
            )
        elif name == "magic":
            return self._gate_magic(
                controls, targets, add_comments
            )
        elif name == "magic-dagger":
            return self._gate_magic_dagger(
                controls, targets, add_comments
            )
        elif name == "givens":
            return self._gate_givens(
                controls, targets, theta_radians, add_comments
            )
        elif name == "cross-resonance":
            return self._gate_cross_resonance(
                controls, targets, theta_radians, add_comments
            )
        elif name == "cross-resonance-dagger":
            return self._gate_cross_resonance_dagger(
                controls, targets, theta_radians, add_comments
            )
        elif name == "qft":
            return self._gate_qft(
                controls, targets, add_comments
            )
        elif name == "qft-dagger":
            return self._gate_qft_dagger(
                controls, targets, add_comments
            )
        elif name == "barrier":
            return self._gate_barrier(
                add_comments
            )
        elif name == "measure-x":
            return self._gate_measure_x(
                targets, bit, add_comments
            )
        elif name == "measure-y":
            return self._gate_measure_y(
                targets, bit, add_comments
            )
        elif name == "measure-z":
            return self._gate_measure_z(
                targets, bit, add_comments
            )
        elif name == "aggregate":
            code = ""
            for gate in gates:
                if gate["name"] == "u3":
                    if len(code): code += "\n"
                    code += self._gate_u3(
                        controls, gate["targets"], gate["theta"], gate["phi"], gate["lambda"], add_comments,
                    )
                elif gate["name"] == "u2":
                    if len(code): code += "\n"
                    code += self._gate_u2(
                        controls, gate["targets"], gate["phi"], gate["lambda"], add_comments
                    )
                elif gate["name"] == "u1":
                    if len(code): code += "\n"
                    code += self._gate_u1(
                        controls, gate["targets"], gate["lambda"], add_comments
                    )
                elif gate["name"] == "identity":
                    if len(code): code += "\n"
                    code += self._gate_identity(
                        gate["targets"], add_comments)
                elif gate["name"] == "hadamard":
                    if len(code): code += "\n"
                    code += self._gate_hadamard(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "hadamard-xy":
                    if len(code): code += "\n"
                    code += self._gate_hadamard_xy(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "hadamard-yz":
                    if len(code): code += "\n"
                    code += self._gate_hadamard_yz(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "hadamard-zx":
                    if len(code): code += "\n"
                    code += self._gate_hadamard_zx(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "pauli-x":
                    if len(code): code += "\n"
                    code += self._gate_pauli_x(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "pauli-y":
                    if len(code): code += "\n"
                    code += self._gate_pauli_y(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "pauli-z":
                    if len(code): code += "\n"
                    code += self._gate_pauli_z(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "pauli-x-root":
                    if len(code): code += "\n"
                    code += self._gate_pauli_x_root(
                        controls, gate["targets"], gate["root"], add_comments
                    )
                elif gate["name"] == "pauli-y-root":
                    if len(code): code += "\n"
                    code += self._gate_pauli_y_root(
                        controls, gate["targets"], gate["root"], add_comments
                    )
                elif gate["name"] == "pauli-z-root":
                    if len(code): code += "\n"
                    code += self._gate_pauli_z_root(
                        controls, gate["targets"], gate["root"], add_comments
                    )
                elif gate["name"] == "pauli-x-root-dagger":
                    if len(code): code += "\n"
                    code += self._gate_pauli_x_root_dagger(
                        controls, gate["targets"], gate["root"], add_comments
                    )
                elif gate["name"] == "pauli-y-root-dagger":
                    if len(code): code += "\n"
                    code += self._gate_pauli_y_root_dagger(
                        controls, gate["targets"], gate["root"], add_comments
                    )
                elif gate["name"] == "pauli-z-root-dagger":
                    if len(code): code += "\n"
                    code += self._gate_pauli_z_root_dagger(
                        controls, gate["targets"], gate["root"], add_comments
                    )
                elif gate["name"] == "t":
                    if len(code): code += "\n"
                    code += self._gate_t(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "t-dagger":
                    if len(code): code += "\n"
                    code += self._gate_t_dagger(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "s":
                    if len(code): code += "\n"
                    code += self._gate_s(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "s-dagger":
                    if len(code): code += "\n"
                    code += self._gate_s_dagger(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "rx-theta":
                    if len(code): code += "\n"
                    code += self._gate_rx_theta(
                        controls, gate["targets"], gate["theta"], add_comments
                    )
                elif gate["name"] == "ry-theta":
                    if len(code): code += "\n"
                    code += self._gate_ry_theta(
                        controls, gate["targets"], gate["theta"], add_comments
                    )
                elif gate["name"] == "rz-theta":
                    if len(code): code += "\n"
                    code += self._gate_rz_theta(
                        controls, gate["targets"], gate["theta"], add_comments
                    )
                elif gate["name"] == "v":
                    if len(code): code += "\n"
                    code += self._gate_v(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "v-dagger":
                    if len(code): code += "\n"
                    code += self._gate_v_dagger(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "h":
                    if len(code): code += "\n"
                    code += self._gate_h(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "h-dagger":
                    if len(code): code += "\n"
                    code += self._gate_h_dagger(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "c":
                    if len(code): code += "\n"
                    code += self._gate_c(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "c-dagger":
                    if len(code): code += "\n"
                    code += self._gate_c_dagger(
                        controls, gate["targets"], add_comments
                    )
                elif gate["name"] == "p":
                    if len(code): code += "\n"
                    code += self._gate_p(
                        controls, gate["targets"], gate["theta"], add_comments
                    )
            return code
        raise ExportException(f"The gate {name} is not implemented in exporter code.")

    @staticmethod
    def _gate_u3(
        controls, targets, theta_radians, phi_radians, lambda_radians, add_comments
    ):
        return ""

    @staticmethod
    def _gate_u2(controls, targets, phi_radians, lambda_radians, add_comments):
        return ""

    @staticmethod
    def _gate_u1(controls, targets, lambda_radians, add_comments):
        return ""

    @staticmethod
    def _gate_identity(targets, add_comments):
        return ""

    @staticmethod
    def _gate_hadamard(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_hadamard_xy(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_hadamard_yz(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_hadamard_zx(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_pauli_x(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_pauli_y(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_pauli_z(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_pauli_x_root(controls, targets, root, add_comments):
        return ""

    @staticmethod
    def _gate_pauli_y_root(controls, targets, root, add_comments):
        return ""

    @staticmethod
    def _gate_pauli_z_root(controls, targets, root, add_comments):
        return ""

    @staticmethod
    def _gate_pauli_x_root_dagger(controls, targets, root, add_comments):
        return ""

    @staticmethod
    def _gate_pauli_y_root_dagger(controls, targets, root, add_comments):
        return ""

    @staticmethod
    def _gate_pauli_z_root_dagger(controls, targets, root, add_comments):
        return ""

    @staticmethod
    def _gate_t(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_t_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_rx_theta(controls, targets, theta, add_comments):
        return ""

    @staticmethod
    def _gate_ry_theta(controls, targets, theta, add_comments):
        return ""

    @staticmethod
    def _gate_rz_theta(controls, targets, theta, add_comments):
        return ""

    @staticmethod
    def _gate_s(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_s_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_v(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_v_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_h(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_h_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_c(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_c_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_p(controls, targets, theta, add_comments):
        return ""

    @staticmethod
    def _gate_swap(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_swap_root(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_swap_root_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_iswap(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_fswap(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_swap_theta(controls, targets, phi, add_comments):
        return ""

    @staticmethod
    def _gate_sqrt_swap(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_sqrt_swap_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_xx(controls, targets, theta, add_comments):
        return ""

    @staticmethod
    def _gate_yy(controls, targets, theta, add_comments):
        return ""

    @staticmethod
    def _gate_zz(controls, targets, theta, add_comments):
        return ""

    @staticmethod
    def _gate_xy(controls, targets, theta, add_comments):
        return ""

    @staticmethod
    def _gate_molmer_sorensen(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_molmer_sorensen_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_berkeley(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_berkeley_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_ecp(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_ecp_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_w(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_a(controls, targets, theta, phi, add_comments):
        return ""

    @staticmethod
    def _gate_magic(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_magic_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_givens(controls, targets, theta, add_comments):
        return ""

    @staticmethod
    def _gate_measure_x(target, classic_bit, add_comments):
        return ""

    @staticmethod
    def _gate_cross_resonance(controls, targets, theta, add_comments):
        return ""

    @staticmethod
    def _gate_cross_resonance_dagger(controls, targets, theta, add_comments):
        return ""

    @staticmethod
    def _gate_measure_y(target, classic_bit, add_comments):
        return ""

    @staticmethod
    def _gate_measure_z(target, classic_bit, add_comments):
        return ""

    @staticmethod
    def _gate_aggregate(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_qft(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_qft_dagger(controls, targets, add_comments):
        return ""

    @staticmethod
    def _gate_barrier(add_comments):
        return ""