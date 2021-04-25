import requests


def get_user_saved_tracks(oauth_token: str, offset: int) -> any:
    try:
        headers = {
            'Authorization': f'Bearer {oauth_token}'
        }
        r = requests.get(f'https://api.spotify.com/v1/me/tracks?limit=50&offset={offset}', headers=headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as error:
        return f'Error to get user saved tracks: {error}'


def save_tracks_for_user(oauth_token: str, ids: str) -> any:
    try:
        headers = {
            'Authorization': f'Bearer {oauth_token}'
        }
        r = requests.put(f'https://api.spotify.com/v1/me/tracks?ids={ids}', data={}, headers=headers)
        r.raise_for_status()
        return r.status_code
    except requests.exceptions.HTTPError as error:
        return f'Error to save tracks for user: {error}'


def get_user_recently_played_tracks(oauth_token: str) -> any:
    try:
        headers = {
            'Authorization': f'Bearer {oauth_token}'
        }
        r = requests.get('https://api.spotify.com/v1/me/player/recently-played?limit=50', headers=headers)
        r.raise_for_status()
        return r.json()['items']
    except requests.exceptions.HTTPError as error:
        return f'Error to get user recently played tracks: {error}'


def get_album_tracks(oauth_token: str, album_id: int) -> any:
    try:
        headers = {
            'Authorization': f'Bearer {oauth_token}'
        }
        r = requests.get(f'https://api.spotify.com/v1/albums/{album_id}/tracks?limit=50', headers=headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as error:
        return f'Error to get album tracks: {error}'


def start_user_playback(oauth_token: str, album_id: int, track_number: int) -> any:
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {oauth_token}'
        }
        body = {
            'context_uri': f'spotify:album:{album_id}',
            'offset': {
                'position': track_number
            },
            'position_ms': 0
        }
        r = requests.put('https://api.spotify.com/v1/me/player/play', json=body, headers=headers)
        r.raise_for_status()
        return r.status_code
    except requests.exceptions.HTTPError as error:
        return f'Error to start user playback: {error}'
