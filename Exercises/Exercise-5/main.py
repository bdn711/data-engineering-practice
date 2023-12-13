import psycopg2


def main():
    
    def drop_table(table_list):
        """Delete each database table in table_list."""
        for table in table_list:
            cursor.execute(f'DROP TABLE IF EXISTS {table}')
    
    
    def ingest_csv_data(table_list):
        """Copy data from a csv file into a corresponding database table."""
        for table in table_list:
            with open(f'data/{table}.csv', 'r') as f:
                next(f) # Skip header row
                cursor.copy_from(f, table, sep=',')
                f.close()
        
    # Connect to database
    host = 'localhost'
    database = 'postgres'
    user = 'postgres'
    pas = 'postgres'
    conn = psycopg2.connect(host=host, database=database, user=user, password=pas)

    # Open a cursor to perform database operations
    cursor = conn.cursor()

    # Remove any pre-existing/conflicting tables
    drop_table(['transactions', 'accounts', 'products'])

    # Define create table sql command variables
    accounts = '''CREATE TABLE accounts (
        customer_id INT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        address_1 VARCHAR(255),
        address_2 VARCHAR(255),
        city VARCHAR(255),
        state VARCHAR(255),
        zip_code VARCHAR(10),
        join_date VARCHAR(255)
        );'''
    products = '''CREATE TABLE products (
        product_id INT PRIMARY KEY,
        product_code INT,
        product_description VARCHAR(255)
        );'''
    transactions = '''CREATE TABLE transactions (
        transaction_id VARCHAR(255) PRIMARY KEY,
        transaction_date VARCHAR(255),
        product_id INT,
        product_code INT,
        product_description VARCHAR(255),
        quantity INT,
        account_id INT,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (account_id) REFERENCES accounts(customer_id)
        );'''

    # Execute create table sql commands
    cursor.execute(accounts + products + transactions)

    # Ingest csv file data into tables 
    ingest_csv_data(['accounts', 'products', 'transactions'])

    # Save changes to the database
    conn.commit()
   
    # Close communication with the database
    cursor.close()
    conn.close()

    
if __name__ == "__main__":
    main()
