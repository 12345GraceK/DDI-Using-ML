# Drug-Drug Interaction (DDI) Multi-Model Benchmark
This repository contains a comprehensive benchmarking framework evaluating 12 different machine learning models for predicting drug-drug interactions (DDIs). After rigorous evaluation, an optimized binary classification Logistic Regression pipeline with Target Encoding was selected as the production model due to its optimal balance between inference speed, interpretability, and predictive performance.
# Datasets
You can find all the datasets in the [Data Folder](https://github.com/12345GraceK/DDI-Using-ML/tree/main/Junior%20Final/Data).
## Initial Dataset
[DDinter](https://ddinter.scbdd.com/)'s various drugs dataset was used in this project. 
You can find it in the data folder [here](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Data/ddinter_downloads_code_V.csv).
## Data Cleaning and Preparation
You can find the data cleaning and preparation in [this notebook](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/preparing%20full%20DDinter%20Dataset.ipynb).
During the data preparation, we used negative sampling, then verified the negative samples using mghobashy's [Drug-Drug Interaction dataset on Kaggle](https://www.kaggle.com/datasets/mghobashy/drug-drug-interactions). You can find it in the data folder [here](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Data/db_drug_interactions.csv).
## Final Dataset used for Training and Testing models.
You can find the final dataset [here](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Data/DDinter_with_negatives.csv).
This dataset was split into 80% training and 20% testing.
# Classification Tasks
Both binary Classification and multi-class classification were tested for all models.
# Pipeline
Target Encoding -> StandardScaler -> Model
# Models
You can find all the model training, testing, and results in the [notebooks folder](https://github.com/12345GraceK/DDI-Using-ML/tree/main/Junior%20Final/Notebooks).
## Binary Classification
[Logistic Regression](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_LogisticRegression_Binary.ipynb),
[SVM](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_SVM_Binary.ipynb),
[Random Forest](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_RandomForest_Binary.ipynb), 
[Decision Tree](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_DecisionTree_Binary.ipynb), 
[XGBoost](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_XGBoost_Binary.ipynb), 
[CatBoost](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_CatBoost_Binary.ipynb).
## Multi-class Classification
[Logistic Regression](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_LogisticRegression_Multi.ipynb),
[SVM](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_SVM_Multi.ipynb),
[Random Forest](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_RandomForest_Multi.ipynb), 
[Decision Tree](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_DecisionTree_Multi.ipynb), 
[XGBoost](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_XGBoost_Multi.ipynb), 
[CatBoost](https://github.com/12345GraceK/DDI-Using-ML/blob/main/Junior%20Final/Notebooks/DDinter_CatBoost_Multi.ipynb).
