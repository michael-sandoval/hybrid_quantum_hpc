# Running on Frontier

Runs a script adapted from this pennylane tutorial: https://pennylane.ai/qml/demos/tutorial_quantum_transfer_learning
The script has been adapted for Frontier and made to distribute over multiple GPUs.

Eventually will place install instructions for the PyTorch environment here.

```
sbatch -S0 --export=NONE submit_qml_gpu.sl
```
