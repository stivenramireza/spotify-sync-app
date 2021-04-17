# Spotify Sync App

FastAPI application to synchronize 2 different Spotify accounts and copy their liked songs, followed playlists and own playlists.

<p align="center">
<img src="https://www.trustedreviews.com/wp-content/uploads/sites/54/2018/10/Spotify_Premium_Update.jpg">
</p>

## Run app in development mode

    $ pip install -r requirements.txt
    $ export PYTHON_ENV=development
    $ uvicorn src.main:app --reload

## Run app in production mode

    $ docker build -t spotify-sync-app:latest .
	$ docker-compose up -d