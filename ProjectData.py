import sys
import spotipy
import spotipy.util as util
import spotipy.oauth2


client_id='77b18607e6c846b2848a028c5a3ef84c'
client_secret='d1880189aefe4b93ad62b05382efb08f'
redirect_uri='http://localhost/'
scope = 'user-library-read'
username = '21kprilkhbiilxetgnj36g2jy'
cache_path =  '.cache-21kprilkhbiilxetgnj36g2jy'
playlist1950uri = 'spotify:user:spotify:playlist:2PE0DbAlT8ZFiiYaCsCm4Q'
playlistLength = 0

user = playlist1950uri.split(':')[2]
playlist_id = playlist1950uri.split(':')[4]

OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need your username!")
    print("usage: python featured_playlists.py [username]")
    sys.exit()
#Length = 1
#print(sys.argv) #Prints name of file
#Authorization flow


#How to get access token
#firstToken = util.prompt_for_user_token(username, scope,
#                           client_id,
#                            client_secret,
#                            redirect_uri)

token = util.oauth2.SpotifyClientCredentials(client_id, client_secret)
#print("token: ", token.get_access_token())

cache_token = token.get_access_token()

print("token: ", cache_token)

sp = spotipy.Spotify(cache_token)


def get_artist(name):
    results1 = sp.search(q='artist:' + name, type='artist')


#def show_artist_albums(id):
    #def get_playlist_tracks

if token:

    results = sp.user_playlist_tracks(user, playlist_id) #Returns all playlist info
    #KeyError
    tracks = results['items']


    listofCoverArt = []
    listofArtists = []
    listofAlbums = []
    #playlistLength = 0

    for track in tracks:
        playlistLength += 1

    print(playlistLength)

    #print(tracks[0])
    i = 0                           #Possibly done
    while (i < playlistLength):     #TODO: Find length of playlist based on tracks, not amount of items
        print(results['items'][i]['track']['album']['images'][0]['url'])
        name = results['items'][i]['track']['album']['artists'][0]['name']  #['name'][0]
        album = results['items'][]  #TODO
        i += 1
        name.append(name)
    #print(tracks[0]['track']['album']['images'][0]['url']) #Prints url for first track
    #print(results['items'][6]['track']['album']['images'][0]['url']) #url for cover art

    #TODO: Get genre of each album
    genreList = []
    #name =


    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    #print(tracks)

#There is no way to get a playlist's albums directly from the playlist
#Must loop through each track and get album
#Consider "repeat" albums

#First, go through tracks of a given playlist and retrieve cover art


