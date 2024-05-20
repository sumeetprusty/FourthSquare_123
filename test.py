import mysql.connector as mq
from tabulate import tabulate
from mysql.connector import MySQLConnection
from typing import Optional
import os
from dotenv import load_dotenv
from typing import List, Tuple, Any
load_dotenv()

# Define a decorator function to manage the database connection
def database_connection(func):
    # Define the wrapper function that will add the database connection logic
    def wrapper(*args, **kwargs):
        try:
            # Establish a connection to the database using environment variables
            con: MySQLConnection = mq.connect(
                host=os.getenv('host'),        
                user=os.getenv('user'),         
                password=os.getenv('password'), 
                database=os.getenv('database')  
            )
            # Execute the wrapped function, passing the connection object along with other arguments
            result = func(con, *args, **kwargs)
            # Close the database connection after the function has executed
            con.close()
            return result
        except mq.Error as e:  # Catch any MySQL errors that occur
            print("Error connecting to the database:", e)  
            return None  # Return None if there is an error
    return wrapper  # Return the wrapper function

# Function to display the main menu
def menu():
        print("\n\t\t\t\tSTUDENT GRADE TRACKER\n\n")
        print("\t\t\t\t\tMAIN MENU\n")
        print("\t\t1. Add Student\t\t\t\t2. Update Student \n\n\t\t3. Remove Student\t\t\t4. Add grade\n\n\t\t5. Calculate Average\t\t\t6. Status\n\n\t\t7. Display\t\t\t\t8. Subject Wise Report\n\n\t\t9. Overall Statistics\t\t\t10. Exit")

# Decorator
@database_connection
def add_student(con: MySQLConnection) -> None:
    """
    Adds a new student to the student_info and grade_table tables in the database.
    """
    print("\n\t\t\t\tADD NEW STUDENT")

    # Iterator (cursor acts as an iterator over the database query results)
    cur = con.cursor() 

    # Get the student's name ensuring it does not contain any digits
    while True:
        name: str = input("Enter Student's Name: ")
        if any(char.isdigit() for char in name):
            print("Name cannot contain digits. Please enter a valid name.")
        else:
            break

    # Get a unique student ID ensuring it does not already exist in the database
    while True:
        student_id: str = input("Enter Student's ID: ")
        query: str = "SELECT * FROM student_info WHERE student_id=%s"
        cur.execute(query, (student_id,))

        # Fetch the first result from the executed query, which should correspond to the student with the given ID
        existing_student = cur.fetchone()

        if existing_student:
            print(f"Student with ID '{student_id}' already exists.")
        else:
            break

    # Get the student's phone number ensuring it is exactly 10 digits
    while True:
        phone_number: str = input("Enter Student's Phone Number: ")
        if len(phone_number) != 10 or not phone_number.isdigit():
            print("Phone number must be exactly 10 digits. Please re-enter.")
        else:
            break

    # Get the student's marks for each subject
    subjects: list[str] = ['Maths', 'English', 'SST', 'Science', 'Computer Science']
    marks: list[float] = []
    for subject in subjects:
        while True:
            try:
                mark: float = float(input(f"Enter marks for {subject} (out of 100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100. Please re-enter.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Calculate total marks and percentage
    total_marks: float = sum(marks)
    max_marks: int = len(subjects) * 100   # each subject has a maximum of 100 marks
    percentage: float = (total_marks / max_marks) * 100

    # Calculate final grade
    if percentage >= 90:
        final_grade: str = "O"
    elif percentage >= 80:
        final_grade = "A"
    elif percentage >= 70:
        final_grade = "B"
    elif percentage >= 60:
        final_grade = "C"
    elif percentage >= 50:
        final_grade = "D"
    else:
        final_grade = "Fail"

    # Insert into student_info table
    query = """
    INSERT INTO student_info(student_id, name, phone_number, maths, english, sst, science, computer_science) 
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(query, (student_id, name, phone_number, marks[0], marks[1], marks[2], marks[3], marks[4]))

    # Insert into grade_table
    query = """
    INSERT INTO grade_table(student_id, name, final_grade, total_marks, percentage) 
    VALUES(%s, %s, %s, %s, %s)
    """
    cur.execute(query, (student_id, name, final_grade, total_marks, percentage))

    # Commit the changes to the database
    con.commit()
    print("\nSuccessfully Added The Student!")

    # Close the database connection
    con.close()

# Decorator
@database_connection

def student_update(con: MySQLConnection) -> None:
    """
    Updates student details in the database based on user input.
    """
    print("\n\t\t\t\tUPDATE STUDENT DETAILS")

    # Iterator (cursor acts as an iterator over the database query results)
    cur = con.cursor()

    # Get the student ID for the student to be updated
    student_id: str = input("Enter Student's ID to update: ")

    # Query to fetch the student's current details
    query: str = "SELECT * FROM student_info WHERE student_id='{}'".format(student_id)
    cur.execute(query)
    existing_student: Optional[Tuple[Any, ...]] = cur.fetchone()

    if existing_student:

        # Display the current details of the student
        print("Student found. Current details:")
        print("Name:", existing_student[1])
        print("Phone Number:", existing_student[2])

        # Prompt the user to choose what they want to update
        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Phone Number")
        print("3. Marks for subjects")
        choice: str = input("Enter your choice (1/2/3): ")

        if choice == '1':

            # Update the student's name
            new_name: str = input("Enter new name: ")
            update_query: str = "UPDATE student_info SET name='{}' WHERE student_id='{}'".format(new_name, student_id)
            cur.execute(update_query)
            con.commit()
            print("Name updated successfully.")

        elif choice == '2':

            # Update the student's phone number
            new_phone_number: str = input("Enter new phone number: ")
            update_query: str = "UPDATE student_info SET phone_number='{}' WHERE student_id='{}'".format(new_phone_number, student_id)
            cur.execute(update_query)
            con.commit()
            print("Phone number updated successfully.")

        elif choice == '3':

            # Update the student's marks for each subject
            subjects: List[str] = ['Maths', 'English', 'SST', 'Science', 'Computer Science']
            for i, subject in enumerate(subjects, start=1):
                new_mark: float = float(input("Enter new marks for {}: ".format(subject)))
                update_query: str = "UPDATE student_info SET {}={} WHERE student_id='{}'".format(subject.lower().replace(" ", "_"), new_mark, student_id)
                cur.execute(update_query)
                con.commit()
            print("Marks updated successfully.")

        else:
            print("Invalid choice. Please enter a valid option.")

    else:

        # If the student ID does not exist in the database
        print("Student with ID '{}' not found.".format(student_id))

    # Close the database connection    
    con.close()

# Decorator
@database_connection
def remove_student(con: MySQLConnection) -> None:
    """
    Removes a student and their corresponding grades from the database.
    """
    print("\n\t\t\t\tREMOVE STUDENT")

    # Iterator (cursor acts as an iterator over the database query results)
    cur = con.cursor()

    student_id: str = input("Enter Student's ID to remove: ")
    query: str = "SELECT * FROM student_info WHERE student_id=%s"
    cur.execute(query, (student_id,))
    existing_student: tuple = cur.fetchone()

    if existing_student:
        confirm: str = input("Are you sure you want to remove student '{}'? (yes/no): ".format(existing_student[1]))
        if confirm.lower() == 'yes':
            try:
                # Delete from grade_table
                delete_grades_query: str = "DELETE FROM grade_table WHERE student_id=%s"
                cur.execute(delete_grades_query, (student_id,))
                
                # Delete from student_info
                delete_student_query: str = "DELETE FROM student_info WHERE student_id=%s"
                cur.execute(delete_student_query, (student_id,))
                
                # Commit the transaction
                con.commit()
                
                print("Student '{}' removed successfully along with their grades.".format(existing_student[1]))
            except mq.Error as e:
                # Rollback in case of error
                con.rollback()
                print("An error occurred: ", e)
        else:
            print("Removal canceled.")
    else:
        print("Student with ID '{}' not found.".format(student_id))

    con.close()

# decorator function to assign grades based on marks
def grade_decorator(func):

    # The wrapper function is defined inside the decorator to add additional functionality
    def wrapper(*args, **kwargs):
        mark = func(*args, **kwargs)

        # Determine the grade based on the mark and return it
        if mark >= 90:
            return "O"
        elif mark >= 80:
            return "A"
        elif mark >= 70:
            return "B"
        elif mark >= 60:
            return "C"
        elif mark >= 50:
            return "D"
        else:
            return "Fail"
        
    # Return the wrapper function to replace the original function   
    return wrapper

# Decorator
@grade_decorator
def calculate_grade(mark: float) -> str:
    """
    Determines the grade based on the given mark.
    """
    return mark

# Decorator
@database_connection
def add_grade(con: MySQLConnection) -> None:
    """
    Generates a report card for a student by fetching their details from the database,
    calculating their grades, and displaying the report card.
    """
    print("\n\t\t\t\tGENERATE REPORT CARD")

    # Iterator (cursor acts as an iterator over the database query results)
    cur = con.cursor()

    # Prompt the user to enter the student's ID for whom the report card needs to be generated
    student_id: str = input("Enter Student's ID to generate report card: ")

    # Query to fetch the student's details from the database
    query: str = "SELECT * FROM student_info WHERE student_id='{}'".format(student_id)
    cur.execute(query)
    student_info: Tuple[Any, ...] = cur.fetchone()

    # Check if the student information is found
    if student_info:

        # Print the header of the report card
        print("\nREPORT CARD")
        print("-------------------------------------------------------------")
        print("Name: ", student_info[1])
        print("Student ID: ", student_info[0])
        print("Phone Number: ", student_info[2])
        print("-------------------------------------------------------------")
        print("{:<20} {:<10} {:<10}".format("Subject", "Marks", "Grade"))
        print("-------------------------------------------------------------")

        subjects: List[str] = ['Maths', 'English', 'SST', 'Science', 'Computer Science']
        total_marks: float = 0

        # Iterate over each subject, calculate the grade and total marks
        for subject in subjects:
            mark: float = student_info[subjects.index(subject) + 3]  # Adjust index for marks columns
            grade: str = calculate_grade(mark)
            total_marks += mark

            # Print the marks and grade for each subject
            print("{:<20} {:<10} {:<10}".format(subject, mark, grade))

        print("-------------------------------------------------------------")
        print("Total Marks Received: ", total_marks)
        max_marks: int = len(subjects) * 100  # Each subject has a maximum of 100 marks
        print("Maximum Marks: ", max_marks)
        percentage: float = (total_marks / max_marks) * 100
        print("Final Percentage: {:.2f}%".format(percentage))
        final_grade: str = calculate_grade(percentage)
        print("Final Grade: ", final_grade)
        print("-------------------------------------------------------------")
    else:
        # If the student ID is not found in the database, display an error message
        print("Student with ID '{}' not found.".format(student_id))
    
    con.close()

# Decorator
@database_connection
def calculate_average(con: MySQLConnection) -> None:
    """
    Calculates and prints the average marks for either a single student or all students cumulatively.
    """    
    print("\n\t\t\t\tCALCULATE AVERAGE")
    # Iterator (cursor acts as an iterator over the database query results)
    cur = con.cursor()

    choice: str = input("Calculate average for (1) Single student or (2) All entries cumulatively? (Enter 1 or 2): ")

    if choice == '1':
        # If the user chooses to calculate average for a single student
        student_id: str = input("Enter Student's ID to calculate average: ")

        # Query to fetch the student's details from the database
        query: str = "SELECT * FROM student_info WHERE student_id='{}'".format(student_id)
        cur.execute(query)
        student_info: Optional[Tuple[Any, ...]] = cur.fetchone()

        # Check if the student information is found
        if student_info:
            # Calculate the total marks by summing up the marks columns
            total_marks: float = sum(student_info[3:])  

            # Calculate the number of subjects by subtracting the non-marks columns (3)
            subjects_count: int = len(student_info) - 3  

            # Calculate the average marks
            average: float = total_marks / subjects_count

            # Print the average marks for the student
            print("Average for student '{}' (ID: {}) is: {:.2f}".format(student_info[1], student_id, average))
        else:
            print("Student with ID '{}' not found.".format(student_id))

    elif choice == '2':

        # If the user chooses to calculate the cumulative average for all students
        cur.execute("SELECT * FROM student_info")
        all_students_info: List[Tuple[Any, ...]] = cur.fetchall()
        total_marks: float = 0
        total_subjects_count: int = 0

        # Iterate over all students' information
        for student_info in all_students_info:

            # Sum the total marks for all students
            total_marks += sum(student_info[3:])
            # Sum the total number of subjects for all students
            total_subjects_count += len(student_info) - 3

        if total_subjects_count > 0:
            # Calculate the cumulative average marks
            average: float = total_marks / total_subjects_count
            # Print the cumulative average marks for all students
            print("Cumulative average for all entries is: {:.2f}".format(average))
        else:
            print("No entries found in the database.")
    con.close()

# Decorator
@database_connection
def get_student_status(con: MySQLConnection) -> None:
    """
    Retrieves and displays the status of students based on the user's choice.
    """
    # Iterator (cursor acts as an iterator over the database query results)
    cur = con.cursor()
    print("\n\t\t\t\tSTUDENT STATUS")

    print("Choose an option:")
    print("1. Get the topper(s) of the class")
    print("2. Get the top N students of the class")
    print("3. Get the list of students who have failed")

    choice: str = input("Enter your choice (1/2/3): ")

    if choice == '1':
        cur.execute("SELECT * FROM student_info")
        all_students_info: list[tuple] = cur.fetchall()

        if all_students_info:
            # Calculate total marks for each student and find the maximum
            student_marks: list[tuple] = [(student[0], student[1], sum(student[3:])) for student in all_students_info]
            # Find all students with the maximum total marks (in case of ties)
            toppers: list[tuple] = [student for student in student_marks if student[2] == max(student_marks, key=lambda x: x[2])[2]]

            if len(toppers) == 1:
                # If there is a single topper, display their information
                print("The topper of the class is:")
                print("Student ID:", toppers[0][0])
                print("Name:", toppers[0][1])
                print("Total Marks:", toppers[0][2])
            else:
                # If there are multiple toppers, display their information
                print("The toppers of the class are:")
                for topper in toppers:
                    print("Student ID:", topper[0])
                    print("Name:", topper[1])
                    print("Total Marks:", topper[2])
        else:
            print("No entries found in the database.")

    elif choice == '2':
        # Option 2: Get the top N students of the class
        try:
            n: int = int(input("Enter the value of N to get top N students: "))
            if n <= 0:
                print("Please enter a positive integer value for N.")
            else:
                cur.execute("SELECT * FROM student_info")
                all_students_info: list[tuple] = cur.fetchall()

                if all_students_info:
                    # Calculate total marks for each student 
                    student_marks: list[tuple] = [(student[0], student[1], sum(student[3:])) for student in all_students_info]

                    # Sort students by total marks in descending order
                    sorted_students: list[tuple] = sorted(student_marks, key=lambda x: x[2], reverse=True)

                    print("Top {} students of the class are:".format(n))

                    # Display information for the top N students
                    for i in range(min(n, len(sorted_students))):
                        print("Student ID:", sorted_students[i][0])
                        print("Name:", sorted_students[i][1])
                        print("Total Marks:", sorted_students[i][2])
                else:
                    print("No entries found in the database.")
        except ValueError:
            print("Invalid input. Please enter a valid integer value for N.")

    elif choice == '3':
        # Option 3: Get the list of students who have failed
        cur.execute("SELECT * FROM student_info")
        all_students_info: list[tuple] = cur.fetchall()

        if all_students_info:
            # Filter students who have failed (at least one mark less than 50)
            failed_students: list[tuple] = [(student[0], student[1], sum(student[3:])) for student in all_students_info if any(mark < 50 for mark in student[3:])]

            if failed_students:
                print("The following students have failed:")
                for student in failed_students:
                    print("Student ID:", student[0])
                    print("Name:", student[1])
                    print("Total Marks:", student[2])
            else:
                print("No students have failed.")
        else:
            print("No entries found in the database.")
        con.close()

# Decorator
@database_connection
def display_entries(con: MySQLConnection) -> None:
    """
    Retrieves and displays all student entries from the database, including their grades, total marks, and percentage.
    """
    # Iterator (cursor acts as an iterator over the database query results)
    cur = con.cursor()

    # query to select student information and their corresponding grades from the database by using LEFT JOIN
    query: str = '''
        SELECT si.student_id, si.name AS student_name, si.phone_number, si.maths, si.english, si.sst, si.science, si.computer_science,
               gt.final_grade, gt.total_marks, gt.percentage
        FROM student_info si
        LEFT JOIN grade_table gt ON si.student_id = gt.student_id
    '''
    cur.execute(query)

    # Fetch all results from the executed query
    entries: List[Tuple] = cur.fetchall()

    if entries:
        # Define headers for the table display
        headers: List[str] = ["Student ID", "Name", "Phone Number", "Maths", "English", "SST", "Science", "Computer Science",
                   "Final Grade", "Total Marks", "Percentage"]
        
        # Print the entries in a tabular format using tabulate
        print(tabulate(entries, headers=headers, tablefmt="grid"))
    else:
        print("No entries found.")

#Decorator
@database_connection

def generate_subject_wise_report(con: MySQLConnection) -> None:
    """
    Generates and displays a report for each subject including average, highest, and lowest marks.
    """
    print("\n\t\t\t\tSUBJECT-WISE REPORT")
    
    # Iterator (cursor acts as an iterator over the database query results)
    cur = con.cursor()

    subjects = ['Maths', 'English', 'SST', 'Science', 'Computer Science']
    report = []

    for subject in subjects:
        query = f"SELECT AVG({subject.lower().replace(' ', '_')}), MAX({subject.lower().replace(' ', '_')}), MIN({subject.lower().replace(' ', '_')}) FROM student_info"
        cur.execute(query)
        avg_marks, max_marks, min_marks = cur.fetchone()
        report.append([subject, round(avg_marks, 2), max_marks, min_marks])

    headers = ["Subject", "Average Marks", "Highest Marks", "Lowest Marks"]
    print(tabulate(report, headers=headers, tablefmt="pretty"))

    con.close()

# Decorator
@database_connection    

def overall_summary_report(con: MySQLConnection) -> None:
    """
    Displays an overall summary report including average, highest, and lowest marks for all students.
    """
    print("\n\t\t\t\tOVERALL SUMMARY REPORT")
    
    # Iterator (cursor acts as an iterator over the database query results)
    cur = con.cursor()

    # Query to fetch all student records along with grades
    query = "SELECT * FROM grade_table"
    cur.execute(query)
    results = cur.fetchall()

    if results:
        report = []

        # Calculate overall statistics
        total_students = len(results)
        total_marks = 0
        highest_percentage = 0
        lowest_percentage = 100
        for row in results:
            total_marks += row[3]
            if row[4] > highest_percentage:
                highest_percentage = row[4]
            if row[4] < lowest_percentage:
                lowest_percentage = row[4]

        # Calculate overall average percentage
        overall_average_percentage = total_marks / (total_students * 500) * 100

        # Add overall statistics to the report
        report.append(["Total Students", total_students])
        report.append(["Overall Average Percentage", "{:.2f}".format(overall_average_percentage)])
        report.append(["Highest Percentage", highest_percentage])
        report.append(["Lowest Percentage", lowest_percentage])

        # Display the report
        headers = ["Statistic", "Value"]
        print(tabulate(report, headers=headers, tablefmt="pretty"))
    else:
        print("No student records found.")

    con.close()

def main() -> None:
    while True:
        menu()
        try:
            ch: int = int(input("ENTER YOUR CHOICE::"))
            if ch == 1:
                add_student()
            elif ch == 2:
                student_update()
            elif ch == 3:
                remove_student()
            elif ch == 4:
                add_grade()
            elif ch == 5:
                calculate_average()
            elif ch == 6:
                get_student_status()
            elif ch == 7:
                display_entries()
            elif ch == 8:
                generate_subject_wise_report()
            elif ch==9:    
                overall_summary_report()
            elif ch==10:
                exit()    
            else:
                print("PLEASE CHOOSE THE CORRECT CHOICE AND TRY AGAIN!!")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to your choice.")
        
        ch: int = int(input("\n\nPress 0 To Continue, Any Other Number To Exit...:"))
        if ch != 0:
            break

if __name__ == "__main__":
    main()


