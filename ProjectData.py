import sys
import spotipy
import spotipy.util as util
import spotipy.oauth2
from spotipy import oauth2
import request

client_id='77b18607e6c846b2848a028c5a3ef84c'
client_secret='d1880189aefe4b93ad62b05382efb08f'
redirect_uri='http://localhost/'
scope = 'user-library-read'
username = '21kprilkhbiilxetgnj36g2jy'
cache_path =  '.cache-21kprilkhbiilxetgnj36g2jy'

OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'




#Authorization flow


#How to get access token
util.prompt_for_user_token(username, scope,
                           client_id,
                           client_secret,
                           redirect_uri)

token = util.oauth2.SpotifyClientCredentials(client_id, client_secret)

cache_token = token.get_access_token()
spotify = spotipy.Spotify(cache_token)

results1 = spotify.user(username)
print(results1)


results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])


results2 = spotify.artist_top_tracks(lz_uri)
for track in results2['tracks'][:10]:
    print 'track    : ' + track['name']
    print 'cover art: ' + track['album']['images'][0]['url']
    print
