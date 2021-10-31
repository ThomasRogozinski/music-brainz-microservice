import musicbrainzngs as mb

def music_api_artist_post(body):  # noqa: E501
    artist_name = None
    artist_id = None

    try:
        if 'name' in body['artist']:
            artist_name = body['artist']['name']
        if 'id' in body['artist']:
            artist_id = body['artist']['id'] 
    except Exception as ex:
        return "Corrupted Input Payload " + str(ex)
    
    if artist_name is None and artist_id is None:
        return "Corrupted Input Payload. Neither artist name nor id is specified"

    try:
        mb.set_useragent("demo music app", "0.1")

        if artist_name is not None and artist_id is not None:
            artists = get_artists(artist_name)
            if artist_id in [artist['id'] for artist in artists]:
                return get_releases(artist_id)
            else:
                return "artist name does not match artist id"

        if artist_name is not None:
            artists = get_artists(artist_name)
            if len(artists) > 1000:
                return artists
            else:
                return get_releases(artists[0]['id'])

        if artist_id is not None:
            return get_releases(artist_id)
        

    except Exception as ex:
        return "Processing error: " + str(ex)


def get_artists(artist_name: str):
    artists = mb.search_artists(artist_name)['artist-list']
    artists_info = []

    for artist in artists:
        artist_info = {}
        if 'name' in artist:
            artist_info['name'] = artist['name']
        if 'type' in artist:
            artist_info['type'] = artist['type']
        if 'gender' in artist:
            artist_info['gender'] = artist['gender']
        if 'area' in artist:
            artist_info['area'] = artist['area']['name']
        if 'id' in artist:
            artist_info['id'] = artist['id']

        artists_info.append(artist_info)

    return artists_info

def get_releases(artist_id: str):
    albums = mb.browse_releases(artist_id, includes=['recordings'])['release-list']
    albums_info = []
    for album in albums: 
        album_info = {}
        if 'title' in album:
            album_info['title'] = album['title']
        if 'status' in album:
            album_info['status'] = album['status']
        if 'date' in album:
            album_info['date'] = album['date']
        if 'country' in album:
            album_info['country'] = album['country']

        albums_info.append(album_info) 
    
    return albums_info


ret = music_api_artist_post({ "artist": { "name": "Pink Floydssss", "id": "83d91898-7763-47d7-b03b-b92132375c47"}})
print(ret)
