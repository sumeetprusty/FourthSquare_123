## Student Grade Tracker Management System
The Student Grade Tracker Management System is created by using SQL and Python. It's a tool that helps users manage student information and track their grades. With this application, users can add, update, and remove students, as well as add grades for each student. It also provides features to calculate averages, determine student status, and display all student records.
## Prerequisites

- Python 3.x installed on the system. [Click here](https://www.python.org/downloads/)
- MySQL server installed and running. [Click here](https://dev.mysql.com/downloads/)
- Required Python packages:
  - Python 3.x
  - MySQL server
  - mysql-connector-python package
  - python-dotenv package
  - tabulate package
  

## Package Installation

Install the required packages to run this program

- MySQL Connector for Python (mysql-connector-python)

```python
pip install mysql-connector-python
```


This package allows Python programs to connect to MySQL databases and interact with them using SQL queries. It's an essential tool for working with MySQL databases from within Python applications.

- Tabulate:

```python
pip install tabulate
```
This package provides a convenient way to format tabular data in Python. It can convert lists of dictionaries or lists of lists into nicely formatted tables, which can be printed to the console or included in reports or documents.

- Dotenv:
```python
pip install python-dotenv
```
This package is a Python module that simplifies the process of loading environment variables from a .env file into your Python project. It's commonly used in development environments to manage sensitive information like API keys, database credentials, and other configuration variables without hardcoding them into your codebase.
## Features

- **Add Student** : Add a new student to the database.
- **Update Student** : Update existing student details.
- **Remove Student** : Remove a student and their grades from the database.
- **Add Grade** : Generate a report card for a student.
- **Calculate Average** : Calculate average marks for a single student or all students cumulatively.
- **Student Status** : Retrieve the topper(s) of the class, the top N students, or the list of students who have failed.
- **Display Entries** : Display all student entries including their grades, total marks, and percentages.
## Database Table Structure

### student_info Table :

 - **student_id:** *VARCHAR(50) (Primary Key)* - Unique identifier for each student.
 - **name:** *VARCHAR(255)* - Name of the student.
 - **phone_number:** *VARCHAR(15)* - Phone number of the student.
 - **maths:** *FLOAT* - Marks obtained in the Mathematics subject.
 - **english:** *FLOAT* - Marks obtained in the English subject.
 - **sst:** *FLOAT* - Marks obtained in the Social Studies subject.
 - **science:** *FLOAT* - Marks obtained in the Science subject.
 - **computer_science:** *FLOAT* - Marks obtained in the Computer Science subject.
### grade_table Table :

 - **student_id:** *VARCHAR(50) (Primary Key)* - Unique identifier for each student.
 - **name:** *VARCHAR(255)* - Name of the student.
 - **final_grade:** *VARCHAR(2)* - Final grade achieved by the student (e.g., 'A', 'B', 'C', etc.).
 - **total_marks:** *FLOAT* - Total marks obtained by the student across all subjects.
 - **percentage:** *FLOAT* - Percentage obtained by the student based on total marks and maximum possible marks.
 
These tables are used to store student information and their corresponding grades in the database. The student_id column serves as the primary key for both tables, ensuring each student's data is uniquely identified.


## Functions

- **get_database_connection()** : Establishes a connection to the MySQL database.
- **menu()** : Displays the main menu.
- **add_student()** : Adds a new student to the database.
- **student_update()**: Updates existing student details.
- **remove_student()** : Removes a student from the database.
- **calculate_grade()** : Determines the grade based on the given mark.
- **add_grade()** : Generates a report card for a student.
- **calculate_average()** : Calculates the average marks for a single student or all students.
- **get_student_status()** : Retrieves the status of students (topper, top N students, failed students).
- **display_entries()**: Displays all student entries from the database.
- **main()**: Main function to run the application.
## Usage

1 : Run the program using Python:
```python
python setup.py
```

```python
python main.py
```
2 : Follow the on-screen menu to perform various operations.
## Files

 - **main.py:** Contains the main application logic.
 - **setup.py:** Contains the setup script to create necessary database tables. 
## Acknowledgements

 - [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [tabulate](https://pypi.org/project/tabulate/)

