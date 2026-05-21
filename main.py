from db import DatabaseManager
def main():
    db =DatabaseManager()
    while True:
        print("\n-----Student Enrollment system-----")
        print("1.Add student")
        print("2.Show student")
        print("3.Enroll student in course")
        print("4.Show student Enrollments")
        print("5.Exit")

        choice = input("Enter a number:")

        if choice =="1":
            #collect info and insert student 
            name= input("Enter student name:")
            email= input("Enter student email:") 
            db.add_student(name,email)
            print("Student added successfully")

        elif choice =="2":
            #display students
            students = db.show_students()
            print("\n-----Students----")
            for s in students:
                print(f"{s[0]}\t{s[1]}\t{s[2]}")
        
        elif choice =="3":
            #collect info and enroll exixting student 
            student_id= int(input("Enter student ID:"))
            course_name= input("Enter course name :") 
            db.enroll_student(student_id,course_name)
            print("Student enrolled into course successfully")

        elif choice =="4":
            #display student enrollments
            enrollments = db.show_enrollments()
            print("\n-----Enrollments----")
            for e in enrollments:
                print(f"{e[0]}\t{e[1]}\t{e[2]}")

        elif choice =="5":
            #Close
            db.close()
            print("Goodbye")
            break
        else:
            print("Invalid Choice, Try again")

if __name__ =="__main__":
    main()