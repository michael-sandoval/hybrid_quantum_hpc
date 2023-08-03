# Running on Frontier

Runs a script adapted from this pennylane tutorial: https://pennylane.ai/qml/demos/tutorial_quantum_transfer_learning

Test data can be downloaded here: https://download.pytorch.org/tutorial/hymenoptera_data.zip

The script has been adapted for Frontier and made to distribute over multiple GPUs by [@Sam-Bieberich].

Eventually will place install instructions for the PyTorch environment here.

But in the meantime, these are the relevant specs:

* ROCm 5.1.0
* PyTorch (torch) 1.13.0 (built from source on Frontier using ROCm 5.1.0)
* PennyLane 0.30.0

```
sbatch -S0 --export=NONE submit_qml_gpu.sl
```
