import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# 1. Read RAW data
df = pd.read_csv(os.path.join(BASE_DIR, "data", "raw_hr_data.csv"))


# 2. Column names clean
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 3. Attrition Yes/No → 1/0
df['attrition_flag'] = df['attrition'].map({'Yes': 1, 'No': 0})

# 4. Tenure
df['tenure_years'] = df['yearsatcompany']

# 5. Select required columns
final_df = df[
    [
        'employeenumber',
        'age',
        'gender',
        'maritalstatus',
        'education',
        'department',
        'jobrole',
        'joblevel',
        'monthlyincome',
        'percentsalaryhike',
        'jobsatisfaction',
        'environmentsatisfaction',
        'worklifebalance',
        'tenure_years',
        'yearsincurrentrole',
        'yearssincelastpromotion',
        'overtime',
        'attrition_flag'
    ]
]

# 6. Save CLEAN data
final_df.to_csv(os.path.join(BASE_DIR, "data", "hr_cleaned.csv"), index=False)


print("STEP 1 DONE: CLEAN DATA READY")
