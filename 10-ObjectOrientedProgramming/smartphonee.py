from contactt import Contact
from contactlist import Contact_list

List = Contact_list()
person1 = Contact('John Brown','brown@onet.pl',555234000)
person2 = Contact('Anna May','am@o2.pl',232000199)
person3 = Contact('George Small','smallg@google.pl',222999100)
List.add_person(person1)
List.add_person(person2)
List.add_person(person3)
print(List.display())