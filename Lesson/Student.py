from Lesson.MarkClass import Mark
from Lesson.Person import Person

# Класс студента

class Student(Person):
    marks: list

    def __init__(self, name, surname, patronic, birth_year):

        self.marks = [Mark(5, "math"), Mark(4, "math"), Mark(4, "math"), Mark(2, "math")]

        self.calculate_age()

        self.name

    def show_marks(self):
        print(self.__name)
        for mark in self.marks:
            print(mark.subject, mark.value)


    def calculate_avg(self):
        mark_sum = 0
        for mark in self.marks:
            mark_sum += mark.value

        self.avg = mark_sum / len(self.marks)

    def get_name(self):
        return self.__name


student = Student("Ivan", "Petrov", "Petrovich", 2000)

mark = Mark(5, "math")

print(student.get_name(), student.age)

student.show_marks()

student.calculate_avg()

print(student.avg)


student.calculate_avg()