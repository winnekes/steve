import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

scope = "user-read-playback-state,user-modify-playback-state"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(),
                          auth_manager=spotipy.SpotifyOAuth(scope=scope))


def get_device_id():
    devices = spotify.devices()
    print(devices)
    for device in devices["devices"]:
        if device["name"] == os.getenv("SPOTIPY_DEVICE_NAME"):
            return device["id"]


def play_song(query, source="track"):
    device_id = get_device_id()
    try:
        results = spotify.search(q=query, type=source, limit=1)

        if "playlists" in results and len(results["playlists"]["items"]) > 0:
            playlist = results["playlists"]["items"][0]["uri"]
            spotify.start_playback(device_id=device_id, context_uri=playlist)
            return True, "Playing the " + source + results["playlists"]["items"][0]["name"]

        if "tracks" in results and len(results["tracks"]["items"]) > 0:
            track = results["tracks"]["items"][0]["uri"]
            spotify.start_playback(device_id=device_id, uris=[track])
            return True, "Playing the " + source + results["tracks"]["items"][0]["name"]
    except Exception as e:
        print(e.message)
        print(e.args)
        return False, "Something went wrong trying on query: " + query
