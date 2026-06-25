# Hypertension Risk Analysis

A data analysis project exploring how family history and stress level 
combine to affect hypertension risk, built using the Zerve AI data platform.

## Overview
This project analyzes a public health dataset to understand how genetic 
risk (family history) and lifestyle risk (stress) interact to predict 
hypertension, going beyond looking at either factor alone.

## Key Findings
- Patients with both a family history of hypertension and high stress 
  reach an 80% hypertension rate, the highest-risk subgroup in the dataset
- By comparison, patients with no family history and low stress have only 
  a 32% hypertension rate
- High stress amplifies risk substantially in both groups, increasing 
  rates by 20+ percentage points
- A logistic regression model using Family History, Age, Stress Score and 
  BMI achieved 71.3% test accuracy, with Family History as the strongest 
  individual predictor

## Dataset
Hypertension Risk Prediction Dataset (Kaggle), 1,985 records and 11 
features built around clinical and public health patterns, including 
Age, Salt Intake, Stress Score, BP History, Sleep Duration, BMI, 
Medication, Family History, Exercise Level, Smoking Status, and 
Has Hypertension as the target variable.

## Workflow
- Loaded and profiled the dataset, identifying 40% missing values in the 
  Medication column
- Cleaned missing Medication values by filling with "No Medication"
- Built a visualization comparing hypertension rates across Family History 
  and Stress Score bands
- Built a logistic regression model to predict hypertension and evaluated 
  feature importance

## Tech Stack
Python, pandas, scikit-learn, Zerve AI data platform

## Note
These are observational associations, not causal estimates. Confounding 
variables such as Age and BMI are not fully isolated in this analysis.
