class EBook():
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = 1
        self.open = False

    def is_open(self):
        self.open = True
    
    def close(self):
        self.open = False
    
    def read_page(self):
        if self.open:
            if self.current_page < self.num_pages:
                self.current_page += 1
                return None
            else:
                return 'book is already finished'
        else:
            return 'not possible to read when the book is closed'

    def status(self):
        if self.open:
            return f'current page:{self.current_page}'
        else:
            return 'book is closed'

    def __str__(self):
        return f"EBook: {self.title} by {self.author} - {self.num_pages} pages"   
