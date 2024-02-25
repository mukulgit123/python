from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def person_method(): 
        """ This is an interface method """

class Student(IPerson):
    def __init__(self):
        self.name = "Student here"
    
    def person_method(self):
        print("I am a student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Teacher here"
    
    def person_method(self):
        print("I am a teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        else:
            print("Invalid Object Type")
            raise Exception(TypeError)

if __name__ == "__main__":
    choice = input("What kind of person do you want to create?")
    person = PersonFactory.build_person(choice)
    person.person_method()

s1 = Student()
s1.person_method()
t1 = Teacher()
t1.person_method()




