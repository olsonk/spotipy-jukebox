from sense_hat import SenseHat
from random import randint

import spotipy
import spotipy.util as util

import vlc

import spotipycreds
SPOTIPY_CLIENT_ID = spotipycreds.SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET = spotipycreds.SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI = spotipycreds.SPOTIPY_REDIRECT_URI

scope = 'playlist-modify-public'
token = util.prompt_for_user_token('olsonk', scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(auth=token)

sense = SenseHat()

search = input("Name a genre: ")
num_results = 20

result = sp.search(q='genre:'+search, limit=num_results)

for i, t in enumerate(result['tracks']['items']):
    print(" ", i+1, t['artists'][0]['name'], "-", t['name'], "(", t['album']['name'], ")")

print("\n\nChoosing random track...\n\n")
rand = randint(0, num_results-1)
rand_track = result['tracks']['items'][rand]
while rand_track['explicit']:
    rand = randint(0, num_results-1)
    rand_track = result['tracks']['items'][rand]
rand_track_uri = [rand_track['uri']]
print(rand_track['artists'][0]['name'], '-', rand_track['name'])
print("This track is explicit: ", rand_track['explicit'])

print("Adding to Spotipy collab playlist...")
pl_id = '5akLeMXmd3bMgmGdwunZ5e'
done = sp.user_playlist_add_tracks('olsonk', pl_id, rand_track_uri)
print("Track added.")

print("Previewing track...")
sample = vlc.MediaPlayer(rand_track['preview_url'])
sample.play()
sense.show_message(rand_track['artists'][0]['name'] + ' - ' + rand_track['name'])
