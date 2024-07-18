#This query plots the top 10 number of customers per State
SELECT cust_state AS State, COUNT(*) AS 'Number of Customers'
FROM cdw_sapp_customer
GROUP BY cust_state
ORDER BY 'Number of Customers' DESC
LIMIT 10;

#This query is used to plot but it shows the customer by their social security number, correct query below
SELECT CUST_SSN, 
       SUM(TRANSACTION_VALUE) AS total
FROM CDW_SAPP_CREDIT_CARD
GROUP BY CUST_SSN
ORDER BY total DESC
LIMIT 10;
#Correct query displaying the highest transcation value by customer names
SELECT 
    c.SSN,
    CONCAT(c.FIRST_NAME, ' ', c.LAST_NAME) AS CUSTOMER_NAME,
    SUM(cc.TRANSACTION_VALUE) AS TOTAL
FROM 
    CDW_SAPP_CREDIT_CARD AS cc
JOIN 
    CDW_SAPP_CUSTOMER AS c
ON 
    cc.CUST_SSN = c.SSN
GROUP BY 
    c.SSN, CUSTOMER_NAME
ORDER BY 
    TOTAL DESC
LIMIT 10;

describe cdw_sapp_loan_application;

describe cdw_sapp_credit_card;

#Here I am displaying the last 3 months with the highest transcation count 
SELECT year, month, COUNT(transaction_id) as transaction_count
FROM CDW_SAPP_CREDIT_CARD
GROUP BY year, month
ORDER BY transaction_count DESC
LIMIT 3;

#This query shows the healthcare branch code with the highest total value per branch 
SELECT branch_code, SUM(transaction_value) as total_value
FROM CDW_SAPP_CREDIT_CARD
WHERE transaction_type = 'Healthcare'
GROUP BY branch_code
ORDER BY total_value DESC
LIMIT 5;

#Alter tables because mysql database was not conencting to python and i had an failed error traceback 
ALTER TABLE cdw_sapp_loan_application 
CHANGE Self_Employed Employment_status VARCHAR(255);

describe app_status;

describe cdw_sapp_customer;
describe CDW_SAPP_LOAN_APPLICATION;
describe cdw_sapp_credit_card;


SELECT t.*
    FROM cdw_sapp_credit_card t
    JOIN cdw_sapp_customer c ON t.cust_ssn = c.ssn
    WHERE c.cust_zip = '?'
    AND t.month = '?'
    AND t.year = '?'
    ORDER BY t.day DESC

# Here we are counting the total number of applications from self-employed applicants
SELECT Employment_status, COUNT(*)
FROM cdw_sapp_loan_application
where App_status = 'Y'
GROUP BY Employment_status;

#Counting what is the typd of transcation that is happening based on credit card
SELECT TRANSACTION_TYPE, 
    COUNT(*) AS count
    FROM CDW_SAPP_CREDIT_CARD
    GROUP BY TRANSACTION_TYPE
    ORDER BY count DESC;
    

describe cdw_sapp_branch


#2.2
SELECT * FROM cdw_sapp_credit_card
WHERE branch_code IN (SELECT branch_code FROM cdw_sapp_branch WHERE branch_zip='?')
ORDER BY year DESC, month DESC, day DESC;

describe cdw_sapp_credit_card;

SELECT * FROM cdw_sapp_credit_card
    WHERE branch_code = '?' AND month = '?' AND year = '?'
    ORDER BY day DESC;

SELECT cust_zip
FROM cdw_sapp_customer;

SELECT first_name, cust_zip
FROM cdw_sapp_customer;

SELECT *
FROM cdw_sapp_customer
WHERE cust_ssn = '%s';

SHOW TABLES IN creditcard_capstone;

SELECT *
FROM cdw_sapp_customer
WHERE ssn = '%s'
LIMIT 0, 1000;

SELECT * FROM cdw_sapp_credit_card
WHERE branch_code = '%s' AND month = '%s' AND year = '%s'
ORDER BY day DESC;
#with values (94580, 4, 2018);

SELECT * FROM cdw_sapp_credit_card;
SELECT * FROM cdw_sapp_customer;

SELECT * 
FROM cdw_sapp_credit_card
WHERE branch_code = '%s' AND month = '%s' AND year = '%s'
ORDER BY day DESC;

SELECT * FROM cdw_sapp_credit_card
WHERE ssn = '%s' AND DATE(CONCAT(year, '-', month, '-', day)) BETWEEN '%s' AND '%s'
ORDER BY DATE(CONCAT(year, '-', month, '-', day)) DESC;


SELECT cust_state AS State, COUNT(*) AS 'Number of Customers'
    FROM cdw_sapp_customer
    GROUP BY cust_state
    ORDER BY COUNT(*) DESC
    LIMIT 10;