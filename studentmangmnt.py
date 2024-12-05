class Student:
    def __init__(self, student_id=0, name=None, email=None, phone=0):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.students = {}
    def __str__(self): 
        return f"ID: {self.student_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

# class StudentManager:
#     def __init__(self):
        # self.students = {}

    def addstudent(self, student):
        if student.student_id in self.students:
            print("A student with this ID already exists.")
        else:
            self.students[student.student_id] = student
            print("Student added successfully.")

    def displaystudent(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(student)
        else:
            print("Student not found.")

    def updatestudent(self, student_id, name=None, email=None, phone=None):
        student = self.students.get(student_id)
        if student:
            if name:
                student.name = name
            if email:
                student.email = email
            if phone:
                student.phone = phone
            print("Updated successfully.")
        else:
            print("Student not found.")

    def deletestudent(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def menu(self):
        print("1. Look up a Student by ID")
        print("2. Add Student")
        print("3. Update Student's Details")
        print("4. Delete a Student by ID")
        print("5. Quit")

    def main():


        while True:
            main.menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                student_id = input("Enter Student ID: ")
                main.displaystudent(student_id)
            elif choice == '2':
                student_id = input("Enter Student ID: ")
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone Number: ")
                student = Student(student_id, name, email, phone)
                main.addstudent(student)
            elif choice == '3':
                student_id = input("Enter Student ID: ")
                name = input("Enter new Name: ")
                email = input("Enter new Email: ")
                phone = input("Enter new Phone Number: ")
                main.updatestudent(student_id, name, email, phone)
            elif choice == '4':
                student_id = input("Enter Student ID: ")
                main.deletestudent(student_id)
            elif choice == '5':
                print("******END******")
                break
            else:
                print("Invalid choice.")

main=Student()
Student.main()

