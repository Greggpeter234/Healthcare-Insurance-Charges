# Healthcare Insurance ETL & Data Visualization Project

## Overview

This project is my first individually assigned bootcamp project, where I perform an **ETL (Extract, Transform, Load) workflow** and create basic data visualizations using Python and associated libraries such as pandas for creating codes, markdown for comments and matplotlib, seaborn for basic visualisations and plotly was used to create a basic visualisation that is interactive. The dataset used is a CSV file containing healthcare insurance data.

## Objectives

- **Extract** data from a CSV file
- **Transform** the data using cleaning and preprocessing techniques
- **Load** the data into a pandas DataFrame for analysis
- Perform **exploratory data analysis (EDA)**
- Create visualizations using **matplotlib**, **seaborn** and **plotly**

## Technologies Used

- Python 3.12.8
- pandas
- matplotlib
- seaborn
- plotly
- NumPy
- Jupyter Notebook
- Git & GitHub
- vs code

## Key Findings
- Smokers are charged significantly higher
- BMI and age positively correlate with increased insurance charges
- Regional geographic differences are evident in pricing but not as significant as other personal features such as age, smoking habits and BMI.


## Project Structure

3. Open `Healthcare_insurance.ipynb` in Jupyter Notebook in VS Code IDE.
4. Run the notebook cells to follow the ETL workflow and view the visualizations.

## Key Steps

1. **Extract:** Load the CSV data using pandas.
2. **Transform:** Clean missing values, check data types, and preprocess as needed.
3. **Load:** Store the cleaned data in a DataFrame.
4. **Visualize:** Generate plots to explore relationships and trends in the data.

## Agile Methodothology
This is a collaborative and sustainable way of managing projects by breaking the work into small, manageable tasks, delivering results step by step, and improving tasks based on regular feedbacks (Beck, K., et al.(2001). Manifesto for Agile Software Development. [https://agilemanifesto.org]
## User Story
As a student Data Analyst, I want to build an ETL pipeline to extract, clean, transform, and load healthcare insurance cost data (including personal features such as age, gender, BMI, family size, smoking habits, and geographic region) from Kaggle, so that I can perform analysis, create and generate reports on how personal and geographic factors influence insurance costs.

## Tasks

1. **Extract Data**  
   - Download and extract healthcare insurance data from Kaggle (CSV format) [https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance]
2. **Clean Data**  
   - Handle missing values (impute or drop as appropriate).
   - Normalize data types and ensure correct formatting of all fields.
3. **Transform Data**  
   - Apply business logic to create derived columns (e.g., BMI category).
   - Encode categorical variables for analytics.
4. **Load Data**  
   - Load the cleaned and transformed data into a Pandas DataFrame.
5. **Validate & Visualize Data**  
   - Check data quality and consistency (duplicates, nulls, ranges).
   - Perform descriptive statistics and correlation analysis.
   - Visualize insights, predictive models, and the impact of geographic regions.

## Acceptance Criteria

### 1. Data Extraction
- 1 The pipeline shall extract raw data from Kaggle in CSV format, including fields: age, gender, BMI, smoking status, family size, region, and insurance cost.
- 2 The extraction process must log missing or duplicate records and report extraction success/failure.

### 2. Data Transformation
- 1 The pipeline shall clean data by removing duplicates, handling missing values, and standardizing field formats (e.g., gender as ‘Male’/‘Female’).
- 2 All numerical fields (age, BMI, family size, insurance cost) must be validated to fall within realistic, pre-defined ranges.
- 3 Categorical variables (gender, smoking status, region) must be encoded for downstream analytics.
- 4 The pipeline shall create derived features, such as BMI category and age group.

### 3. Data Loading
- 1 The cleaned and transformed data shall be loaded into a Pandas DataFrame following a pre-defined schema.
- 2 The loading process must be IDE potent, preventing duplicate entries.
- 3 The pipeline must validate and log each load, including row counts and data checksums.

### 4. Data Quality & Integrity
- **AC4.1:** The pipeline shall include automated data quality checks (e.g., null checks, referential integrity) and alert on anomalies.
- **AC4.2:** All transformation steps must be documented and auditable.
- 
### 5. Security & Compliance
- 1 Sensitive attributes (age, region) must be handled in compliance with data privacy regulations (e.g., HIPAA, GDPR).
- 2 Access to data must be restricted and audit-logged.

### 6. Documentation & Monitoring
- 1 The ETL process shall be documented with setup, configuration, and troubleshooting instructions.
- 2 The pipeline must include monitoring and alerting for failures or significant data anomalies.

## Additional Requirements for Analysis & Reporting

- The pipeline must enable:
- Descriptive statistics (average insurance charges by age, gender, region, etc.).
- Correlation and visualisation reports between personal features and insurance cost.
- Visualization of geographic factors on insurance cost using maps.


## Visualizations
- Distribution of insurance charges
- Correlation heatmaps
- Age vs. charges scatter plots
- Categorical comparisons (e.g., smoker vs. non-smoker)
- 
## Credits
- Copilot for code correction, review and explanation
- Chatgpt for code research and context.
- Professional definition for Agile methodology. Beck, K., et al.(2001). Manifesto for Agile Software Development. [https://agilemanifesto.org]


## Acknowledgements
- First and foremost my partner who provided support and understanding through out the course of this project and undertood that i have to be left alone to work and also helped in bringing insights and suggestions for my visualisation section.
- To my instructors at code institute who have been very supportive and helpful and take their time to ensure we are all good even during times i lost confidence in myself. Most especially to Emma who is very patient with all of us.
- Lastly to the Almighty

---

*Created as part of my Data Analytics bootcamp journey!*
