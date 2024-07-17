#2.1 - #2.2
import mysql.connector
from mysql.connector import Error

def prompt_for_input(prompt, validation_func):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print("Invalid input. Please try again.")

def is_valid_zip(zip_code):
    return zip_code.isdigit() and len(zip_code) == 5

def is_valid_month(month):
    return month.isdigit() and 1 <= int(month) <= 12

def is_valid_year(year):
    return year.isdigit() and len(year) == 4

def fetch_transactions(zip_code, month, year):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password',
            port='3306',
            database='creditcard_capstone'  # Replace with your actual database name
        )
        if conn.is_connected():
            cursor = conn.cursor()
            query = """
            SELECT * FROM cdw_sapp_credit_card
            WHERE branch_code = %s AND month = %s AND year = %s
            ORDER BY day DESC
            """
            cursor.execute(query, (zip_code, month, year))
            transactions = cursor.fetchall()
            cursor.close()
            conn.close()
            return transactions
    except Error as e:
        print(f"Error: {e}")
        return []

def main_transaction_details():
    zip_code = prompt_for_input("Enter a 5-digit zip code: ", is_valid_zip)
    month = prompt_for_input("Enter the month (1-12): ", is_valid_month)
    year = prompt_for_input("Enter the year (4 digits): ", is_valid_year)
    transactions = fetch_transactions(zip_code, int(month), int(year))
    for transaction in transactions:
        print(transaction)

def fetch_customer_details(cust_ssn):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password',
            port='3306',
            database='creditcard_capstone'  # Replace with your actual database name
        )
        if conn.is_connected():
            cursor = conn.cursor()
            query = """
            SELECT * FROM customer_table
            WHERE cust_ssn = %s
            """
            cursor.execute(query, (cust_ssn,))
            details = cursor.fetchone()
            cursor.close()
            conn.close()
            return details
    except Error as e:
        print(f"Error: {e}")
        return None

def update_customer_details(cust_ssn, new_details):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password',
            port='3306',
            database='creditcard_capstone'  # Replace with your actual database name
        )
        if conn.is_connected():
            cursor = conn.cursor()
            query = """
            UPDATE customer_table
            SET name = %s, address = %s, phone = %s
            WHERE cust_ssn = %s
            """
            cursor.execute(query, (*new_details, cust_ssn))
            conn.commit()
            cursor.close()
            conn.close()
    except Error as e:
        print(f"Error: {e}")

def generate_monthly_bill(credit_card_no, month, year):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password',
            port='3306',
            database='creditcard_capstone'  # Replace with your actual database name
        )
        if conn.is_connected():
            cursor = conn.cursor()
            query = """
            SELECT SUM(transaction_value) FROM cdw_sapp_credit_card
            WHERE credit_card_no = %s AND month = %s AND year = %s
            """
            cursor.execute(query, (credit_card_no, month, year))
            bill = cursor.fetchone()[0]
            cursor.close()
            conn.close()
            return bill
    except Error as e:
        print(f"Error: {e}")
        return None

def fetch_transactions_between_dates(cust_ssn, start_date, end_date):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password',
            port='3306',
            database='creditcard_capstone'  # Replace with your actual database name
        )
        if conn.is_connected():
            cursor = conn.cursor()
            query = """
            SELECT * FROM cdw_sapp_credit_card
            WHERE cust_ssn = %s AND DATE(CONCAT(year, '-', month, '-', day)) BETWEEN %s AND %s
            ORDER BY DATE(CONCAT(year, '-', month, '-', day)) DESC
            """
            cursor.execute(query, (cust_ssn, start_date, end_date))
            transactions = cursor.fetchall()
            cursor.close()
            conn.close()
            return transactions
    except Error as e:
        print(f"Error: {e}")
        return []

def main_customer_details():
    # Implement your CLI interaction here for customer details
    pass

if __name__ == "__main__":
    main_transaction_details()
    main_customer_details()