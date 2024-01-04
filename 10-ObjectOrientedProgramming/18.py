class Book():
    def __init__(self,title,author,current_page,page_nrs=10):
        self.title = title
        self.author = author
        self.page_nrs = page_nrs
        self.current_page = current_page

    def open_book(self):
        
