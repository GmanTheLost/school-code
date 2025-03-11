class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}  # {course_name: grade}

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = None
            print(f"Successfully added course: {course_name}")
        else:
            print(f"Student {self.name} is already enrolled in {course_name}.")

    def remove_course(self, course_name):
        if course_name in self.courses:
            del self.courses[course_name]
            print(f"Successfully unenrolled {self.name} from course: {course_name}")
        else:
            print(f"{self.name} is not enrolled in {course_name}")

    def set_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
            print(f"Successfully set grade for {course_name}: {grade}")
        else:
            print(f"Cannot set grade. Course {course_name} not found.")

    def get_grade(self, course_name):
        return self.courses.get(course_name, "No grade available")


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.enrolled_students = {}  # {student_id: Student object}

    def add_student(self, student):
        self.enrolled_students[student.student_id] = student
        student.add_course(self.course_name)

    def remove_student(self, student_id):
        if student_id in self.enrolled_students:
            self.enrolled_students[student_id].remove_course(self.course_name)
            del self.enrolled_students[student_id]

    def set_student_grade(self, student_id, grade):
        if student_id in self.enrolled_students:
            self.enrolled_students[student_id].set_grade(self.course_name, grade)

    def list_students(self):
        if not self.enrolled_students:
            print(f"No students enrolled in {self.course_name}.")
        else:
            print(f"Students in {self.course_name}:")
            for student in self.enrolled_students.values():
                print(f"- {student.name} (ID: {student.student_id})")


class SchoolSystem:
    def __init__(self):
        self.students = {}  # {student_id: Student object}
        self.courses = {}  # {course_name: Course object}

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = Course(course_name)
            print(f"Successfully added course: {course_name}")
        else:
            print(f"Course {course_name} already exists.")

    def register_student(self, name, student_id):
        if student_id not in self.students:
            self.students[student_id] = Student(name, student_id)
            print(f"Successfully registered student: {name} (ID: {student_id})")
        else:
            print(f"Student ID {student_id} is already registered.")

    def assign_student_to_course(self, student_id, course_name):
        if student_id in self.students and course_name in self.courses:
            course = self.courses[course_name]
        # Check if the student is already enrolled in the course
            if student_id in course.enrolled_students:
                print(f"Student {student_id} is already enrolled in {course_name}.")
            else:
                course.add_student(self.students[student_id])
                print(f"Successfully assigned student {student_id} to course {course_name}")
        else:
            print("Error: Invalid student ID or course name.")

    def grade_student(self, student_id, course_name, grade):
        if course_name in self.courses and student_id in self.students:
            self.courses[course_name].set_student_grade(student_id, grade)
            print(f"Successfully graded student {student_id} in {course_name}: {grade}")
        else:
            print("Error: Invalid student ID or course name.")

    def remove_student_from_course(self, student_id, course_name):
        if course_name in self.courses and student_id in self.students:
            self.courses[course_name].remove_student(student_id)
            print(f"Successfully removed student {student_id} from {course_name}")
        else:
            print("Error: Invalid student ID or course name.")

    def list_students_in_course(self, course_name):
        if course_name in self.courses:
            self.courses[course_name].list_students()
        else:
            print(f"Course {course_name} does not exist.")


def main():
    system = SchoolSystem()

    while True:
        print("\n--- SIMPLE STUDENT MANAGEMENT ---")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Assign Student to Course")
        print("4. Grade Student")
        print("5. Remove Student from Course")
        print("6. List Students in Course")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            cname = input("Enter course name: ")
            system.add_course(cname)

        elif choice == '2':
            name = input("Enter student name: ")
            sid = input("Enter student ID: ")
            system.register_student(name, sid)

        elif choice == '3':
            sid = input("Enter student ID: ")
            cname = input("Enter course name: ")
            system.assign_student_to_course(sid, cname)

        elif choice == '4':
            sid = input("Enter student ID: ")
            cname = input("Enter course name: ")
            grade = input("Enter grade: ")
            system.grade_student(sid, cname, grade)

        elif choice == '5':
            sid = input("Enter student ID: ")
            cname = input("Enter course name: ")
            system.remove_student_from_course(sid, cname)

        elif choice == '6':
            cname = input("Enter course name: ")
            system.list_students_in_course(cname)

        elif choice == '7':
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()
