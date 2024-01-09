from Ebook2 import Ebook

Book1 = Ebook('Boek', 'Schrijver', 100)
Book1.open()
print(Book1.display_status())
Book1.read_pages(8)
print(Book1.display_status())
Book1.close()
Book1.read_pages(5)
print(Book1.display_status())
