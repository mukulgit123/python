from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ This is an interface method """


class Person(IPerson):

    def person_method(self):
        print("I am a Person.")


class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am a proxy person.")
        self.person.person_method()


p1 = Person()
p1.person_method()
p = ProxyPerson()
p.person_method()
