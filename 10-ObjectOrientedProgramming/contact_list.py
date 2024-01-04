class ContactList():
    def __init__(self,list=[]):
        self.list = list

    def add_contact(self,person):
        self.person = person
        x = self.list
        x.append(self.person)

    def display(self):
        return self.list