from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def print_data(self):
        """ Implement in child class. """

class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Some Name", 20)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton can't be instatiatied more than once.")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
     
    @staticmethod
    def print_data():
        print(PersonSingleton.__instance.name)
        print(PersonSingleton.__instance.age)

p = PersonSingleton("Mike", 20)
print(p)
p.print_data()

p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()

p = PersonSingleton("Goku", 2000)