import mysql.connector
from mysql.connector import Error
import os
import time

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        """Singleton pattern to ensure a single database connection instance."""
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance

    def _initialize_connection(self):
        """Initialize the database connection with retry logic."""
        self.connection = None
        retries = 5  # Maximum retry attempts
        delay = 5  # Delay between retries in seconds
        for attempt in range(retries):
            try:
                self.connection = mysql.connector.connect(
                    host=os.getenv('DB_HOST', 'localhost'),  
                    port=int(os.getenv('DB_PORT', 3307)),    # Ensure the port is an integer
                    user=os.getenv('DB_USER', 'root'),
                    password=os.getenv('DB_PASSWORD', 'Fall2024'),
                    database=os.getenv('DB_NAME', 'movie_app')
                )
                if self.connection.is_connected():
                    print(f"Connected to database: {os.getenv('DB_NAME', 'movie_app')}")
                    break
            except Error as e:
                print(f"Connection attempt {attempt + 1}/{retries} failed: {e}")
                if attempt < retries - 1:
                    time.sleep(delay)
                else:
                    print("Max retries reached. Could not connect to database.")
                    raise Exception("Failed to connect to the database after multiple attempts.")

    def get_connection(self):
        """Returns the active database connection. Reconnects if needed."""
        if not self.connection or not self.connection.is_connected():
            self._initialize_connection()
        return self.connection

    def execute_query(self, query, params=None):
        """Executes a query and commits if needed."""
        try:
            connection = self.get_connection()
            cursor = connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            # Commit changes for INSERT, UPDATE, DELETE queries
            if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
                connection.commit()
                print("Query committed.")
            return cursor
        except Error as e:
            print(f"Error executing query: {e}")
            if self.connection:
                self.connection.rollback()
            return None

    def fetch_all(self, query, params=None):
        """Fetches all results from a query."""
        cursor = self.execute_query(query, params)
        if cursor:
            return cursor.fetchall()
        return None

    def fetch_one(self, query, params=None):
        """Fetches a single result from a query."""
        cursor = self.execute_query(query, params)
        if cursor:
            return cursor.fetchone()
        return None

    def close_connection(self):
        """Closes the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed.")

    def __del__(self):
        """Ensures the connection is closed when the object is destroyed."""
        self.close_connection()
