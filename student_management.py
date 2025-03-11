import time

class Student:

    def __init__(self, name: str, student_id: int):
        self.name = name
        self.student_id = student_id
        self.courses = {} # store the courses and (optionally) the grade for each course

    # enroll the student in a course
    def add_course(self, course_name):
        if course_name in self.courses:
            time.sleep(0.5)
            print(f"\n{course_name} already exists.\n")
        else:
            self.courses[course_name] = None
    
    # unenroll the student from a course if they are in it
    def remove_course(self, course_name):
        if course_name not in self.courses:
            time.sleep(0.5)
            print(f"\n{course_name} does not exist.\n")
        else:
            del self.courses[course_name]

    # set or update the student’s grade in a course
    def set_grade(self, course_name, grade):
        if course_name not in self.courses:
            time.sleep(0.5)
            print(f"\n{course_name} does not exist.\n")
        else:
            self.courses[course_name] = grade

    # retrieve the student’s grade for a course (optional)
    def get_grade(self, course_name):
        if course_name not in self.courses:
            time.sleep(0.5)
            print(f"\{self.name} is not enrolled in {course_name}\n")
        elif not self.courses[course_name]:
            time.sleep(0.5)
            print(f"\n{course_name} has no grade.\n")
        else:
            return self.courses[course_name]
    
    def get_info(self):
        return f"\nStudent Name: {self.name}\nStudent ID: {self.student_id}\n"


class Course:

    def __init__(self, course_name: str):
        self.course_name = course_name
        self.enrolled_students = {}

    def add_student(self, student_obj):
        if student_obj.student_id in self.enrolled_students:
            time.sleep(0.5)
            print(f"\n{student_obj.name} is already enrolled.\n")
        else:
            self.enrolled_students[student_obj.student_id] = student_obj
        
    def remove_student(self, student_id):
        if student_id not in self.enrolled_students:
            time.sleep(0.5)
            print(f"\n Student with the id: {student_id} does not exist.\n")
        else:
            del self.enrolled_students[student_id]

    # update the grade for the student in this course
    def set_student_grade(self, student_id, grade):
        if student_id not in self.enrolled_students:
            time.sleep(0.5)
            print(f"\n Student with the id: {student_id} does not exist.\n")
        else:
            self.enrolled_students[student_id].set_grade(self.course_name, grade)
    
    # look up a student’s grade in this course
    def get_student_grade(self, student_id):
        if student_id not in self.enrolled_students:
            time.sleep(0.5)
            print(f"\n Student with the id: {student_id} does not exist.\n")
        else:
            self.enrolled_students[student_id].get_grade(self.course_name)

class SchoolSystem:

    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_course(self, course_name):
        if course_name in self.courses:
            time.sleep(0.5)
            print(f"\n{course_name} already exists.\n")
        else:
            self.courses[course_name] = Course(course_name)
            print(f"\n{course_name} course has been added.")
            print(f"Current courses available: {[course for course in self.courses.keys()]}")

    def register_student(self, name, student_id):
        if student_id in self.students:
            time.sleep(0.5)
            print(f"\nStudent with id: {student_id} already exists.\n")
        else:
            self.students[student_id] = Student(name, student_id)
            print(f"\n{name} has been registered.")
            print(f"Current registered students: {[student.name for student in self.students.values()]}")

    def assign_student_to_course(self, student_id, course_name):
        if student_id in self.students and course_name in self.courses:

            student_obj = self.students[student_id]
            self.courses[course_name].add_student(student_obj)
            self.students[student_id].add_course(course_name)
            print(f"\n{student_obj.name} has been assigned to {course_name}")
            print(f"Current students enrolled in {course_name}: {[student.name for student in self.courses[course_name].enrolled_students.values()]}")

        elif student_id not in self.students:
            time.sleep(0.5)
            print(f"\nStudent with id: {student_id} does not exist.\n")
        elif course_name not in self.courses:
            time.sleep(0.5)
            print(f"\n{course_name} does not exist.\n")
        else:
            time.sleep(0.5)
            print(f"\nNeither {course_name} or student with id: {student_id} exists.\n")

    def grade_student(self, student_id, course_name, grade):
        if student_id in self.students and course_name in self.courses:

            self.courses[course_name].set_student_grade(student_id, grade)
            print(f"\n{self.students[student_id].name} now has a {grade} in {course_name}")
            print(f"Full Report on {self.students[student_id].name}:\n{self.students[student_id].courses}")

        elif student_id not in self.students:
            time.sleep(0.5)
            print(f"\nStudent with id: {student_id} already exists.\n")
        elif course_name not in self.courses:
            time.sleep(0.5)
            print(f"\n{course_name} does not exist.\n")
        else:
            time.sleep(0.5)
            print(f"\nNeither {course_name} or student with id: {student_id} exists.\n")

    def remove_student_from_course(self, student_id, course_name):
        if student_id in self.students and course_name in self.courses:

            self.courses[course_name].remove_student(student_id)
            self.students[student_id].remove_course(course_name)
            print(f"\n{self.students[student_id].name} has been removed from {course_name} course.")
            print(f"Full Report on {self.students[student_id].name}:\n{self.students[student_id].courses}")

        elif student_id not in self.students:
            time.sleep(0.5)
            print(f"\nStudent with id: {student_id} already exists.\n")
        elif course_name not in self.courses:
            time.sleep(0.5)
            print(f"\n{course_name} does not exist.\n")
        else:
            time.sleep(0.5)
            print(f"\nNeither {course_name} or student with id: {student_id} exists.\n")
        
    def list_students_in_course(self, course_name):
        print(f"\n All currently enrolled students in this course include:\n{[student.name for student in self.courses[course_name].enrolled_students.values()]}")


def invalid():
    time.sleep(0.5)
    print("\nInvalid choice.\n")
    time.sleep(0.5)
    print("Try again.\n")
    time.sleep(0.5)

def main():

    system = SchoolSystem()

    while True:

        print("\n1. Add Course\n"
        "2. Register Student\n"
        "3. Assign Student to Course\n"
        "4. Grade Student\n"
        "5. Remove Student from Course\n"
        "6. List all students in a Course\n"
        "7. Quit")

        try:
            choice = int(input("What would you like to do?: "))
            if choice >= 1 and choice <= 6:
                match choice:
                    case 1:
                        system.add_course(input("Enter course name: "))
                    case 2:
                        system.register_student(input("Enter student name: "), input("Enter student ID: "))
                    case 3:
                        system.assign_student_to_course(input("Enter student ID: "), input("Enter course name: "))
                    case 4:
                        system.grade_student(input("Enter student ID: "), input("Enter course name: "), input("Enter grade (number or letter): "))
                    case 5:
                        system.remove_student_from_course(input("Enter student ID: "), input("Enter course name: "))
                    case 6:
                        system.list_students_in_course(input("Enter course name: "))

            elif choice == 7:
                time.sleep(0.5)
                print("\nGoodbye.\n")
                time.sleep(0.5)
                break
            else:
                invalid()
        except:
                invalid()

if __name__ == "__main__":
    main()