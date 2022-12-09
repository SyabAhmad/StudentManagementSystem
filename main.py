
print("Student Management System using Python language")

class student:
    def displayInfo(self, name, rollNumber):
        print("Your Name is: ",name)
        print("Your Roll Number is: ",rollNumber)

class DisplayPanel(student):
    def loginForm(self):
        name = str(input("Enter Your Key: "))
        pinCode = int(input("Enter Your Pin Code: "))
        if pinCode == 123321:
            self.displayInfo(name, pinCode)
        else:
            print("Invalid PIN Code or Key Phrase ")


panel = DisplayPanel()
panel.loginForm()