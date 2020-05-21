import mysql.connector
import csv
# from variables import get_vals_path


# Open a connection and create a cursor
def get_connection_and_cursor():
    # Get sign-in info
    with open('../db_vals.csv', 'r') as csvfile:
        path_reader = csv.reader(csvfile, delimiter=',')
        vars = next(path_reader)

    ap = 'mysql_native_password'

    print(f"host={vars[0]}")
    print(f"db={vars[1]}")
    print(f"user={vars[2]}")
    print(f"pw={vars[3]}")

    try:
        connection = mysql.connector.connect(host=vars[0],
                                             database=vars[1],
                                             user=vars[2],
                                             password=vars[3],
                                             auth_plugin=ap)

        print(f"MySQL connection established")

    except mysql.connector.Error as error:
        print(f"Failed to open connection: {error}")
        return None

    try:
        cursor = connection.cursor()
        return connection, cursor

    except mysql.connector.Error as error:
        print(f"Failed to create cursor: {error}")


# Close the mysql connection
def close_connection(connection):

    if (connection.is_connected()):
        connection.close()
        print("Database connection is closed")
