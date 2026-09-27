# Logistic Regression - ExcelR Resubmission

Files:
- Logistic_Regression.ipynb - complete analysis notebook
- Diabetes.csv - dataset used for training
- logistic_regression_model.pkl - trained Logistic Regression model
- app.py - Streamlit deployment script
- requirements.txt - required Python packages

Model training follows the notebook approach:
train_test_split(test_size=0.2, random_state=42) and
LogisticRegression(max_iter=1000).

Test-set accuracy with this dataset: 0.7467532467532467

Run Streamlit:
streamlit run app.py
