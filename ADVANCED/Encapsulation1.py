class Person:
    def __init__(self, name, age, gender):
        self.__name = name  # Two underscores set the attributes to private
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @property
    def Age(self):
        return self._age

    @Age.setter
    def Age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative. Setting age to 0.")

    @staticmethod
    def mymethod():
        print("Hello World!!")


# For calling a method of a class without instantiating an object of the class.
Person.mymethod()
p1 = Person("Mike", 29, 'm')
print(p1.Name)
p2 = Person("Not here", -1, 'm')
print(p2.Name)
p2.Age = -1
print(p2.Name)
