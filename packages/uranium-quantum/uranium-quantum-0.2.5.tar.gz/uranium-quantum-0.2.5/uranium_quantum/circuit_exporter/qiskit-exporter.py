import importlib
import numpy as np

BaseExporter = importlib.import_module("uranium_quantum.circuit_exporter.base-exporter")
class Exporter(BaseExporter.BaseExporter):
    def start_code(self):
        return f"\
import numpy as np\n\
from qiskit import QuantumRegister\n\
from qiskit.circuit import ClassicalRegister\n\
from qiskit import QuantumCircuit\n\
\n\
from qiskit.circuit.library.standard_gates import XGate, YGate, ZGate, HGate\n\
from qiskit.circuit.library import RXGate, RYGate, RZGate\n\
from qiskit.circuit.library import RXXGate, RYYGate, RZZGate\n\
from qiskit.circuit.library import RZXGate\n\
from qiskit.circuit.library import SXGate, SXdgGate\n\
from qiskit.circuit.library import SGate, SdgGate, TGate, TdgGate\n\
from qiskit.circuit.library import UGate, U1Gate\n\
from qiskit.circuit.library import SwapGate, iSwapGate\n\
from uranium_quantum.circuit_exporter.qiskit_custom_gates import *\n\
\n\
cr = ClassicalRegister({self._bits})\n\
qr = QuantumRegister({self._qubits})\n\
qc = QuantumCircuit(qr, cr)\n\n"

    def end_code(self):
        return f""

    @staticmethod
    def get_control_states(controls):
        controlstates = ""
        for control in controls:
            if str(control['state']) in ["0", "+", "+i"]:
                controlstates += "0"
            else:
                controlstates += "1"
        # in qiskit higher qubit indices are more significant
        # while we order controls by target index in increasing order
        controlstates = controlstates[::-1]
        return controlstates

    @staticmethod
    def get_plain_gate(name, label, theta_radians=None, phi_radians=None, lambda_radians=None, root=None):
        params = ""
        if theta_radians != None:
          params += f"{theta_radians}"
        if phi_radians != None:
          if params:
            params += f", {phi_radians}"
          else:
            params += f"{phi_radians}"
        if lambda_radians != None:
          if params:
            params += f", {lambda_radians}"
          else:
            params += f"{lambda_radians}"
        if root != None:
          if params:
            params += f", {root}"
          else:
            params += f"{root}"
        if params:
            if label:
                return f"{name}({params}, label='{label}')"
            else:
                return f"{name}({params})"
        else:
            if label:
                return f"{name}(label='{label}')"
            else:
                return f"{name}()"

    @staticmethod
    def get_controlled_gate(name, controls, label, theta_radians=None, phi_radians=None, lambda_radians=None, root=None):
        controlstates = Exporter.get_control_states(controls)
        params = ""
        if theta_radians != None:
            params += f"{theta_radians}"
        if phi_radians != None:
            if params:
                params += f", {phi_radians}"
            else:
                params += f"{phi_radians}"
        if lambda_radians != None:
            if params:
                params += f", {lambda_radians}"
            else:
                params += f"{lambda_radians}"
        if root != None:
            if params:
                params += f", {root}"
            else:
                params += f"{root}"
        if label:
            return f"{name}({params}).control(num_ctrl_qubits={len(controls)}, ctrl_state='{controlstates}', label='{label}')"
        else:
            return f"{name}({params}).control(num_ctrl_qubits={len(controls)}, ctrl_state='{controlstates}')"


    @staticmethod
    def rotate_state_to_x_basis(target):
        return f"qc.h(qr[{target}])\n"

    @staticmethod
    def rotate_state_to_y_basis(target):
        return f"qc.unitary(gate_rotation_to_y_basis(), [{target}])\n"

    @staticmethod
    def undo_rotate_state_to_x_basis(target):
        return f"qc.h(qr[{target}])\n"

    @staticmethod
    def undo_rotate_state_to_y_basis(target):
        return f"qc.unitary(gate_undo_rotation_to_y_basis(), [{target}])\n"

    @staticmethod
    def controlled_gate_code(name, controls, targets, label=None, theta_radians=None, phi_radians=None, root=None, lambda_radians=None):
        controlled_gate = Exporter.get_controlled_gate(name, controls, label, theta_radians, phi_radians, lambda_radians, root)

        qubits = ""
        for control in controls:
            if qubits:
                qubits += ", "
            qubits += f"qr[{control['target']}]"
        for target in targets:
            if qubits:
                qubits += ", "
            qubits += f"qr[{target}]"

        code = ""
        for control in controls:
            if '+i' in control['state'] or '-i' in control['state']:
                code += Exporter.rotate_state_to_y_basis(control['target'])
            elif '+' in control['state'] or '-' in control['state']:
                code += Exporter.rotate_state_to_x_basis(control['target'])

        code += f"qc.append({controlled_gate}, [{qubits}])\n"

        for control in controls:
            if '+i' in control['state'] or '-i' in control['state']:
                code += Exporter.undo_rotate_state_to_y_basis(control['target'])
            elif '+' in control['state'] or '-' in control['state']:
                code += Exporter.undo_rotate_state_to_x_basis(control['target'])

        return code


    @staticmethod
    def plain_gate_code(name, targets, label=None, theta_radians=None, phi_radians=None, root=None, lambda_radians=None):
        plain_gate = Exporter.get_plain_gate(name, label, theta_radians, phi_radians, lambda_radians, root)
        qubits = ""
        for target in targets:
            if qubits:
                qubits += ", "
            qubits += f"qr[{target}]"
        return f"qc.append({plain_gate}, [{qubits}])"

    @staticmethod
    def _gate_u3(
        controls, targets, theta_radians, phi_radians, lambda_radians, add_comments=True
    ):
        out = "# u3 gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('UGate', controls, targets, theta_radians=theta_radians, phi_radians=phi_radians, lambda_radians=lambda_radians)
            out += f"{code}"
        else:
            out += f"qc.u({theta_radians}, {phi_radians}, {lambda_radians}, qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_u2(controls, targets, phi_radians, lambda_radians, add_comments=True):
        out = "# u2 gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('UGate', controls, targets, theta_radians=(np.pi/2), phi_radians=phi_radians, lambda_radians=lambda_radians)
            out += f"{code}"
        else:
            out += f"qc.u(np.pi/2, {phi_radians}, {lambda_radians}, qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_u1(controls, targets, lambda_radians, add_comments=True):
        out = "# u1 gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('U1Gate', controls, targets, lambda_radians=lambda_radians)
            out += f"{code}"
        else:
            out += f"qc.p({lambda_radians}, qr[{targets[0]}])\n"
        return out


    @staticmethod
    def _gate_identity(targets, add_comments=True):
        out = "# identity gate\n" if add_comments else ""
        out += f"qc.id(qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_hadamard(controls, targets, add_comments=True):
        out = "# hadamard gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('HGate', controls, targets)
            out += f"{code}"
        else:
            out += f"qc.h(qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_hadamard_xy(controls, targets, add_comments=True):
        out = "# hadamard-xy gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('hadamard_xy', controls, targets, label='hadamard-xy')
            out += f"{code}"
        else:
            out += f"qc.unitary(hadamard_xy(), [{targets[0]}], label='hadamard-xy')\n"
        return out

    @staticmethod
    def _gate_hadamard_yz(controls, targets, add_comments=True):
        out = "# hadamard-yz gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('hadamard_yz', controls, targets, label='hadamard-yz')
            out += f"{code}"
        else:
            out += f"qc.unitary(hadamard_yz(), [{targets[0]}], label='hadamard-yz')\n"
        return out

    @staticmethod
    def _gate_hadamard_zx(controls, targets, add_comments=True):
        out = "# hadamard-zx gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('HGate', controls, targets)
            out += f"{code}"
        else:
            out += f"qc.h(qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_pauli_x(controls, targets, add_comments=True):
        out = "# pauli-x gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('XGate', controls, targets)
            out += f"{code}"
        else:
            out += f"qc.x(qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_pauli_y(controls, targets, add_comments=True):
        out = "# pauli-y gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('YGate', controls, targets)
            out += f"{code}"
        else:
            out += f"qc.y(qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_pauli_z(controls, targets, add_comments=True):
        out = "# pauli-z gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('ZGate', controls, targets)
            out += f"{code}"
        else:
            out += f"qc.z(qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_pauli_x_root(controls, targets, root, add_comments=True):
        out = "# pauli-x-root gate\n" if add_comments else ""
        root = f"(2**{root[4:]})" if '^' in root else root[2:]
        if controls:
            code = Exporter.controlled_gate_code('pauli_x_root', controls, targets, root=root, label='pauli-x-root')
            out += f"{code}"
        else:
            out += f"qc.unitary(pauli_x_root({root}), [{targets[0]}], label='pauli-x-root')\n"
        return out

    @staticmethod
    def _gate_pauli_y_root(controls, targets, root, add_comments=True):
        out = "# pauli-y-root gate\n" if add_comments else ""
        root = f"(2**{root[4:]})" if '^' in root else root[2:]
        if controls:
            code = Exporter.controlled_gate_code('pauli_y_root', controls, targets, root=root, label='pauli-y-root')
            out += f"{code}"
        else:
            out += f"qc.unitary(pauli_y_root({root}), [{targets[0]}], label='pauli-y-root')\n"
        return out

    @staticmethod
    def _gate_pauli_z_root(controls, targets, root, add_comments=True):
        out = "# pauli-z-root gate\n" if add_comments else ""
        root = f"(2**{root[4:]})" if '^' in root else root[2:]
        if controls:
            code = Exporter.controlled_gate_code('pauli_z_root', controls, targets, root=root, label='pauli-z-root')
            out += f"{code}"
        else:
            out += f"qc.unitary(pauli_z_root({root}), [{targets[0]}], label='pauli-z-root')\n"
        return out

    @staticmethod
    def _gate_pauli_x_root_dagger(controls, targets, root, add_comments=True):
        out = "# pauli-x-root-dagger gate\n" if add_comments else ""
        root = f"(2**{root[4:]})" if '^' in root else root[2:]
        if controls:
            code = Exporter.controlled_gate_code('pauli_x_root_dagger', controls, targets, root=root, label='pauli-x-root-dagger')
            out += f"{code}"
        else:
            out += f"qc.unitary(pauli_x_root_dagger({root}), [{targets[0]}], label='pauli-x-root-dagger')\n"
        return out

    @staticmethod
    def _gate_pauli_y_root_dagger(controls, targets, root, add_comments=True):
        out = "# pauli-y-root-dagger gate\n" if add_comments else ""
        root = f"(2**{root[4:]})" if '^' in root else root[2:]
        if controls:
            code = Exporter.controlled_gate_code('pauli_y_root_dagger', controls, targets, root=root, label='pauli-y-root-dagger')
            out += f"{code}"
        else:
            out += f"qc.unitary(pauli_y_root_dagger({root}), [{targets[0]}], label='pauli-y-root-dagger')\n"
        return out

    @staticmethod
    def _gate_pauli_z_root_dagger(controls, targets, root, add_comments=True):
        out = "# pauli-z-root-dagger gate\n" if add_comments else ""
        root = f"(2**{root[4:]})" if '^' in root else root[2:]
        if controls:
            code = Exporter.controlled_gate_code('pauli_z_root_dagger', controls, targets, root=root, label='pauli-z-root-dagger')
            out += f"{code}"
        else:
            out += f"qc.unitary(pauli_z_root_dagger({root}), [{targets[0]}], label='pauli-z-root-dagger')\n"
        return out

    @staticmethod
    def _gate_t(controls, targets, add_comments=True):
        out = "# t gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('TGate', controls, targets)
            out += f"{code}"
        else:
            out += f"qc.t(qr[{targets[0]}])\n"
        return out


    @staticmethod
    def _gate_t_dagger(controls, targets, add_comments=True):
        out = "# t-dagger gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('TdgGate', controls, targets)
            out += f"{code}"
        else:
            out += f"qc.tdg(qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_rx_theta(controls, targets, theta_radians, add_comments=True):
        out = "# rx-theta gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('RXGate', controls, targets, theta_radians=theta_radians)
            out += f"{code}"
        else:
            out += f"qc.rx({theta_radians}, qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_ry_theta(controls, targets, theta_radians, add_comments=True):
        out = "# ry-theta gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('RYGate', controls, targets, theta_radians=theta_radians)
            out += f"{code}"
        else:
            out += f"qc.ry({theta_radians}, qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_rz_theta(controls, targets, theta_radians, add_comments=True):
        out = "# rz-theta gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('RZGate', controls, targets, theta_radians=theta_radians)
            out += f"{code}"
        else:
            out += f"qc.rz({theta_radians}, qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_v(controls, targets, add_comments=True):
        out = "# v gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('SXGate', controls, targets)
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('SXGate', targets)
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_v_dagger(controls, targets, add_comments=True):
        out = "# v-dagger gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('SXdgGate', controls, targets)
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('SXdgGate', targets)
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_h(controls, targets, add_comments=True):
        out = "# h gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('h', controls, targets, label='h')
            out += f"{code}"
        else:
            out += f"qc.unitary(h(), [{targets[0]}], label='h')\n"
        return out

    @staticmethod
    def _gate_h_dagger(controls, targets, add_comments=True):
        out = "# h-dagger gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('h_dagger', controls, targets, label='h-dagger')
            out += f"{code}"
        else:
            out += f"qc.unitary(h_dagger(), [{targets[0]}], label='h-dagger')\n"
        return out

    @staticmethod
    def _gate_c(controls, targets, add_comments=True):
        out = "# c gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('c', controls, targets, label='c')
            out += f"{code}"
        else:
            out += f"qc.unitary(c(), [{targets[0]}], label='c')\n"
        return out

    @staticmethod
    def _gate_c_dagger(controls, targets, add_comments=True):
        out = "# c-dagger gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('c_dagger', controls, targets, label='c-dagger')
            out += f"{code}"
        else:
            out += f"qc.unitary(c_dagger(), [{targets[0]}], label='c-dagger')\n"
        return out


    @staticmethod
    def _gate_p(controls, targets, theta_radians, add_comments=True):
        out = "# p gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('U1Gate', controls, targets, theta_radians=theta_radians)
            out += f"{code}"
        else:
            out += f"qc.p({theta_radians}, qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_s(controls, targets, add_comments=True):
        out = "# s gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('SGate', controls, targets)
            out += f"{code}"
        else:
            out += f"qc.s(qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_s_dagger(controls, targets, add_comments=True):
        out = "# s-dagger gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('SdgGate', controls, targets)
            out += f"{code}"
        else:
            out += f"qc.sdg(qr[{targets[0]}])\n"
        return out

    @staticmethod
    def _gate_swap(controls, targets, add_comments=True):
        out = "# swap gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('SwapGate', controls, targets)
            out += f"{code}"
        else:
            out += f"qc.swap(qr[{targets[0]}], qr[{targets[1]}])\n"
        return out

    @staticmethod
    def _gate_swap_root(controls, targets, root, add_comments=True):
        out = "# swap root gate\n" if add_comments else ""
        root = f"(2**{root[4:]})" if '^' in root else root[2:]
        if controls:
            code = Exporter.controlled_gate_code('swap_root', controls, targets, root=root, label="swap-root")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('swap_root', targets, root=root, label="swap-root")
            out += f"{code}\n"
        return out


    @staticmethod
    def _gate_swap_root_dagger(controls, targets, root, add_comments=True):
        out = "# swap root dagger gate\n" if add_comments else ""
        root = f"(2**{root[4:]})" if '^' in root else root[2:]
        if controls:
            code = Exporter.controlled_gate_code('swap_root_dagger', controls, targets, root=root, label="swap-root-dagger")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('swap_root_dagger', targets, root=root, label="swap-root-dagger")
            out += f"{code}\n"
        return out

  
    @staticmethod
    def _gate_iswap(controls, targets, add_comments=True):
        out = "# iswap gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('iSwapGate', controls, targets)
            out += f"{code}"
        else:
            out += f"qc.iswap(qr[{targets[0]}], qr[{targets[1]}])\n"
        return out

    @staticmethod
    def _gate_fswap(controls, targets, add_comments=True):
        out = "# fswap gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('fswap', controls, targets, label="fswap")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('fswap', targets, label="fswap")
            out += f"{code}\n"
        return out


    @staticmethod
    def _gate_swap_theta(controls, targets, theta_radians, add_comments=True):
        out = "# swap theta gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('swap_theta', controls, targets, theta_radians=theta_radians, label="swap-theta")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('swap_theta', targets, theta_radians=theta_radians, label="swap-theta")
            out += f"{code}\n"
        return out


    @staticmethod
    def _gate_sqrt_swap(controls, targets, add_comments=True):
        out = "# sqrt-swap gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('sqrt_swap', controls, targets, label="sqrt-swap")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('sqrt_swap', targets, label="sqrt-swap")
            out += f"{code}\n"
        return out


    @staticmethod
    def _gate_sqrt_swap_dagger(controls, targets, add_comments=True):
        out = "# sqrt-swap-dagger gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('sqrt_swap_dagger', controls, targets, label="sqrt-swap-dagger")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('sqrt_swap_dagger', targets, label="sqrt-swap-dagger")
            out += f"{code}\n"
        return out


    @staticmethod
    def _gate_xx(controls, targets, theta_radians, add_comments=True):
        out = "# xx gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('RXXGate', controls, targets, theta_radians=theta_radians)
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('RXXGate', targets, theta_radians=theta_radians)
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_yy(controls, targets, theta_radians, add_comments=True):
        out = "# yy gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('RYYGate', controls, targets, theta_radians=theta_radians)
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('RYYGate', targets, theta_radians=theta_radians)
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_zz(controls, targets, theta_radians, add_comments=True):
        out = "# zz gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('RZZGate', controls, targets, theta_radians=theta_radians)
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('RZZGate', targets, theta_radians=theta_radians)
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_xy(controls, targets, theta_radians, add_comments=True):
        out = "# xy gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('xy', controls, targets, theta_radians=theta_radians, label="xy")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('xy', targets, theta_radians=theta_radians, label="xy")
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_givens(controls, targets, theta_radians, add_comments=True):
        out = "# givens gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('givens', controls, targets, theta_radians=theta_radians, label="givens")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('givens', targets, theta_radians=theta_radians, label="givens")
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_a(controls, targets, theta_radians, phi_radians, add_comments=True):
        out = "# a gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('a', controls, targets, theta_radians=theta_radians, phi_radians=phi_radians, label="a")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('a', targets, theta_radians=theta_radians, phi_radians=phi_radians, label="a")
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_cross_resonance(controls, targets, theta_radians, add_comments=True):
        out = "# crosss-resonance gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('RZXGate', controls, targets, theta_radians=theta_radians, label='cross-resonance')
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('RZXGate', targets, theta_radians=theta_radians)
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_cross_resonance_dagger(controls, targets, theta_radians, add_comments=True):
        out = "# crosss-resonance-dagger gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('RZXGate', controls, targets, theta_radians=-theta_radians, label='cross-resonance-dg')
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('RZXGate', targets, theta_radians=-theta_radians)
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_molmer_sorensen(controls, targets, add_comments=True):
        out = "# molmer-sorensen gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('molmer_sorensen', controls, targets, label="molmer-sorensen")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('molmer_sorensen', targets, label="molmer-sorensen")
            out += f"{code}\n"
        return out


    @staticmethod
    def _gate_molmer_sorensen_dagger(controls, targets, add_comments=True):
        out = "# molmer-sorensen-dagger gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('molmer_sorensen_dagger', controls, targets, label="molmer-sorensen-dagger")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('molmer_sorensen_dagger', targets, label="molmer-sorensen-dagger")
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_berkeley(controls, targets, add_comments=True):
        out = "# berkeley gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('berkeley', controls, targets, label="berkeley")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('berkeley', targets, label="berkeley")
            out += f"{code}\n"
        return out


    @staticmethod
    def _gate_berkeley_dagger(controls, targets, add_comments=True):
        out = "# berkeley-dagger gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('berkeley_dagger', controls, targets, label="berkeley-dagger")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('berkeley_dagger', targets, label="berkeley-dagger")
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_ecp(controls, targets, add_comments=True):
        out = "# ecp gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('ecp', controls, targets, label="ecp")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('ecp', targets, label="ecp")
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_ecp_dagger(controls, targets, add_comments=True):
        out = "# ecp-dagger gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('ecp_dagger', controls, targets, label="ecp-dagger")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('ecp_dagger', targets, label="ecp-dagger")
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_magic(controls, targets, add_comments=True):
        out = "# magic gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('magic', controls, targets, label="magic")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('magic', targets, label="magic")
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_magic_dagger(controls, targets, add_comments=True):
        out = "# magic-dagger gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('magic_dagger', controls, targets, label="magic-dagger")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('magic_dagger', targets, label="magic-dagger")
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_w(controls, targets, add_comments=True):
        out = "# w gate\n" if add_comments else ""
        if controls:
            code = Exporter.controlled_gate_code('w', controls, targets, label="w")
            out += f"{code}"
        else:
            code = Exporter.plain_gate_code('w', targets, label="w")
            out += f"{code}\n"
        return out

    @staticmethod
    def _gate_qft(controls, targets, add_comments=True):
        raise BaseExporter.ExportException("The qft gate is not yet implemented.")

    @staticmethod
    def _gate_qft_dagger(controls, targets, add_comments=True):
        raise BaseExporter.ExportException("The qft gate is not yet implemented.")

    @staticmethod
    def _gate_measure_x(targets, classic_bit, add_comments=True):
        raise BaseExporter.ExportException("The measure-x gate is not implemented.")

    @staticmethod
    def _gate_measure_y(targets, classic_bit, add_comments=True):
        raise BaseExporter.ExportException("The measure-y gate is not implemented.")

    @staticmethod
    def _gate_measure_z(targets, classic_bit, add_comments=True):
        out = "# measure-z gate\n" if add_comments else ""
        out += f"qc.measure({targets[0]}, {classic_bit})\n"
        return out
