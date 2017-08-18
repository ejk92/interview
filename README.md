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

## How to run it locally in dev mode  ##

`mkdir interview_assignments`

`cd interview_assignments`

Clone repository

`git clone https://github.com/ejk92/interview.git`

Prepare virtual environment

`virtualenv .`

Activate it

`source bin/activate`

Install project dependencies

`pip install -r interview/task3/requirements.txt`

Configure local settings, by:

`cp interview/task3/spotifypy/spotifypy/settings/local_sample.py interview/task3/spotifypy/spotifypy/settings/local.py`

Edit info regarding spotify app in your `local.py`(set `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, `SPOTIFY_REDIRECT_URL`).
Also, you need to set up correct `Redirect URIs` in your spotify app, the same as `SPOTIFY_REDIRECT_URL` from `local.py`.
For development you should use `http://127.0.0.1:8000/spotify_authorize_callback/`.

At the end run Django migrations by

`cd interview/task3/spotifypy`

`python manage.py migrate`

and to run the development server

`python manage.py runserver`

