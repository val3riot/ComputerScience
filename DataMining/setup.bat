@echo off
SET ENV_NAME=corso_ml

echo === Creazione ambiente Conda: %ENV_NAME% ===
call conda create -n %ENV_NAME% python=3.10 -y

echo === Attivazione ambiente ===
call conda activate %ENV_NAME%

echo === Installazione pacchetti Base, Jupyter e Machine Learning ===
call conda install numpy pandas matplotlib seaborn scikit-learn scipy jupyter notebook ipykernel nltk -y

echo === Installazione completata! ===
echo Per iniziare usa: conda activate %ENV_NAME%
pause