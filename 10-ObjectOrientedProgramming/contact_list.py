class ContactList():
    def __init__(self, lst=None):
        self.list = lst if lst is not None else []

    def add_contact(self, person):
        self.list.append(person)

    def display(self):
        return [str(contact) for contact in self.list]