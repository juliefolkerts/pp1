from contact import Contact
from contact_list import ContactList

clist = ContactList()
contact1 = Contact('John Brown' ,'brown@onet.pl','555234000')
clist.add_contact(contact1)
print(clist.display())