import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# using .env to store the credentials, and then storing in a dictionary for easy access
load_dotenv()

credentials = {
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET"),
}


# Led Zeppelin spotify url
lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

# authenticate with the spotify API using our tokens and secret
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=credentials["client_id"],
                                                                              client_secret=credentials[
                                                                                  "client_secret"]))
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
