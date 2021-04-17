# Spotify Sync App

FastAPI application to synchronize 2 different Spotify accounts and copy their liked songs, followed playlists and own playlists.

<p align="center">
<img src="https://www.trustedreviews.com/wp-content/uploads/sites/54/2018/10/Spotify_Premium_Update.jpg">
</p>

## Run app in development mode

    $ pip install -r requirements.txt
    $ export PYTHON_ENV=development
    $ uvicorn src.main:app --reload

## Run app in production mode with Docker Compose

    $ docker build -t stivenramireza/spotify-sync:latest .
    $ docker push stivenramireza/spotify-sync:latest
	$ docker-compose up -d

## Run app in production mode with Docker Swarm + Traefik

    $ docker build -t stivenramireza/spotify-sync:latest .
    $ docker push stivenramireza/spotify-sync:latest
	$ export DOMAIN=<DOMAIN>
    $ docker stack deploy -c stack.yml production --with-registry-auth