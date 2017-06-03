def make_album(artist_name, album_title, album_tracks=''):
    """builds a dictionary describing a music album."""
    album_info = {'artist': artist_name, 'album': album_title, '#tracks': album_tracks}
    return album_info
    
while True:
    print("\nPlease provide an artist name and ")
    print("an album name")
    print("\n+++ Type quit to exit +++")
    
    ar_name = input("Artist name: ")
    if ar_name == 'quit':
        break
    al_name = input("Album name: ")
    if al_name == 'quit':
        break
    
    album = make_album(ar_name, al_name) 
    print(album) 
    
