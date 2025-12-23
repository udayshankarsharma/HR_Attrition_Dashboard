HR Attrition Analysis Dashboard (Power BI)

Project Overview

The objective of this project is to analyze and understand the factors contributing to Employee Attrition (turnover) within an organization. This Power BI dashboard enables HR teams to identify high-risk employees and develop data-driven retention strategies to reduce turnover costs.

Data Modeling (Star Schema)

To optimize performance and maintainability, the flat dataset was transformed into a Star Schema architecture:

Fact Table: Fact_Attrition (Contains quantitative metrics such as Attrition status, Monthly Income, and Distance from Home).

Dimension Tables:

Dim_Employee: Personal demographics (Age, Gender, Marital Status).

Dim_JobDetails: Professional information (Department, Job Role, Business Travel).

Dim_Satisfaction: Qualitative ratings (Job Satisfaction, Environment Satisfaction, Work-Life Balance).

Dim_Tenure: Experience metrics (Years at Company, Years in Current Role, Promotion Lag).

Dim_Compensation: Financial data (Salary Hike %, Stock Options, Overtime status).

Key Measures (DAX)

Several custom measures were created to drive the dashboard's analytical capabilities:

Total Employees: COUNT(Fact_Attrition[EmployeeNumber])

Attrition Rate %: DIVIDE([Attrition Count], [Total Employees], 0)

Overall Satisfaction Score: A composite average of Environment, Job, Relationship, and Work-Life ratings.

High-Risk Employees: A count of staff working Overtime with a Job Satisfaction score ≤ 2.

Dashboard Features

The dashboard is organized into three strategic layers:

1. Executive Summary (KPIs)

High-level cards displaying Total Headcount, Attrition Rate, Average Salary, and Average Tenure.

2. Demographic Analysis

Attrition by Department: Comparative analysis of turnover between Sales, R&D, and HR.

Attrition by Age Group: Binned age analysis to identify life-stage trends.

Attrition by Job Role: Granular view of specific roles with high instability.

3. Root Cause Analysis (The "Why")

Overtime Impact: Visualizing the correlation between workload (Overtime) and the decision to leave.

Career Stagnation: Analyzing the relationship between the years since the last promotion and attrition.

Income vs. Satisfaction: A scatter plot identifying roles that are undercompensated relative to employee satisfaction.

Implementation Steps

Data Ingestion: Loaded the HR_Attrition_Cleaned.csv into Power BI Desktop.

Data Transformation: Performed cleaning in Power Query, including creating age bins and numeric attrition flags.

Data Modeling: Established 1:1 and 1:Many relationships in the Model View.

DAX Development: Created the Measures table to house all calculation logic.

Visualization: Designed the UI/UX with focus on cross-filtering and interactive slicers.

Key Insights & Recommendations

Departmental Risk: The Sales Department exhibits the highest attrition, specifically among Sales Executives.

Burnout: Employees working Overtime are twice as likely to leave the company.

Growth Issues: Turnover peaks when employees stay in the same role for more than 2 years without a promotion.
