from src.data_access import (
    get_user_saved_tracks,
    save_tracks_for_user,
    get_user_recently_played_tracks,
    get_album_tracks,
    start_user_playback,
    get_user_playlists
)

from src.logger import logger

import pandas as pd
import time


def filter_user_saved_tracks(oauth_token: str) -> list:
    try:
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
        logger.info('User saved tracks have been filtered successfully')
        return saved_tracks
    except Exception as error:
        logger.error(f'Error to filter user saved tracks: {error}')
        raise


def filter_tracks_for_user(oauth_token_1: str, oauth_token_2: str) -> None:
    try:
        saved_tracks = filter_user_saved_tracks(oauth_token_1)
        df_saved_tracks = pd.DataFrame(saved_tracks)
        saved_tracks_list = df_saved_tracks['items.track.id'].tolist()
        offset = 0
        while offset < len(saved_tracks_list):
            ids_list = [track for track in saved_tracks_list[offset:offset + 50]]
            ids = ",".join(ids_list)
            save_tracks_for_user(oauth_token_2, ids)
            offset += 50
        logger.info(f'Tracks for user have been saved successfully')
    except Exception as error:
        logger.error(f'Error to filter tracks for user: {error}')
        raise


def filter_user_recently_played_tracks(oauth_token: str) -> list:
    try:
        data = get_user_recently_played_tracks(oauth_token)
        df = pd.DataFrame(data)
        df = df.filter(['track'])
        df = pd.json_normalize(df.to_dict('records'))
        df = df.filter(['track.album.id', 'track.id', 'track.name'])
        df.rename(columns={'track.album.id': 'album_id', 'track.id': 'track_id', 'track.name': 'track_name'}, inplace=True)
        logger.info('Recently played tracks have been filtered successfully')
        return [track for track in df.to_dict('records')]
    except Exception as error:
        logger.error(f'Error to filter recently played tracks: {error}')
        raise


def filter_album_tracks(oauth_token: str, recent_tracks: list) -> list:
    try:
        tracks = []
        for track in recent_tracks:
            album_tracks = get_album_tracks(oauth_token, track['album_id'])
            df_album_tracks = pd.DataFrame(album_tracks)
            df_album_tracks = df_album_tracks.filter(['items'])
            df_album_tracks = pd.json_normalize(df_album_tracks.to_dict('records'))
            df_album_tracks = df_album_tracks.filter(['items.id', 'items.track_number'])
            df_album_tracks.rename(columns={'items.id': 'track_id', 'items.track_number': 'track_number'}, inplace=True)
            df_album_tracks['track_number'] = df_album_tracks['track_number'] - 1
            current_track = pd.merge(pd.DataFrame(recent_tracks), df_album_tracks, on='track_id', how='inner').to_dict('records')[0]
            tracks.append(current_track)
        logger.info('Album tracks have been filtered successfully')
        return tracks
    except Exception as error:
        logger.error(f'Error to filter album tracks: {error}')
        raise


def filter_user_playback(oauth_token: str, recent_tracks: list) -> None:
        try:
            for recent_track in reversed(recent_tracks):
                status_code = start_user_playback(oauth_token, recent_track['album_id'], recent_track['track_number'])
                if status_code == 204:
                    time.sleep(7)
            logger.info(f'Recent tracks have been played successfully')
        except Exception as error:
            logger.error(f'Error to filter user playback: {error}')
            raise


def filter_user_playlists(oauth_token: str) -> list:
    try:
        current_playlists = [None]
        saved_playlists = []
        offset = 0
        while len(current_playlists) != 0:
            data = get_user_playlists(oauth_token, offset)
            df = pd.DataFrame(data)
            df = df.filter(['items'])
            df = pd.json_normalize(df.to_dict('records'))
            df = df.filter(['items.id'])
            current_playlists = [playlist for playlist in df.to_dict('records')]
            for saved_playlist in current_playlists:
                saved_playlists.append(saved_playlist)
            offset += 50
        logger.info('User playlists have been filtered successfully')
        return saved_playlists
    except Exception as error:
        logger.error(f'Error to filter user playlists: {error}')
        raise


def filter_playlists_for_user(oauth_token_1: str, oauth_token_2: str) -> None:
    try:
        saved_playlists = filter_user_playlists(oauth_token_1)
        df_saved_playlists = pd.DataFrame(saved_playlists)
        saved_playlists_list = df_saved_playlists['items.id'].tolist()
        for playlist_id in saved_playlists_list:
            status_code = follow_playlist(oauth_token_2, playlist_id)
            if status_code == 204:
                time.sleep(2)
        logger.info(f'Playlists for user have been followed successfully')
    except Exception as error:
        logger.info(f'Error to filter playlists for user: {error}')
        raise
