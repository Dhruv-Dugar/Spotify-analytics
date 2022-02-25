import os
import tekore as tk
from dotenv import load_dotenv

# using .env to store the credentials, and then storing in a dictionary for easy access
load_dotenv()

credentials = {
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET"),
    "redirect_uri": os.getenv("REDIRECT_URI"),
}

conf = (credentials["client_id"], credentials["client_secret"], credentials["redirect_uri"])

token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)

spotify = tk.Spotify(token)
tracks = spotify.current_user_top_tracks(limit=10)
spotify.playback_start_tracks([t.id for t in tracks.items])
