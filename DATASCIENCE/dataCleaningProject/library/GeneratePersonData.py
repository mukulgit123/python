from faker import Faker
from typing import Generator, Any
class GeneratePersonData:
    '''This class is used to generate fake person data using faker library'''
    def __init__(self):
        self.fake = Faker()
        
    def generate_person(self) -> Generator[Any, Any, Any]:
        '''This function is used to generate fake person data using faker library and yield the data as a generator object'''
        yield (self.fake.name(),self.fake.address(),self.fake.email(),self.fake.text(),self.fake.phone_number(),self.fake.country())

