# Student Management System

students = []

# Function to add student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))

    mark1 = int(input("Enter mark 1: "))
    mark2 = int(input("Enter mark 2: "))
    mark3 = int(input("Enter mark 3: "))

    marks = (mark1, mark2, mark3)

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


# Function to display students
def display_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\nStudent Details:")
        for student in students:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            print("Average:", calculate_average(student["marks"]))
            print("------------------------")


# Function to calculate average
def calculate_average(marks):
    return sum(marks) / len(marks)


# Function to find topper
def find_topper():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        topper = students[0]

        for student in students:
            if sum(student["marks"]) > sum(topper["marks"]):
                topper = student

        print("\nTopper Details")
        print("Name:", topper["name"])
        print("Marks:", topper["marks"])
        print("Average:", calculate_average(topper["marks"]))
        print()


# Main menu using while loop
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        find_topper()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.\n")