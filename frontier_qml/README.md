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
sbatch --export=NONE submit_3gpu.sl
```

## Different Codes

* `cnn_qml_distributed.py`: The original (outdated) distributed code, which utilizes a PyTorch spawner to spawn threads across a user-provided number of GPUs (does NOT work with multiple nodes). Relevant batch script is `submit_qml_gpu_outdated.sl`

* `cnn_qml_distributed_mpi_1GpuPerTask.py`: The updated distributed code which utilizes mpi4py and `srun` to spawn threads (works across multiple nodes). Meant to be run with 1 GPU per task like so (e.g., for 3 GPUs): `srun -n3 -c7 --gpus-per-task=1 --gpu-bind=closest python3 -W ignore -u script.py` . Relevant batch script is `submit_3gpu.sl`

* `cnn_qml_distributed_torchrun_cpu.py`: Bonus script if ever need to run across multiple CPUs (no GPUs) of a system using torchrun (mpi4py syntax provided in comments). Meant to be run like so (e.g., for 3 threads): `torchrun --standalone --nnodes=1 --nproc_per_node=3 script.py`
