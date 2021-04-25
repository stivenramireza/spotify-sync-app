from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from src.model import Account
from src.logger import logger
from src.filters import (
    filter_tracks_for_user,
    filter_user_recently_played_tracks,
    filter_album_tracks,
    filter_user_playback
)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def synchronize(request: Request) -> object:
    return templates.TemplateResponse('spotify_sync.html', {"request": request})


@app.post("/synchronize")
def synchronize_accounts(request: Request, account: Account = Depends(Account.as_form)) -> object:
    try:
        filter_tracks_for_user(account.oauth_token_1, account.oauth_token_2)
        recent_tracks = filter_user_recently_played_tracks(account.oauth_token_1)
        recent_tracks = filter_album_tracks(account.oauth_token_1, recent_tracks)
        filter_user_playback(account.oauth_token_2, recent_tracks)
        return templates.TemplateResponse('success_spotify_sync.html', {"request": request})
    except Exception as error:
        logger.error(f'Error to synchronize accounts: {error}')
        return templates.TemplateResponse('error_spotify_sync.html', {"request": request})
