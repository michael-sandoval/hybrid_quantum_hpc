#!/bin/bash
#SBATCH -A XXXYYY
#SBATCH -J qml_gpu
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

export MIOPEN_USER_DB_PATH="/tmp/my-miopen-cache" 
export MIOPEN_CUSTOM_CACHE_DIR=${MIOPEN_USER_DB_PATH} 
rm -rf ${MIOPEN_USER_DB_PATH} 
mkdir -p ${MIOPEN_USER_DB_PATH}

export PATH="/path/to/miniconda_frontier/bin:$PATH"
source activate pyt_env

which python3
python3 -W ignore -u cnn_qml_distributed.py --gpus 3
