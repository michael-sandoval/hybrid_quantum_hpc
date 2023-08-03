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

with Session(service=service, backend="ibmq_qasm_simulator") as session:
    sampl = Sampler(backend)
    n_jobs = 10
    t_dum = 0
    for i in range(0,n_jobs):
        t_loop_0 = tp.time()
        job = sampl.run(compiled_circuit,shots=1000)
        result = job.result()
        t_loop_1 = tp.time()
        print(f'Job {i} execution time {t_loop_1 - t_loop_0}')
        t_dum +=(t_loop_1 - t_loop_0)
    t_ave = t_dum / n_jobs

    # Close the session only if all jobs are finished, and you don't need to run more in the session
    session.close() # Closes the session

t3 = tp.time()

print(f'Average time per job in session: {t_ave}')
print(f'Time between beginning of script and end of session: {t3-t0}')
print(f'Time between circuit construction and end of session: {t3-t1}')
print(f'Time of entire session: {t3-t2}')

probs = result.quasi_dists
print("\nProbabilities for 00 and 11 in the last job of the session are:",probs)

# Draw the circuit
print(circuit.draw())
