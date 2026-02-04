# Student Management System

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, marks, roll_no):
        super().__init__(name, age)
        self.marks = marks
        self.roll_no = roll_no

    def show_student(self):
        print(self.display_info())
        print(f"Roll No: {self.roll_no}, Marks: {self.marks}")


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def show_teacher(self):
        print(self.display_info())
        print(f"Subject: {self.subject}, Salary: {self.salary}")


# Objects
s1 = Student("Yash", 20, 85, 101)
t1 = Teacher("Mr. Sharma", 45, "Mathematics", 50000)

# Output
print("Student Details:")
s1.show_student()

print("\nTeacher Details:")
t1.show_teacher()
