from classes.person import Person
import csv

class Staff(Person):
    all_staff_lst=[]
    
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id
        
    @classmethod
    def all_staff(self):
        with open('./data/staff.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.all_staff_lst.append(Staff(**row))
        return self.all_staff_lst