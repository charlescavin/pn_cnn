import psycopg2


class psql_wrapper:

    def __init__(self, host, db, user, passwd):

        conn_str = f"host={host} dbname={db} user={user} password={passwd}"
        print("Connection string: " + conn_str)
        try:
            self.__connection = psycopg2.connect(conn_str)

            print(f"postgresql connection established.")

        except psycopg2.Error as error:
            self.__show_error(error, "Failed to open connection.")

        try:
            self.__cursor = self.__connection.cursor()

        except psycopg2.Error as error:
            self.__show_error(error, "Failed to establish cursor.")

    def __show_error(self, e, msg):
        print(f"{msg}: {e.pgerror}")
        print(f"Error code: {e.pgcode}")

    # Execute a query
    def exec_query_commit(self, query, with_commit=True):
        try:
            self.__cursor.execute(query)

        except psycopg2.Error as error:
            self.__show_error(error, "Failed to execute error")

        if with_commit is True:
            self.commit()

    # Commit the changes
    def commit(self):
        try:
            self.__connection.commit()
        except psycopg2.Error as error:
            self.__show_error(error, "Failed to commit changes")

    # Close the psql connection
    def close_connection(self):

        try:
            self.__cursor.close()
            print("Cursor is closed")

        except psycopg2.Error as error:
            self.__show_error(error, "Failed to close cursor.")

        try:
            self.__connection.close()
            print("Connection is closed.")

        except psycopg2.Error as error:
            self.__show_error(error, "Failed to close connection.")
