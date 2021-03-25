import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


scope = "user-read-playback-state,user-modify-playback-state"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(),
                          auth_manager=spotipy.SpotifyOAuth(scope=scope))


def play_song(query, type="track"):
    results = spotify.search(q=query, type=type, limit=1)
    print(json.dumps(results, indent=2))

    if "playlists" in results and len(results["playlists"]["items"]) > 0:
        playlist = results["playlists"]["items"][0]["uri"]
        spotify.start_playback(context_uri=playlist)
        return True, "success"

    if "tracks" in results and len(results["tracks"]["items"]) > 0:
        track = results["tracks"]["items"][0]["uri"]
        spotify.start_playback(uris=[track])
        return True, "success"

    return False, "blip"


