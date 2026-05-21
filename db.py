import sqlite3

class DatabaseManager:

    def __init__(self,db_name ="school.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_student(self,name, email):
        """INSERT NEW STUDENT"""
        self.cursor.execute("INSERT INTO students (name, email) VALUES (?,?)",(name,email,))
        self.conn.commit()

    def show_students(self):
        """Display all students"""
        self.cursor.execute("SELECT * FROM students",)
        return self.cursor.fetchall()
     
    def enroll_student(self,student_id,course_name):
        """ADD ENROLLMENT FOR A STUDENT"""

        self.cursor.execute("INSERT INTO enrollments (student_id, course_name) VALUES (?,?)",(student_id, course_name))

        self.conn.commit()

    def show_enrollments(self):
        """Display enrollments with student names"""
        #Joins: combines rows from 2 tables on a related column(usually a PK or FK)
        #INNER JOIN: only return matching rows
        #LEFT JOIN: all rows from the left table + matches from the right
        #RIGHT JOIN:all rows from the right table + matches from the left
        #FULL JOIN: everything from both tables , matching where possible

        self.cursor.execute("""
SELECT enrollments.enroll_id,students.name , enrollments.course_name FROM enrollments INNER JOIN students ON enrollments.student_id = students.student_id
 """)
        return self.cursor.fetchall()
    def close(self):
        """Close Db connection"""
        self.conn.close()