print("Welcome to the Student Data Organizer!\n")

students = []

while True:
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit\n")

    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        print("Enter student details:")
        stud_id = int(input("Student ID: "))
        stud_name = (input("Name: "))
        stud_age = int(input("Age: "))
        stud_grade = (input("Grade: "))
        stud_dob = (input("Date of Birth (YYYY-MM-DD): "))
        stud_subjects = (input("Subjects (comma-separated): "))
        student_tuple = (stud_id, stud_dob)
        student_set = set(subject.strip() for subject in stud_subjects.split(","))
        student = {
            "ID & DOB": student_tuple,
            "Name": stud_name,
            "Age": stud_age,
            "Grade": stud_grade,
            "Subjects": student_set
        }
        students.append(student)
        print("Student added successfully!\n")

    elif choice == 2:
        print("--- Display All Students ---")

        if not students:
            print("No student records found.\n")
            continue

        for student in students:
            print(
                f"Student ID: {student['ID & DOB'][0]} | "
                f"Name: {student['Name']} | "
                f"Age: {student['Age']} | "
                f"Grade: {student['Grade']} | "
                f"Subjects: {', '.join(sorted(student['Subjects']))}"
            )
            print()
    
    elif choice == 3:
        update_id = int(input("Enter Student ID to update: "))

        for student in students:
            if student["ID & DOB"][0] == update_id:
                student["Name"] = input("New Name: ")
                student["Age"] = int(input("New Age: "))
                student["Grade"] = input("New Grade: ")
                subjects = input("New Subjects (comma-separated): ")
                student["Subjects"] = set(subject.strip() for subject in subjects.split(","))

                print("Student information updated successfully!\n")
                break
        else:
            print("Student ID not found.\n")

    elif choice == 4:
        delete_id = int(input("Enter Student ID to delete: "))

        for student in students:
            if student["ID & DOB"][0] == delete_id:
                del students[students.index(student)]
                print("Student deleted successfully!\n")
                break
        else:
            print("Student ID not found.\n")

    elif choice == 5:
        if not students:
            print("No subjects available.\n")
            continue

        all_subjects = set()

        for student in students:
            all_subjects.update(student["Subjects"])

        print("Subjects Offered:")
        print(", ".join(sorted(all_subjects)))
        print()
        
    elif choice == 6:
        break
    else:
        print("Invalid choice\n")

print("Thanks for using Student Data Organizer.\nHave a nice day!")