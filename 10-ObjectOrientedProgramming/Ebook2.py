class Ebook():
    def __init__(self,title,author,pages):
        self.author = author
        self.title = title
        self.pages = pages
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def read_pages(self,amount):
        if self.is_open == True:
            self.amount = amount
            self.current_page += int(amount)
        else:
            print('Can not read book, it is closed')

    def display_status(self):
        if self.is_open == False:
            return 'Book is closed'
        else:
            return f'{self.title} is written by {self.author}\nTotal pages:{self.pages}\nCurrent page:{self.current_page}'