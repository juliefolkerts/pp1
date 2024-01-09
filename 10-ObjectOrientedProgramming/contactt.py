class Contact():
    def __init__(self,name,email,phonenr):
        self.name = name 
        self.email = email
        self.phonenr = phonenr

    def __str__(self):
        return f'{self.name} {self.email} {self.phonenr}'