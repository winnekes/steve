import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

scope = "user-read-playback-state,user-modify-playback-state"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(),
                          auth_manager=spotipy.SpotifyOAuth(scope=scope))

print(spotify.devices())


def play_song(query, source="track"):
    try:
        results = spotify.search(q=query, type=source, limit=1)

        if "playlists" in results and len(results["playlists"]["items"]) > 0:
            playlist = results["playlists"]["items"][0]["uri"]
            spotify.start_playback(context_uri=playlist)
            return True, "success"

        if "tracks" in results and len(results["tracks"]["items"]) > 0:
            track = results["tracks"]["items"][0]["uri"]
            spotify.start_playback(uris=[track])
            return True, "Playing the " + source + results["playlists"]["items"][0]["name"]
    except:
        return False, "Something went wrong trying on query: " + query

