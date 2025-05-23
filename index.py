import json
import os
from datetime import date

# Files to persist data
STUDENTS_FILE = "students.json"
ATTENDANCE_FILE = "attendance.json"

# Global lists
students = []
attendance = []

# Load and Save functions
def load_data():
    global students, attendance
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as f:
            students = json.load(f)
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "r") as f:
            attendance = json.load(f)

def save_data():
    with open(STUDENTS_FILE, "w") as f:
        json.dump(students, f, indent=4)
    with open(ATTENDANCE_FILE, "w") as f:
        json.dump(attendance, f, indent=4)

# Main menu
def main_menu():
    while True:
        print("\n===== Main Menu =====")
        print("1. Enroll New Student")
        print("2. Update Student Details")
        print("3. Mark Attendance")
        print("4. View Attendance")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            enroll_new_student()
        elif choice == "2":
            update_details()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            view_attendance()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

# Enroll student
def enroll_new_student():
    print("\n--- Enroll New Student ---")
    student_id = input("Enter student ID: ")
    if any(s[0] == student_id for s in students):
        print("Student ID already exists.")
        return
    title = input("Enter title (e.g., Mr/Ms): ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    mobile = input("Enter mobile number: ")
    email = input("Enter email address: ")
    tutor_group = input("Enter tutor group: ")
    centre = input("Enter centre name: ")

    student_data = [
        student_id, title, first_name, last_name, address,
        mobile, email, tutor_group, centre
    ]
    students.append(student_data)
    save_data()
    print(f"Student {first_name} {last_name} added successfully.")

# Update student details
def update_details():
    print("\n--- Update Student Details ---")
    student_id = input("Enter student ID: ")
    for student in students:
        if student[0] == student_id:
            print("Current data:")
            for i, field in enumerate(["ID", "Title", "First Name", "Last Name", "Address", "Mobile", "Email", "Tutor Group", "Centre"]):
                print(f"{field}: {student[i]}")
            print("Enter new data (leave blank to keep current):")
            for i in range(1, 9):
                new_data = input(f"{['Title', 'First Name', 'Last Name', 'Address', 'Mobile', 'Email', 'Tutor Group', 'Centre'][i-1]}: ")
                if new_data:
                    student[i] = new_data
            save_data()
            print("Student data updated.")
            return
    print("Student ID not found.")

# Mark attendance
def mark_attendance():
    print("\n--- Mark Attendance ---")
    tutor_group = input("Enter tutor group: ")
    centre = input("Enter centre name: ")
    today = str(date.today())
    count = 0

    for student in students:
        if student[7] == tutor_group and student[8] == centre:
            presence = input(f"Is {student[2]} {student[3]} (ID: {student[0]}) present? (yes/no): ").strip().lower()
            status = "Present" if presence == "yes" else "Absent"
            attendance.append({
                "student_id": student[0],
                "date": today,
                "status": status
            })
            count += 1

    if count > 0:
        save_data()
        print("Attendance marked successfully.")
    else:
        print("No students found for this group and centre.")

# View attendance
def view_attendance():
    print("\n--- View Attendance ---")
    student_id = input("Enter student ID: ")
    records = [record for record in attendance if record["student_id"] == student_id]
    if not records:
        print("No attendance records found for this student.")
    else:
        print(f"Attendance for Student ID {student_id}:")
        for record in records:
            print(f"{record['date']}: {record['status']}")

# Start the app
load_data()
main_menu()
