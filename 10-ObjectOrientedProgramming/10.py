class Music():
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = str(year)
    def __str__(self):
        a = 'Performer: '+ self.artist + '\n'
        b = 'Song:      '+ self.track_title + '\n'
        c = 'Album:     '+ self.album + '\n'
        d = 'Year:      '+ self.year
        return a + b + c + d
    
song1 = Music('Ed', 'Heyy', 'Ho', 2004)
print(song1)