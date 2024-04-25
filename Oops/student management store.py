class Student:
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept_student_details(self):
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        student = Student(roll_no, name, age, grade)
        self.students.append(student)
        print("Student details added successfully!")

    def display_student_details(self):
        if self.students:
            print("Student Details:")
            for student in self.students:
                print(f"Roll Number: {student.roll_no}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
        else:
            print("No student details available.")

    def search_student_details(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"Student found - Roll Number: {student.roll_no}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
                return
        print("Student not found.")

    def delete_student_details(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student details deleted successfully!")
                return
        print("Student not found.")

    def update_student_details(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                name = input("Enter new Name: ")
                age = input("Enter new Age: ")
                grade = input("Enter new Grade: ")
                student.name = name
                student.age = age
                student.grade = grade
                print("Student details updated successfully!")
                return
        print("Student not found.")

def main():
    sms = StudentManagementSystem()

    while True:
        print("\nOptions:")
        print("1. Accept Student Details")
        print("2. Display Student Details")
        print("3. Search Details of a Student")
        print("4. Delete Details of Student")
        print("5. Update Student Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sms.accept_student_details()
        elif choice == '2':
            sms.display_student_details()
        elif choice == '3':
            roll_no = input("Enter Roll Number to search: ")
            sms.search_student_details(roll_no)
        elif choice == '4':
            roll_no = input("Enter Roll Number to delete: ")
            sms.delete_student_details(roll_no)
        elif choice == '5':
            roll_no = input("Enter Roll Number to update: ")
            sms.update_student_details(roll_no)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
