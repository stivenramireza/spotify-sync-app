from typing import Any

import requests


def get_user_saved_tracks(oauth_token: str, offset: int) -> Any:
    try:
        headers = {
            'Authorization': f'Bearer {oauth_token}'
        }
        r = requests.get(f'https://api.spotify.com/v1/me/tracks?limit=50&offset={offset}', headers=headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as error:
        return f'Error to get user saved tracks: {error}'


def save_tracks_for_user(oauth_token: str, ids: str) -> Any:
    try:
        headers = {
            'Authorization': f'Bearer {oauth_token}'
        }
        r = requests.put(f'https://api.spotify.com/v1/me/tracks?ids={ids}', data={}, headers=headers)
        r.raise_for_status()
        return r.status_code
    except requests.exceptions.HTTPError as error:
        return f'Error to save tracks for user: {error}'
