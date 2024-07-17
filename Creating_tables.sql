
CREATE TABLE IF NOT EXISTS CDW_SAPP_BRANCH (
            branch_code INT PRIMARY KEY,
            branch_name VARCHAR(255),
            branch_street VARCHAR(255),
            branch_city VARCHAR(255),
            branch_state VARCHAR(255),
            branch_zip VARCHAR(20),
            branch_phone VARCHAR(20),
            last_updated DATE
        )

CREATE TABLE IF NOT EXISTS CDW_SAPP_CREDIT_CARD (
            transaction_id INT PRIMARY KEY,
            day INT,
            month INT,
            year INT,
            credit_card_no VARCHAR(255),
            cust_ssn INT,
            branch_code INT,
            transaction_type VARCHAR(255),
            transaction_value DECIMAL(10, 2)
        )

        CREATE TABLE IF NOT EXISTS CDW_SAPP_CUSTOMER (
            ssn INT PRIMARY KEY,
            first_name VARCHAR(255),
            middle_name VARCHAR(255),
            last_name VARCHAR(255),
            credit_card_no VARCHAR(255),
            apt_no VARCHAR(10),
            street_name VARCHAR(255),
            cust_city VARCHAR(255),
            cust_state VARCHAR(255),
            cust_country VARCHAR(255),
            cust_zip VARCHAR(20),
            cust_phone VARCHAR(20),
            cust_email VARCHAR(255),
            last_updated DATETIME