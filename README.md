# Spotify Sync App

FastAPI application to synchronize 2 different Spotify accounts and copy their liked and recently played tracks and playlists.

<p align="center">
<img src="https://www.trustedreviews.com/wp-content/uploads/sites/54/2018/10/Spotify_Premium_Update.jpg">
</p>

## Run app in development mode

    $ python3 -m venv spotify
    $ source spotify/bin/activate
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
    $ docker stack deploy -c stack.yml spotify --with-registry-auth
