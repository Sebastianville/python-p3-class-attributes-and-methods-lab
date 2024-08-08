class Song:
 
    # Class attribute
    count = 0 
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    


    def __init__(self, name="", artist='', genre=''):
        # instance attributes
        self.name = name
        self.artist = artist 
        self. genre = genre 
        # Increment count to our songs
        Song.add_song_to_count()
        #Add genre to grenes list
        Song.add_to_genres(genre)
        #Add artist to artists list
        Song.add_to_artists(artist)
        
        # Add to genre count
        Song.add_to_genre_count(genre)
        
        # Add to artist count
        Song.add_to_artist_count(artist)
    
        
        

    @classmethod
    def add_song_to_count(cls):
        Song.count += 1 
    

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres: 
            cls.genres.append(genre)

    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists: 
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Add the count for the genre 
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        # add the count for the artist
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1





