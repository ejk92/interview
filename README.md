# interview
Job interview assignment

## Assignments info

### Task 1
To run, type in your console:
```
python task1.py
```
Screen shows results for test cases.

### Task 2
To run, type in your console:
```
python task2.py
```
Screen shows results for test cases.
Assumptions: Operators and numbers need to be separated by spaces. No validation expression.

### Task 3
Web application that uses spotify API(https://developer.spotify.com/web-api/). Allows you as authorized user to search for music.

## How to run it locally by dockerfile  ##

Move to project catalog

`cd task3/spotifypy`

In `environment.env` file set your `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET` variable (make sure there is no spaces between `=` and variable) from registered application on spotify.
Also, you need to set up correct `Redirect URIs` in your spotify app - `http://127.0.0.1:8000/spotify_authorize_callback/`

Build containter

`docker build . -t 'spotifypy_container'`

Run container

`docker run -d -p 8000:8000 --env-file ./environment.env spotifypy_container`

Server is working on address `127.0.0.1:8000`
