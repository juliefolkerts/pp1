from Ebook import EBook

book1 = EBook("The Great Gatsby", "F. Scott Fitzgerald", 180)

book1.is_open() 

print(book1)

book1.read_page()
book1.read_page()
book1.read_page()

print(book1.status())

book1.close()

#book1.read_page()

message = book1.read_page()

print(book1.status())

if message == None:
    print(message) 