import mysql.connector

class DBConnection:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mahek#1608",
            database="billing_db"
        )
        self.cursor = self.conn.cursor()

    def get_connection(self):
        return self.conn, self.cursor

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
