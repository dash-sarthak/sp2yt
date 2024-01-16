from typing import Union

from spotipy import Spotify

from yt import create_playlist


def get_all_playlists(spotify: Spotify) -> Union[list[dict], None]:
    playlist_details = spotify.current_user_playlists()

    return playlist_details["items"]


def tui(spotify: Spotify):
    print("\n\n")
    playlists: list = get_all_playlists(spotify)
    for idx, playlist in enumerate(playlists):
        p_name: str = playlist["name"]
        tracks: int = playlist["tracks"]["total"]

        print(f"\t\t{idx + 1}. {p_name} - {tracks} tracks")

    print("\n")
    choice: int = int(input("\t> Enter playlist ID (1, 2, 3, ...): "))
    playlist_to_download: dict = playlists[choice - 1]
    get_playlist_songs(playlist_to_download["id"], playlist_to_download["name"], spotify)


def get_playlist_songs(playlist_id: str, playlist_name: str, spotify: Spotify):
    print(f"\t> Fetching tracks from {playlist_name}...")
    tracks: list[dict] = spotify.playlist_items(playlist_id)["items"]
    songs: list = []
    for track in tracks:
        name: str = track["track"]["name"]
        album: str = track["track"]["album"]["name"]
        release: str = track["track"]["album"]["release_date"].split("-")[0]
        songs.append(f"{name} - {album} ({release})")

    create_playlist(playlist_name, songs)
