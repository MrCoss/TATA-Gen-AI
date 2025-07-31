# TATA GenAI – Delinquency Prediction EDA

[![License: Educational Use Only](https://img.shields.io/badge/License-Educational%20Use-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Built with pandas](https://img.shields.io/badge/Built%20with-pandas-purple?logo=pandas)](https://pandas.pydata.org/)
[![Built with seaborn](https://img.shields.io/badge/Built%20with-seaborn-c92f7a?logo=seaborn)](https://seaborn.pydata.org/)

---

## 📖 Table of Contents

- [1. Project Overview](#1-project-overview)
- [2. Dataset Description](#2-dataset-description)
- [3. Project Structure](#3-project-structure)
- [4. Exploratory Data Analysis (EDA) Methodology](#4-exploratory-data-analysis-eda-methodology)
- [5. Key Findings & Insights](#5-key-findings--insights)
- [6. Technical Stack](#6-technical-stack)
- [7. Setup and Installation Guide](#7-setup-and-installation-guide)
- [8. Future Work & Development Roadmap](#8-future-work--development-roadmap)
- [9. Author](#9-author)
- [10. License](#10-license)

---

## 1. Project Overview

### Business Problem
Loan delinquency represents a significant financial risk to lending institutions. Proactively identifying customers who are likely to default on their loan payments allows the institution to take preventative measures, such as offering financial counseling, restructuring loans, or adjusting credit limits. This reduces financial losses and improves portfolio health.

### Project Objective
This project, part of the **TATA GenAI Simulation**, focuses on performing a comprehensive **Exploratory Data Analysis (EDA)** on a loan dataset. The primary goal is to deeply understand the data's underlying patterns, identify key features correlated with delinquency, and uncover insights that will inform the development of a predictive machine learning model. This EDA serves as the critical first step in building a reliable delinquency prediction system.

---

## 2. Dataset Description

The analysis is performed on the `Delinquency_prediction_dataset.xlsx` file. This dataset contains anonymized customer and loan information.

- **Source:** Provided as part of the TATA GenAI Simulation.
- **Content:** The dataset includes a variety of feature types:
    - **Customer Demographics:** Information about the borrower (e.g., age, location).
    - **Loan Characteristics:** Details about the loan itself (e.g., amount, term, interest rate).
    - **Credit History:** Past financial behavior of the customer.
- **Target Variable:** A binary column, likely named `'target'` or `'delinquent'`, indicating whether a customer has defaulted (1) or not (0).

---

## 3. Project Structure

The repository is organized as follows to ensure clarity and reproducibility:

```

.
├── data/
│   ├── Delinquency\_prediction\_dataset.xlsx  \# The raw dataset for analysis.
│   └── [supporting reference documents]      \# Any supporting docs or data dictionaries.
│
├── eda\_report.py                            \# The main Python script to run the EDA.
├── requirements.txt                         \# A list of all Python dependencies for the project.
├── .gitignore                               \# Specifies files for Git to ignore.
└── README.md                                \# This detailed project documentation.

````

---

## 4. Exploratory Data Analysis (EDA) Methodology

The EDA is structured into a multi-step process to ensure a thorough investigation of the data.

###  Step 1: Data Loading and Initial Inspection
- **Action:** Load the dataset from the `.xlsx` file into a `pandas` DataFrame.
- **Inspection:** Perform an initial health check using:
    - `df.shape`: To understand the dataset's size (rows, columns).
    - `df.info()`: To review column data types and non-null counts.
    - `df.head()`: To view the first few rows and get a feel for the data.

###  Step 2: Data Cleaning and Preprocessing
- **Missing Values:** Conduct a detailed analysis of missing data using `df.isnull().sum()` and visualize the patterns with a `seaborn` heatmap. This informs the strategy for handling them (e.g., imputation, removal).
- **Duplicate Records:** Check for and remove any complete duplicate rows using `df.duplicated().sum()`.
- **Data Type Correction:** Ensure all columns have the appropriate data type (e.g., converting numerical strings to `int` or `float`, date strings to `datetime`).

###  Step 3: Univariate Analysis (Analyzing Individual Features)
- **Numerical Features:**
    - **Central Tendency & Dispersion:** Use `df.describe()` to get statistics like mean, median, standard deviation, and quartiles.
    - **Distribution:** Plot histograms and Kernel Density Estimates (KDEs) to visualize the distribution shapes (e.g., normal, skewed).
    - **Outliers:** Use box plots to visually identify potential outliers in each numerical feature.
- **Categorical Features:**
    - **Frequency Distribution:** Use `df['column'].value_counts()` and bar plots to understand the frequency of each category. This helps identify rare categories or class imbalance.

###  Step 4: Bivariate and Multivariate Analysis (Analyzing Feature Relationships)
- **Correlation Matrix:** Generate a heatmap of the correlation matrix for all numerical features. This is crucial for identifying multicollinearity (highly correlated predictors) and features strongly correlated with the target.
- **Numerical vs. Target:** Use box plots or violin plots to see how the distribution of a numerical feature (e.g., `income`) differs between delinquent and non-delinquent customers.
- **Categorical vs. Target:** Use stacked or grouped bar charts to compare the delinquency rate across different categories of a feature (e.g., `loan_purpose`).

###  Step 5: Target Variable Analysis
- **Class Distribution:** Analyze the distribution of the target variable using `value_counts()` and a pie or bar chart.
- **Imbalance Assessment:** Determine if there is a significant class imbalance (i.e., far fewer delinquent cases than non-delinquent). This has major implications for model training and evaluation metric selection.

---

## 5. Key Findings & Insights
*(This section would be populated after running the analysis. Below are hypothetical examples.)*

- **Data Quality:** The dataset contains approximately 5% missing values in the `credit_score` column, which will require imputation (e.g., mean or median).
- **Correlations:** `loan_amount` and `annual_income` show a moderate positive correlation with the likelihood of delinquency.
- **Distributions:** The `age` feature is right-skewed, suggesting that a log transformation may be beneficial for linear models.
- **Class Imbalance:** The target variable is highly imbalanced, with only 8% of the loans marked as delinquent. This necessitates the use of techniques like SMOTE or class weights during modeling and evaluation metrics like F1-score or ROC-AUC.

---

## 6. Technical Stack

- **Python 3.9+:** The core programming language for the analysis.
- **pandas:** Used for data manipulation, loading, and cleaning. The primary tool for working with tabular data.
- **seaborn & matplotlib:** Used for advanced statistical data visualization to create insightful plots like heatmaps, histograms, and box plots.
- **openpyxl:** Required by `pandas` to read and write Excel `.xlsx` files.
- **Jupyter Notebook (Optional):** Ideal for iterative exploration and documenting the analysis process step-by-step.

---

## 7. Setup and Installation Guide

To replicate this analysis, please follow these steps:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/MrCoss/your-repository-name.git](https://github.com/MrCoss/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create a Virtual Environment**
    It is highly recommended to use a virtual environment to manage dependencies.
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Required Packages**
    All dependencies are listed in the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the EDA Script**
    Make sure the path to the dataset in `eda_report.py` is correct:
    ```python
    # Inside eda_report.py
    df = pd.read_excel('data/Delinquency_prediction_dataset.xlsx')
    ```
    Then, execute the script from the terminal:
    ```bash
    python eda_report.py
    ```

---

## 8. Future Work & Development Roadmap

This EDA provides the foundation for the following development stages:

- **Advanced Feature Engineering:**
    - Create interaction terms (e.g., `loan_to_income_ratio`).
    - Apply transformations (log, Box-Cox) to normalize skewed numerical features.
    - Bin numerical features into categorical ones (e.g., `age_group`).
    - Use one-hot encoding for nominal categorical features and label encoding for ordinal ones.

- **Model Development & Training:**
    - **Baseline Model:** Establish a simple baseline using Logistic Regression.
    - **Advanced Models:** Train and tune more complex models like Random Forest, Gradient Boosting (XGBoost, LightGBM), and Support Vector Machines (SVM).
    - **Imbalance Handling:** Implement strategies like SMOTE (Synthetic Minority Over-sampling Technique) or use `class_weight` parameters in models.

- **Model Evaluation:**
    - Use k-fold cross-validation for robust performance estimation.
    - Evaluate models based on appropriate metrics for imbalanced data, such as **Precision, Recall, F1-Score, and ROC-AUC**, in addition to accuracy.
    - Analyze the **Confusion Matrix** for a detailed view of prediction errors.

- **Model Explainability & Interpretation:**
    - Employ techniques like **SHAP (SHapley Additive exPlanations)** or **LIME** to explain individual predictions and understand global feature importance.

- **Deployment Pipeline:**
    - Build a preprocessing pipeline to automate all data cleaning and feature engineering steps for new data.
    - Containerize the final model and pipeline using **Docker**.
    - Deploy the container as a REST API using a web framework like **Flask** or **FastAPI** for real-time predictions.

---

## 9. Author

- **Name:** Costas Pinto
- **GitHub:** [MrCoss](https://github.com/MrCoss)

---

## 10. License

**Type:** Educational Use Only

This project is part of a job simulation and is intended for educational and portfolio purposes only. No commercial use or redistribution is permitted without explicit permission from the author.
````
