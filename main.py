# Student-Grade-Mangement-System_Vithyarthi-Project

students = []


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def add_student():
    print("\n--- Add Student ---")

    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")

    try:
        maths = float(input("Enter Mathematics marks: "))
        programming = float(input("Enter Programming marks: "))
        physics = float(input("Enter Physics marks: "))
        english = float(input("Enter English marks: "))
        electronics = float(input("Enter Electronics marks: "))
    except ValueError:
        print("Please enter marks using numbers only.")
        return

    marks = [maths, programming, physics, english, electronics]

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Marks should be between 0 and 100.")
        return

    total = sum(marks)
    percentage = total / 5
    grade = calculate_grade(percentage)

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully.")


def display_students():
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nRoll Number :", student["roll_no"])
        print("Name        :", student["name"])
        print("Total       :", student["total"], "/ 500")
        print("Percentage  :", round(student["percentage"], 2), "%")
        print("Grade       :", student["grade"])


def search_student():
    print("\n--- Search Student ---")
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found")
            print("Name        :", student["name"])
            print("Roll Number :", student["roll_no"])
            print("Total       :", student["total"], "/ 500")
            print("Percentage  :", round(student["percentage"], 2), "%")
            print("Grade       :", student["grade"])
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
