import numpy as np
import time as tp
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram
from qiskit.providers.jobstatus import JobStatus

t0 = tp.time()

QiskitRuntimeService.save_account(channel="ibm_quantum", token="API TOKEN GOES HERE", overwrite=True)
service = QiskitRuntimeService(channel="ibm_quantum", instance="ibm-q-ornl/ornl/csc431")

t1=tp.time()

backend = service.backend("ibmq_qasm_simulator", instance="ibm-q-ornl/ornl/csc431") #does not work with backend.run()

circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0,1], [0,1])
compiled_circuit = transpile(circuit, backend)

t2 = tp.time()

sampl = Sampler(backend)
job = sampl.run(compiled_circuit,shots=1000)

print("Job status is", job.status() )
result = job.result()

t3 = tp.time()

print(f'Time between beginning of script and job results: {t3-t0}')
print(f'Time between circuit construction and job results: {t3-t1}')
print(f'Time between job sumission and job results: {t3-t2}')

probs = result.quasi_dists
print("\nProbabilities for 00 and 11 are:",probs)

# Draw the circuit
print(circuit.draw())
