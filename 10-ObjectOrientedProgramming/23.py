class C():
    def __init__(self,name, surname, age,seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def result(self):
        if int(self.age) >= 18:
            last_name = self.surname.upper()
            first_name = self.name[0].upper()
        else:
            last_name = self.surname.lower()
            first_name = self.name[0].lower()
        x = f'{last_name}{first_name}{self.seniority}'
        return x

emp1 = C("Anna","May",17,7)
emp2 = C("George","Brown",21,4)
print(emp1.result())
print(emp2.result())