# Defining a class
class Student:

    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method
    def display(self):
        print("Student Details")
        print("----------------")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")
        print()


# Creating objects
student1 = Student("Antra Agarwal", 20, "B.Tech CSE")
student2 = Student("Rahul Sharma", 21, "BCA")

# Calling methods
student1.display()
student2.display()