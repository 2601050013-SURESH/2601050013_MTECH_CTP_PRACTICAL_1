students = []

def add_student():
    name = input("Enter student name: ")
    number = input("Enter student number: ")
    conducted = int(input("Enter total classes conducted: "))
    attended = int(input("Enter total classes attended: "))

    if conducted <= 0:
        print("Total classes conducted must be greater than 0.")
        return

    if attended < 0 or attended > conducted:
        print("Invalid number of classes attended.")
        return

    percentage = (attended / conducted) * 100

    student = {
        "name": name,
        "number": number,
        "conducted": conducted,
        "attended": attended,
        "percentage": percentage
    }

    students.append(student)
    print("Student added successfully.")


def display_attendance():
    if not students:
        print("No student records available.")
        return

    print("\nStudent Attendance")
    print("-" * 70)

    for student in students:
        print(
            f"Name: {student['name']}, "
            f"Number: {student['number']}, "
            f"Attendance: {student['percentage']:.2f}%"
        )


def below_75():
    low_attendance = [
        student for student in students
        if student["percentage"] < 75
    ]

    print("\nStudents Below 75%")

    if not low_attendance:
        print("No students are below 75%.")
        return

    for student in low_attendance:
        print(
            f"{student['name']} ({student['number']}) - "
            f"{student['percentage']:.2f}%"
        )


def highest_attendance():
    if not students:
        print("No student records available.")
        return

    highest = max(students, key=lambda student: student["percentage"])

    print("\nHighest Attendance")
    print("Student Name:", highest["name"])
    print("Student Number:", highest["number"])
    print(f"Attendance: {highest['percentage']:.2f}%")


def class_average():
    if not students:
        print("No student records available.")
        return

    total_percentage = sum(
        student["percentage"] for student in students
    )

    average = total_percentage / len(students)

    print("\nClass Average Attendance")
    print(f"Average Attendance: {average:.2f}%")


def attendance_report():
    if not students:
        print("No student records available.")
        return

    display_attendance()
    below_75()
    highest_attendance()
    class_average()


def main():
    while True:
        print("\n" + "=" * 50)
        print("       STUDENT ATTENDANCE ANALYZER")
        print("=" * 50)
        print("1. Add Student")
        print("2. Display Attendance")
        print("3. Find Students Below 75%")
        print("4. Find Highest Attendance")
        print("5. Calculate Class Average")
        print("6. Display Complete Report")
        print("7. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_attendance()
        elif choice == "3":
            below_75()
        elif choice == "4":
            highest_attendance()
        elif choice == "5":
            class_average()
        elif choice == "6":
            attendance_report()
        elif choice == "7":
            print("Thank you.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
