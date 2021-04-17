from typing import List, Dict, Any

from src.data_access import (
    get_user_saved_tracks,
    save_tracks_for_user
)

import pandas as pd


def filter_user_saved_tracks(oauth_token: str) -> List[Dict[str, Any]]:
    current_tracks = [None]
    saved_tracks = []
    offset = 0
    while len(current_tracks) != 0:
        data = get_user_saved_tracks(oauth_token, offset)
        df = pd.DataFrame(data)
        df = df.filter(['items'])
        df = pd.json_normalize(df.to_dict('records'))
        df = df.filter(['items.track.id'])
        current_tracks = [track for track in df.to_dict('records')]
        for saved_track in current_tracks:
            saved_tracks.append(saved_track)
        offset += 50
    return saved_tracks


def filter_tracks_for_user(oauth_token_1: str, oauth_token_2: str) -> None:
    saved_tracks = filter_user_saved_tracks(oauth_token_1)
    df_saved_tracks = pd.DataFrame(saved_tracks)
    saved_tracks_list = df_saved_tracks['items.track.id'].tolist()
    offset = 0
    while offset < len(saved_tracks_list):
        ids_list = [track for track in saved_tracks_list[offset:offset + 50]]
        ids = ",".join(ids_list)
        save_tracks_for_user(oauth_token_2, ids)
        offset += 50
