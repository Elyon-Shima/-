# Question 2: School Class Management System
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added successfully.")

    def display_all_students(self):
        if not self.students:
            print("No students in the class.")
        else:
            print("List of Students:")
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")

    def get_student_average_grade(self, student_name):
        for student in self.students:
            if student.name == student_name:
                grades = student.grades.values()
                avg_grade = sum(grades) / len(grades)
                print(f"Average grade for {student_name}: {avg_grade}")
                return
        print(f"Student '{student_name}' not found.")

    def get_class_average_grade(self, subject):
        total_grades = 0
        total_students = 0
        for student in self.students:
            if subject in student.grades:
                total_grades += student.grades[subject]
                total_students += 1
        
        if total_students == 0:
            print(f"No students have grades for {subject}.")
        else:
            class_avg_grade = total_grades / total_students
            print(f"Class average grade for {subject}: {class_avg_grade}")

# Part 3
classroom = Classroom()

student1 = Student("Alice", {"Math": 90, "Science": 85, "History": 88})
student2 = Student("Bob", {"Math": 75, "Science": 78, "History": 80})

classroom.add_student(student1)
classroom.add_student(student2)

classroom.display_all_students()

classroom.get_student_average_grade("Alice")
classroom.get_class_average_grade("Math")
