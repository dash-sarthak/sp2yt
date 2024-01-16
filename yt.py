from ytmusicapi import YTMusic
yt_music = YTMusic("oauth.json")


def create_playlist(title: str, tracks: list):
    playlist_id = yt_music.create_playlist(
        title, f"{title} imported from spotify")
    print(f"\t> Creating '{title}' playlist on YoutubeMusic")
    for track in tracks:
        search_results = yt_music.search(track)
        try:
            yt_music.add_playlist_items(
                playlist_id, [search_results[0]['videoId']])
        except Exception:
            print(f"\t\t -- Could not add {track}")
