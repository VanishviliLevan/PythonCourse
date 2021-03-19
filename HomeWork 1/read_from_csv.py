import  csv

class Employee:
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def info(self):
        print(f"Name - {self.name} , Surname - {self.surname} , Age - {self.age} , Salary - {self.salary}")


f = open("data.csv", "r")
data = csv.reader(f)

data_obj = []
for i in data:
    tmp = Employee(i[0], i[1], i[2], i[3])
    data_obj.append(tmp)

max_salary = max(data_obj[1:], key=lambda x: x.salary)
min_age = min(data_obj[1:], key=lambda x: x.age)

max_salary.info()
min_age.info()
