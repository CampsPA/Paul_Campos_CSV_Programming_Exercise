"""
This program manages student exam records using a CSV file.

It includes two main functions:

1. A function to collect student data (first name, last name, and three exam grades)
   from the instructor and write it to a CSV file named 'grades.csv' using the csv module.
   Each student record includes a header row: First Name, Last Name, Exam 1, Exam 2, Exam 3.

2. A separate function to read the 'grades.csv' file and display its contents
   in a neatly formatted table using the with keyword for file handling.

This modular design ensures that data entry and data retrieval are kept as distinct,
reusable components.
"""
import csv

class Grades:
    def __init__(self):
        self.first_name = []
        self.last_name = []
        self.exam_1 = []
        self.exam_2 = []
        self.exam_3 = []


    def create_file(self):
        # Name the file.
        self.csv_file = 'grades.csv'

        # Create the headers.
        self.csv_headers = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']

        # Write the csv file.
        with open(self.csv_file, mode = 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            # Write the headers.
            csvwriter.writerow(self.csv_headers)

        # Record inputs
        while True:
            first_name = str(input('Enter the first name: '))
            last_name = str(input('Enter the last name: '))
            exam_1 = float(input('Enter exam 1 grade: '))
            exam_2 = float(input('Enter exam 2 grade: '))
            exam_3 = float(input('Enter exam 3 grade: '))
            self.first_name.append(first_name)
            self.last_name.append(last_name)
            self.exam_1.append(exam_1)
            self.exam_2.append(exam_2)
            self.exam_3.append(exam_3)

            # Record additional information.
            repeat = str.lower(input('Would you like to enter another information? y= yes, n= no: '))
            if repeat != 'y':
                print('Information recorded')
                break
        # Combine all student data using zip.
        rows = zip(self.first_name, self.last_name, self.exam_1, self.exam_2, self.exam_3)

        # Add data rows
        with open(self.csv_file, mode='a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            # Write all rows to the file
            csvwriter.writerows(rows)

    # Read the file
    def read_file(self):
        with open('grades.csv', mode='r', newline='') as csv_file:
            # Create a csv reader object.
            csvreader = csv.reader(csv_file)

            # Read the entire file.
            data = list(csvreader)

            # Format and display as a table
            print("\nStudent Grades:\n")
            for i, row in enumerate(data):
                if i == 0:
                    print(f"{row[0]:<15} {row[1]:<15} {row[2]:<8} {row[3]:<8} {row[4]:<8}")
                    print("-" * 60)
                else:
                    print(f"{row[0]:<15} {row[1]:<15} {row[2]:<8} {row[3]:<8} {row[4]:<8}")

# CReate a main function
def main():
    # Create an instance of the Grades class
    grades = Grades()
    # Call the method to write the file.
    grades.create_file()
    # Call the method to read the file an display its contents.
    grades.read_file()

if __name__ == "__main__":
    main()

