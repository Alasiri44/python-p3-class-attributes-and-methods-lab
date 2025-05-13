# defining a class called
class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        if self.genre not in Song.genres:Song.genres.append(self.genre) 
        
        if self.artist not in Song.artists: Song.artists.append(self.artist) 
        
        if (not Song.genre_count.get(self.genre)):
            Song.genre_count[self.genre] = 1
        else:
            Song.genre_count[self.genre] += 1
            
        if (not Song.artist_count.get(self.artist)):
            Song.artist_count[self.artist] = 1
        else:
            Song.artist_count[self.artist] += 1
    
    
Song("99 Problems", "Jay Z", "Rap")
Song("Halo", "Beyonce", "Pop")
Song("Smells Like Teen Spirit", "Nirvana", "Rock")