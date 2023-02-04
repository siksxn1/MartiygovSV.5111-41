from Lesson.IPerson import IPerson
import datetime

class Person(IPerson):
    surname: str
    patronic: str
    birth_year: int


    def __init__(self, name, surname, patronic, birth_year):
        pass

    def calculate_age(self):
        self.age = datetime.datetime.now().year - self.birth_year
