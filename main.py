from spotipy import Spotify

from spotify import authenticate_spotify
from songs import tui


if __name__ == '__main__':
    spotify: Spotify = authenticate_spotify()
    tui(spotify)
