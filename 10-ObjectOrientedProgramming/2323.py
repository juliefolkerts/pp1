class C():
    def __init__(self,name, surname, age,seniority ):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def display(self):
        if self.age >= 18:
            result = print(f'{self.surname.upper()}{self.name[0].upper()}{self.seniority}')
        else:
            result = print(f'{self.surname.lower()}{self.name[0].lower()}{self.seniority}')
        return result
    

C("Anna","May",17,7).display()
C("George","Brown",21,4) .display()
