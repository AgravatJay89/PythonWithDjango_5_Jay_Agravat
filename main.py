import mysql.connector
from mysql.connector import Error

def update_data_in_db(host, database, user, password, table, column, new_value, condition_column, condition_value):
    """
    Update data in a MySQL database table.

    :param host: MySQL server host.
    :param database: Database name.
    :param user: MySQL username.
    :param password: MySQL password.
    :param table: Table name.
    :param column: Column to update.
    :param new_value: New value for the column.
    :param condition_column: Column to apply the condition.
    :param condition_value: Value to match for the condition.
    """
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Prepare the SQL query
            sql_query = f"UPDATE {table} SET {column} = %s WHERE {condition_column} = %s"

            # Execute the SQL query
            cursor.execute(sql_query, (new_value, condition_value))

            # Commit the transaction
            connection.commit()

            print(f"Data updated successfully in table {table}.")
            print(f"Updated column '{column}' with value '{new_value}' where {condition_column} = {condition_value}")

    except Error as e:
        print(f"Error occurred: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Example usage
if __name__ == "__main__":
    host = "localhost"  # MySQL host
    database = "mydatabase"  # Database name
    user = "root"  # MySQL username
    password = "your_password"  # MySQL password

    table = "employees"  # Table name
    column = "salary"  # Column to update
    new_value = 75000  # New value for the column
    condition_column = "employee_id"  # Column to apply condition
    condition_value = 101  # Condition value

    update_data_in_db(host, database, user, password, table, column, new_value, condition_column, condition_value)
