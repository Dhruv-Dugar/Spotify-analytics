# reusing the repository for the CSA Backend recruitment task

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


def search(spotify):
    print("Search for artist/song?:")
    search_term = input("Enter your search term: ")
    if search_term.lower() == "artist":
        print("Searching for artists...")
        search_type = "artist"
        artists = spotify.search(search_term, search_type, limit=10)
        print(artists)
    elif search_term.lower() == "song":
        print("Searching for songs...")
        search_type = "track"
        print("todo")

def main():
    # main function and the script entry point
    conf = (credentials["client_id"], credentials["client_secret"], credentials["redirect_uri"])
    token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)
    # making the class object
    spotify = tk.Spotify(token)
    print(f"Welcome {spotify.current_user()['display_name']}")
    print("Options:")
    print("1. Search")
    print("2. Control Playback")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        search(spotify)
    elif choice == "2":
        # playback(spotify)
        print("todo")
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        exit()


main()
