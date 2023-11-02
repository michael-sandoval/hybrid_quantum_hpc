#!/bin/bash
#SBATCH -A XXXYYY
#SBATCH -J qml_3gpu
#SBATCH -o %x-%j.out
#SBATCH -N 1
#SBATCH -t 0:10:00
#SBATCH -p batch

unset SLURM_EXPORT_ENV

cd $SLURM_SUBMIT_DIR
date

module load PrgEnv-gnu
module load gcc/11.2.0
module load amd-mixed/5.1.0
module load craype-accel-amd-gfx90a
module unload darshan-runtime
export LD_PRELOAD="/usr/lib64/libcrypto.so /usr/lib64/libssh.so.4 /usr/lib64/libssl.so.1.1"

export MIOPEN_USER_DB_PATH="/tmp/my-miopen-cache" 
export MIOPEN_CUSTOM_CACHE_DIR=${MIOPEN_USER_DB_PATH} 
rm -rf ${MIOPEN_USER_DB_PATH} 
mkdir -p ${MIOPEN_USER_DB_PATH}

scontrol show hostnames $SLURM_NODELIST > job.node_${SLURM_JOB_ID}.list
input="./job.node_${SLURM_JOB_ID}.list"
readarray -t arr <"$input"
first=${arr[0]}
echo "first=" $first
ips=`ssh $first hostname -I`
read -ra arr <<< ${ips}
export MASTER_ADDR=${arr[0]}
echo "MASTER_ADDR=" $MASTER_ADDR

export PATH="/path/to/your/miniconda_frontier/bin:$PATH"
source activate pyt_env_310_510_mpi

export OMP_NUM_THREADS=1

which python3
srun -n3 -c7 --gpus-per-task=1 --gpu-bind=closest python3 -W ignore -u cnn_qml_distributed_mpi_1GpuPerTask.py
