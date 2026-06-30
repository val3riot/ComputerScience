#!/bin/bash
set -e

ENV_NAME="corso_ml"

echo "=== Creazione ambiente Conda: $ENV_NAME ==="
conda create -n $ENV_NAME python=3.10 -y

# Inizializza conda nel sotto-guscio dello script
eval "$(conda shell.bash hook)"
conda activate $ENV_NAME

echo "=== Installazione pacchetti Base, Jupyter e Machine Learning ==="
conda install numpy pandas matplotlib seaborn scikit-learn scipy jupyter notebook ipykernel nltk -y

echo "=== Installazione completata! ==="
echo "Per iniziare usa: conda activate $ENV_NAME"