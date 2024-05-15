import mysql.connector as mq
import os
from mysql.connector import MySQLConnection
from dotenv import load_dotenv
from typing import Union

load_dotenv()

def get_database_connection() -> Union[mq.MySQLConnection, None]:
    """
    Establishes a connection to the MySQL database.
    Returns:
        mq.MySQLConnection: Database connection object if successful, otherwise None.
    """
    try:
        con: mq.MySQLConnection = mq.connect(
            host=os.getenv('host'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            database=os.getenv('database')
        )
        return con
    except mq.Error as e:
        print("Error connecting to the database:", e)
        return None

def main() -> None:
    """
    Main function to set up database tables.
    """
    # Connect to the database
    con: Union[mq.MySQLConnection, None] = get_database_connection()
    if con:
        cur: mq.cursor.MySQLCursor = con.cursor()

        # Create student_info table if not exists
        cur.execute('''
            CREATE TABLE IF NOT EXISTS student_info (
                student_id VARCHAR(50) PRIMARY KEY,  
                name VARCHAR(255) NOT NULL,
                phone_number VARCHAR(15),
                maths FLOAT,
                english FLOAT,
                sst FLOAT,
                science FLOAT,
                computer_science FLOAT
            )
        ''')

        # Create grade_table table if not exists
        cur.execute('''
            CREATE TABLE IF NOT EXISTS grade_table (
                student_id VARCHAR(50) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                final_grade VARCHAR(2),
                total_marks FLOAT,
                percentage FLOAT
            )
        ''')
        # Committing the changes to the database
        con.commit()

        # Closing the database connection
        con.close()

# Entry point of the script
if __name__ == "__main__":
    main()
