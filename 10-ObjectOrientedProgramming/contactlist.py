

class Contact_list():
    def __init__(self,lst=[]):
        self.lst = lst

    def add_person(self,person):
        self.person = person
        self.lst.append(self.person)

    def display(self):
        print('ContactList:')
        result = []
        for contact in self.lst:
            result.append(f"Name: {contact.name}\t Email: {contact.email}\t Telephone: {contact.phonenr}")
        return '\n'.join(result)