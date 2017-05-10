#!/bin/bash

#SBATCH --time=02:10:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=16384M   # memory per CPU core
#SBATCH -J "auvsi"   # job name
#SBATCH --mail-user=gellings13@gmail.com   # email address
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END

# Compatibility variables for PBS. Delete if not needed.
export PBS_NODEFILE=`/fslapps/fslutils/generate_pbs_nodefile`
export PBS_JOBID=$SLURM_JOB_ID
export PBS_O_WORKDIR="$SLURM_SUBMIT_DIR"
export PBS_QUEUE=batch

# Set the max number of threads to use for programs using OpenMP. Should be <= ppn. Does nothing if the program doesn't use OpenMP.
export OMP_NUM_THREADS=$SLURM_CPUS_ON_NODE

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE
module purge
module load cuda/7.5.18
module load cudnn/4.0_gcc-4.4.7
module load tensorflow/0.9.0_python-3.4.4+cuda

#cd tf_jaron
python classification_hw5b.py
#python transform_hw5b.py
#python transform_classify_hw5b.py
#cd ..
