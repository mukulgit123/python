class student:
    def __init__(self):
        self.name = ""
        self.age = ""

    def enroll(self, name, age):
        return self.name,self.age
    
    def display(self):
        print(self.name,self.age)


if __name__ == '__main__':
    a = student()
    a.enroll("Mukul",21)
    a.display()

    b = student()
    b.enroll("Modi", 60)
    b.display()