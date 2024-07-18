# LW-Capstone-project

# Capstone Project: Loan Application and Credit Card Data Analysis

This project involves building an ETL process to analyze a Loan Application dataset and a Credit Card dataset. The goal of this project is to demonstrate my data engineering skills by cleaning, transforming, and visualizing data to provide actionable insights for anyone who views it


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
- Loan Application Dataset: Contains information on loan applications and their statuses. As well as well written steps given to break down the processes 
- Credit Card Dataset: Contains information on credit card transactions and customer profiles. As well as well written steps given to break down the processes 

### Code
- `Data_Extraction.ipynb`: Jupyter notebook for cleaning and preprocessing the data.
- `Data_Transformation.ipynb`: Jupyter notebook for cleaning, preprocessing and transforming data.
- `Data_Visualization.ipynb`: Jupyter notebook for visualizing the data.

### Database Scripts
- `Creating_tables.sql`: SQL script to create necessary database tables.
- `load_data.sql`: SQL script to load data into the database.

## Interpreting the Visualizations

- **Loan Approval Rate for Self-Employed Applicants**: The bar chart shows the approval rate of loan applications for self employed indivuals vs not self employed and how many were approved over different time periods. A higher bar indicates a higher approval rate for people that are not self employed.
- **Rejections for Married Male Applicants**: The line graph illustrates the spending patterns of customers over the past year. Peaks represent high represents the amount of approvals for married male applicants, while the low indicates the amount of rejection for married male applicants.
- **Loan Applications Over the last 3 months**: This line chart displays the distribution of number of application within the last 3 months. Each line point represents the most applicants that they had in the exact month.
- **Branch with the highest Healthcare Transcations** This scatter plot displays which branch had the highest transaction value.


![Screenshot 2024-07-17 023531](https://github.com/user-attachments/assets/93d3cc28-6508-4070-990b-af86c950c66a)


![Screenshot 2024-07-17 023622](https://github.com/user-attachments/assets/1562737a-6c73-444b-a670-38623b9389b5)

![Screenshot 2024-07-17 023630](https://github.com/user-attachments/assets/710bbeb8-ed5b-4af2-acd1-9066ea94e477)


![Screenshot 2024-07-17 024028](https://github.com/user-attachments/assets/cfbf6e64-458f-4917-a513-4bd11ee48e93)


![Screenshot 2024-07-17 051506](https://github.com/user-attachments/assets/252f4789-6304-42ff-bfff-48876b1547f5)


![Screenshot 2024-07-17 051520](https://github.com/user-attachments/assets/b2e5c3be-0248-447c-9465-20f3ce80434d)


![Screenshot 2024-07-17 051615](https://github.com/user-attachments/assets/ede55c94-be8f-4a38-82de-e18e0f0c0b3a)
