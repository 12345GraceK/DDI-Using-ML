# Drug-Drug Interaction (DDI) Multi-Model Benchmark
This repository contains a comprehensive benchmarking framework evaluating 12 different machine learning models for predicting drug-drug interactions (DDIs). After rigorous evaluation, an optimized binary classification Logistic Regression pipeline with Target Encoding was selected as the production model due to its optimal balance between inference speed, interpretability, and predictive performance.
## Datasets
You can find all the datasets in the [Data Folder](https://github.com/12345GraceK/DDI-Using-ML/tree/main/Junior%20Final/Data).
### Initial Dataset
[DDinter](https://ddinter.scbdd.com/)'s various drugs dataset was used in this project. 
You can find it in the data folder [here](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Data/ddinter_downloads_code_V.csv).
### Data Cleaning and Preparation
You can find the data cleaning and preparation in [this notebook](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/preparing%20full%20DDinter%20Dataset.ipynb).
During the data preparation, we used negative sampling, then verified the negative samples using mghobashy's [Drug-Drug Interaction dataset on Kaggle](https://www.kaggle.com/datasets/mghobashy/drug-drug-interactions). You can find it in the data folder [here](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Data/db_drug_interactions.csv).
### Final Dataset used for Training and Testing models.
You can find the final dataset [here](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Data/DDinter_with_negatives.csv).
This dataset was split into 80% training and 20% testing.
## Classification Tasks
Both binary Classification and multi-class classification were tested for all models.
## Pipeline
Target Encoding -> StandardScaler -> Model
## Models
You can find all the model training, testing, and results in the [notebooks folder](https://github.com/12345GraceK/DDI-Using-ML/tree/main/Junior%20Final/Notebooks).
### Binary Classification
[Logistic Regression](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_LogisticRegression_Binary.ipynb),
[SVM](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_SVM_Binary.ipynb),
[Random Forest](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_RandomForest_Binary.ipynb), 
[Decision Tree](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_DecisionTree_Binary.ipynb), 
[XGBoost](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_XGBoost_Binary.ipynb), 
[CatBoost](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_CatBoost_Binary.ipynb).
### Multi-class Classification
[Logistic Regression](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_LogisticRegression_Multi.ipynb),
[SVM](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_SVM_Multi.ipynb),
[Random Forest](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_RandomForest_Multi.ipynb), 
[Decision Tree](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_DecisionTree_Multi.ipynb), 
[XGBoost](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_XGBoost_Multi.ipynb), 
[CatBoost](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_CatBoost_Multi.ipynb).
## Final Selection
All the models were tested with real-world-like noisy drug pairs their results were evaluated, and Binary classification logistic regression was chosen as the best. You can see  the full selection process [here](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/Real_World_Like_testing.ipynb).
### Production Model Performance (Logistic Regression)
**Overall Accuracy:** 90.23% <br/>
**Precision:** 98.89% <br/>
**Recall:** 91.43% <br/>
**F1-Score:** 90.70% <br/>
**Inference Time:** 0.008006s
### Using Binary Classification Logistic Regression Model
You can find the saved model .pkl file [here](https://github.com/12345GraceK/DDI-Using-ML/tree/main/Junior%20Final/Saved_Models).
You can find the prediction function [here](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/predict.py).
## Installation & Setup

Run the following commands in your terminal or prompt to set up the project environment and launch the Jupyter workspace.  <br/>
**Clone the repository and navigate into the project directory**

```
git clone https://github.com
cd Junior-Final
```

**Setup an isolated environment (Choose ONLY ONE option based on your preference)** <br/>
Option A: For Anaconda Users
```
conda create --name ddi-env python=3.12 -y && conda activate ddi-env
```
Option B: For Standard Python Users (Terminal/CLI scripts)
```
python3.12 -m venv venv && source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
Option C: For Non-Anaconda Users running Jupyter Notebook
```
python3.12 -m venv venv && source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install ipykernel
python -m ipykernel install --user --name=ddi-env --display-name "Python 3.12 (ddi-env)"
```
Install the required packages
```
pip install -r requirements.txt
```
Install Jupyter and launch the workspace
```
pip install jupyter notebook
jupyter notebook
```

*Note: If you followed Option A or C, ensure your notebook kernel is switched to `Python 3.12 (ddi-env)` from the top menu (`Kernel` -> `Change kernel`) once Jupyter opens to prevent dependency conflicts.*

## Contributing to this project
Read this if you are interested in contributing to this project:

### Experiments
While the pipeline achieves strong baseline statistics (~90% F1-score), there's still some experiments to do. <br/>
1. The DDinter dataset contains a class called (Unknown) it contains drugs that researchers don't know wethere they interact with each other or not or what's the level of interacion. In this pipline this class was kept. we can try to delete this class and rely on the negative sampling.
2. Skip the negative sampling so that the multi-class clalssification target is (major, moderate, minor and Unknown) without the no interaction class as unknown can be considered equivelant to no interaction (no known interactions), and binary classification target is (interaction, Unknown)
3. Use different more comprehensive datasets.
4. Use the full DDinter dataset by concatinating the different subsets.
5. Use SMOTE for the class imbalance.

### Issues
1. The current pipline doesn't acknowledge that (drug a, drug b) = (drug b, drug a).
