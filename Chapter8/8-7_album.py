def make_album(artist_name, album_title, album_tracks=''):
    """builds a dictionary describing a music album."""
    album_info = {'artist': artist_name, 'album': album_title, '#tracks': album_tracks}
    return album_info
    
album = make_album('skinny puppy', 'VIVIsectVI', 9 )
print(album)

album = make_album('smashing pumpkins', 'siamese dream')
print(album)
    
