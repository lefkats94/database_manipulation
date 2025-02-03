import os
import psycopg2

class ConnectionManager:
    def __init__(self):
        """
        Initialize connection parameters.
        """
        self.db_name = os.getenv('DBNAME')
        self.user = os.getenv('USER')
        self.password = os.getenv('PASSWORD')
        self.host = os.getenv('HOST')
        self.port = os.getenv('PORT')

        # Set connection and cursor as None initially
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Establish connection to the PostgreSQL database.
        """
        self.connection = psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cursor = self.connection.cursor()

    def close_db(self):
        """
        Close the database connection and cursor.
        """
        self.cursor.close()
        self.connection.close()