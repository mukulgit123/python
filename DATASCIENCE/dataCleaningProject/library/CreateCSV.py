import pandas as pd

class CreateCSV:
    def __init__(self, person , filename, recordcount):
        '''This class is used to create a csv file from the data provided'''
        self.person = person
        self.filename = filename
        self.recordcount = recordcount
        self.write_to_csv()
    
    def write_to_csv(self):
        '''This function is used to write the data to a csv file'''
        persons = []
        try:
            for i in range(self.recordcount):
                person_generator = self.person.generate_person()
                for person_data in person_generator:
                    cleaned_record = tuple(s.replace('\n', '') for s in person_data)
                    persons.append(cleaned_record)
            df = pd.DataFrame(persons, columns=['Name', 'Address', 'Email', 'Text', 'Phone Number', 'Country'])
            df.to_csv(self.filename, index=False)
        except Exception as e:
            raise e
        

