from services.student_service import (
    get_all_students,
    add_student,
    update_student,
    delete_student,
    student_search_by_id
)

while True:
    print("\n====== Student Management System ======\n")
    print("1. View students:")
    print("2. Add students:")
    print("3. Update students:")
    print("4. Delete students:")
    print("5. Search students:")
    print("6. Exit")

    choice = input("Enter your choice: ") 

    if choice == "1":
        students = get_all_students()

        print("\nStudents: ")

        for s in students:
            print(f"Id: {s[0]} | Name: {s[1]} | Age: {s[2]} | Course: {s[3]}")

    elif choice == "2":
        name = input("Enter your name: ")            
        age = int(input("Enter your age: "))          
        course = input("Enter your course: ")      

        add_student(name, age, course)

    elif choice == "3":
        id = int(input("Enter id to update: ")) 
        name = input("Enter new name: ")            
        age = int(input("Enter new age: "))          
        course = input("Enter new course: ")      

        update_student(id, name, age, course)    

    elif choice == "4":
        id = int(input("Enter id to delete: "))

        delete_student(id)

    elif choice == "5":
        id = int(input("Enter id to search: "))

        student = student_search_by_id(id)  

        if student:
            print(f"Id: {s[0]} | Name: {s[1]} | Age: {s[2]} | course: {s[3]}")

        else:
            print("Student not found!!!!")    

    elif choice == "6":
        print("Exiting Programm...... ") 
        break  

    else:
        print("Invalid choice!.... Try Again!!!")