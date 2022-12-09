
print("Student Management System using Python language")

class student:
    def __init__(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber

    def displayInfo(self):
        print("UserName: ", self.name)
        print("RollNumber: ", self.rollNumber)
        