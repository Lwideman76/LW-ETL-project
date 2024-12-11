import mysql.connector
from mysql.connector import Error

# Function to prompt for input and validate it using a validation function
def prompt_for_input(prompt, validation_func):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print("Invalid input. Please try again.")

# Validation function for ZIP code
def is_valid_zip(zip_code):
    return zip_code.isdigit() and len(zip_code) == 5

# Validation function for month
def is_valid_month(month):
    return month.isdigit() and 1 <= int(month) <= 12

# Validation function for year
def is_valid_year(year):
    return year.isdigit() and len(year) == 4

# Function to fetch transactions based on ZIP code, month, and year
def fetch_transactions(zip_code, month, year):
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Password',
            port='3306',
            database='creditcard_capstone'  # Replace with your actual database name
        )
        if conn.is_connected():
            cursor = conn.cursor()
            # SQL query to fetch transactions
            query = """
            SELECT cc.*, cu.*
            FROM cdw_sapp_credit_card cc
            JOIN cdw_sapp_customer cu
            ON cc.cust_ssn = cu.ssn
            WHERE cu.cust_zip = %s AND cc.month = %s AND cc.year = %s
            ORDER BY cc.day DESC
            """
            print(f"Executing query: {query} with values ({zip_code}, {month}, {year})")
            cursor.execute(query, (zip_code, month, year))
            transactions = cursor.fetchall()  # Fetch all the transactions
            cursor.close()
            conn.close()
            return transactions
    except Error as e:
        print(f"Error: {e}")
        return []

# Main function to handle transaction details
def main_transaction_details():
    zip_code = prompt_for_input("Enter a 5-digit zip code: ", is_valid_zip)
    month = prompt_for_input("Enter the month (1-12): ", is_valid_month)
    year = prompt_for_input("Enter the year (4 digits): ", is_valid_year)
    transactions = fetch_transactions(zip_code, int(month), int(year))
    if not transactions:
        print("No transactions found.")
    for transaction in transactions:
        print(transaction)

# Function to fetch customer details based on SSN
def fetch_customer_details(ssn):
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
            # SQL query to fetch customer details
            query = """
            SELECT * FROM cdw_sapp_customer
            WHERE ssn = %s
            LIMIT 0, 1000
            """
            print(f"Executing query: {query} with value ({ssn})")
            cursor.execute(query, (ssn,))
            details = cursor.fetchone()  # Fetch one customer detail
            cursor.close()
            conn.close()
            return details
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to update customer details
def update_customer_details(ssn, new_details):
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
            # SQL query to update customer details
            query = """
            UPDATE cdw_sapp_customer
            SET first_name = %s, last_name = %s, cust_phone = %s
            WHERE ssn = %s
            """
            print(f"Executing query: {query} with values ({new_details}, {ssn})")
            cursor.execute(query, (*new_details, ssn))
            conn.commit()  # Commit the transaction
            cursor.close()
            conn.close()
            print(f"Customer details updated for SSN: {ssn}")
    except Error as e:
        print(f"Error: {e}")

# Function to generate monthly bill for a credit card
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
            # SQL query to calculate the monthly bill
            query = """
            SELECT SUM(transaction_value) FROM cdw_sapp_credit_card
            WHERE credit_card_no = %s AND month = %s AND year = %s
            """
            print(f"Executing query: {query} with values ({credit_card_no}, {month}, {year})")
            cursor.execute(query, (credit_card_no, month, year))
            bill = cursor.fetchone()[0]  # Fetch the sum of transaction values
            cursor.close()
            conn.close()
            return bill
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to fetch transactions between two dates for a customer
def fetch_transactions_between_dates(ssn, start_date, end_date):
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
            # SQL query to fetch transactions between dates
            query = """
            SELECT * FROM cdw_sapp_credit_card
            WHERE cust_ssn = %s AND DATE(CONCAT(year, '-', month, '-', day)) BETWEEN %s AND %s
            ORDER BY DATE(CONCAT(year, '-', month, '-', day)) DESC
            """
            print(f"Executing query: {query} with values ({ssn}, {start_date}, {end_date})")
            cursor.execute(query, (ssn, start_date, end_date))
            transactions = cursor.fetchall()  # Fetch all transactions
            cursor.close()
            conn.close()
            return transactions
    except Error as e:
        print(f"Error: {e}")
        return []

# Main function to handle customer details
def main_customer_details():
    while True:
        print("\n1. Check Existing Account Details")
        print("\n2. Modify Existing Account Details")
        print("\n3. Generate Monthly Bill")
        print("\n4. Display Transactions Between Dates")
        print("\n5. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            ssn = input("Enter customer SSN: ")
            details = fetch_customer_details(ssn)
            if details:
                print("Customer Details:", details)
            else:
                print("No details found for the provided SSN.")
        elif choice == '2':
            ssn = input("Enter customer SSN: ")
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            phone = input("Enter new phone number: ")
            update_customer_details(ssn, (first_name, last_name, phone))
        elif choice == '3':
            credit_card_no = input("Enter credit card number: ")
            month = prompt_for_input("Enter the month (1-12): ", is_valid_month)
            year = prompt_for_input("Enter the year (4 digits): ", is_valid_year)
            bill = generate_monthly_bill(credit_card_no, int(month), int(year))
            if bill is not None:
                print(f"Monthly bill for {credit_card_no} is ${bill:.2f}.")
            else:
                print("Error generating bill.")
        elif choice == '4':
            ssn = input("Enter customer SSN: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            transactions = fetch_transactions_between_dates(ssn, start_date, end_date)
            if not transactions:
                print("No transactions found.")
            for transaction in transactions:
                print(transaction)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Main function to navigate between transaction and customer details
def main():
    while True:
        print("\n1. Transaction Details")
        print("2. Customer Details")
        print("\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            main_transaction_details()
        elif choice == '2':
            main_customer_details()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()