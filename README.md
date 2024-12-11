# Advanced ETL Techniques: Loan and Credit Card Data Analysis

# Project Overview

This project involves building an ETL (Extract, Transform, Load) process to analyze a Loan Application dataset and a Credit Card dataset. The goal of this project is to demonstrate my data engineering skills by cleaning, transforming, and visualizing data to provide actionable insights.


## Setup and Installation

### Prerequisites
- Python 3.x
- PySpark
- Jupyter Notebook
- Pandas
- Matplotlib
- Plotly.express
- Mysql.connector 

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Lwideman76/LW-Capstone-project.git
   cd LW-Capstone-project

### Data

### Loan Application Dataset
Contains information on loan applications and their statuses. Detailed steps are provided to break down the processes involved.

### Credit Card Dataset
Contains information on credit card transactions and customer profiles. Detailed steps are provided to break down the processes involved.

### Code
- `Data_Extraction.ipynb`: Notebook for cleaning and preprocessing the data.
- `Data_Transformation.ipynb`: Notebook for cleaning, preprocessing, and transforming data.
- `Data_Visualization.ipynb`: Jupyter notebook for visualizing the data.

### Database Scripts
- `Creating_tables.sql`: SQL script to create necessary database tables.
- `load_data.sql`: SQL script to load data into the database.

## Interpreting the Visualizations

- **Loan Approval Rate for Self-Employed Applicants**: The bar chart shows the approval rate of loan applications for self-employed individuals versus non-self-employed individuals, detailing how many were approved over different time periods. A higher bar indicates a higher approval rate for non-self-employed individuals.
- **Rejections for Married Male Applicants**: The line graph illustrates the number of loan application rejections for married male applicants. Peaks represent the high number of approvals for married male applicants, while the lows indicate the number of rejections.
- **Loan Applications Over the last 3 months**: This line chart displays the distribution of the number of loan applications within the last three months. Each point on the line represents the number of applications received in a specific month.
- **Branch with the highest Healthcare Transcations** This scatter plot displays which branch had the highest transaction value in the healthcare category. Each point represents a branch, with the size of the point indicating the total transaction value.


![Screenshot 2024-07-17 023531](https://github.com/user-attachments/assets/93d3cc28-6508-4070-990b-af86c950c66a)


![Screenshot 2024-07-17 023622](https://github.com/user-attachments/assets/1562737a-6c73-444b-a670-38623b9389b5)

![Screenshot 2024-07-17 023630](https://github.com/user-attachments/assets/710bbeb8-ed5b-4af2-acd1-9066ea94e477)


![Screenshot 2024-07-17 024028](https://github.com/user-attachments/assets/cfbf6e64-458f-4917-a513-4bd11ee48e93)


![Screenshot 2024-07-17 051506](https://github.com/user-attachments/assets/252f4789-6304-42ff-bfff-48876b1547f5)


![Screenshot 2024-07-17 051520](https://github.com/user-attachments/assets/b2e5c3be-0248-447c-9465-20f3ce80434d)


![Screenshot 2024-07-17 051615](https://github.com/user-attachments/assets/ede55c94-be8f-4a38-82de-e18e0f0c0b3a)
