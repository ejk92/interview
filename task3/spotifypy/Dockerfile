FROM django:python2

ADD . /spotifypy

WORKDIR /spotifypy

RUN pip install -r requirements.txt

RUN cp ./spotifypy/settings/local_example.py ./spotifypy/settings/local.py

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]