class Musicpiece():
    def __init__(self,artist, title, album, year):
        self.artist = artist
        self.title = title 
        self.album = album
        self.year = year

    def __str__(self):
        return f'performer:{self.artist}\nsong:{self.title}\nalbum:{self.album}\nyear:{self.year}'
    
song1 = Musicpiece('ed', 'singie','albumi','2004')
print(song1)