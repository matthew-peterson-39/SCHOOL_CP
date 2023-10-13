from classes.person import Person
import csv

class Student(Person):
    all_student_lst=[]
    
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id
        
    @classmethod
    def all_students(self):
        with open('./data/students.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.all_student_lst.append(Student(**row))
        return self.all_student_lst