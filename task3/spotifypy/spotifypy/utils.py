# -*- coding: utf-8 -*-
import urllib
import base64
import time

import requests

import settings


class SpotifyException(Exception):
    pass


class SpotifyOauthCaller(object):
    """Auxiliary structure for Spotify oauth communication"""

    @staticmethod
    def _get_auth_headers():
        """Generate autorization header for oauth requests"""

        auth_header = base64.b64encode('{}:{}'.format(settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_CLIENT_SECRET))
        return {'Authorization': 'Basic {}'.format(auth_header)}

    @staticmethod
    def get_authorize_url():
        """
        Generate authorization url.
        :return url
        """

        credentials_data = {
            'scope': 'user-read-private user-read-email',
            'response_type': 'code',
            'client_id': settings.SPOTIFY_CLIENT_ID,
            'client_secret': settings.SPOTIFY_CLIENT_SECRET,
            'redirect_uri': settings.SPOTIFY_REDIRECT_URL
        }

        url = '{}?{}'.format(settings.SPOTIFY_API_OAUTH_AUTHORIZE_URL, urllib.urlencode(credentials_data))
        return url

    @classmethod
    def get_access_token(cls, user_session, code=None):
        """
        Obtain token data.
        :param user_session -
        :param code - authorization code(first obtaining token)
        :return access token
        """

        if 'token' in user_session.keys():
            if not SpotifyOauthCaller.valid_token(user_session['token']):
                user_session['token'] = SpotifyOauthCaller.refresh_access_token(user_session['token']['refresh_token'])

            return user_session['token']['access_token']

        elif code is not None:
            credentials_data = {
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': settings.SPOTIFY_REDIRECT_URL
            }

            headers = cls._get_auth_headers()
            response = requests.post(settings.SPOTIFY_API_TOKEN_URL, headers=headers, data=credentials_data)

            if response.status_code != 200:
                raise SpotifyException(response.reason)

            user_session['token'] = response.json()
            # increase expires_token time for comparing with time.time
            user_session['token']['expires_in'] += int(time.time())
            return user_session['token']['access_token']
        else:
            return None

    @classmethod
    def refresh_access_token(cls, refresh_token):
        """Refreshing token
        :param refresh_token - token for refreshing access token
        """

        credentials_data = {
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }
        headers = cls._get_auth_headers()

        response = requests.post(
            settings.SPOTIFY_API_TOKEN_URL,
            data=credentials_data,
            headers=headers,
        )

        if response.status_code != 200:
            raise SpotifyException(response.reason)

        data = response.json()
        data['expires_in'] += int(time.time())
        if 'refresh_token' not in data:
            data['refresh_token'] = refresh_token

        return data

    @staticmethod
    def valid_token(token):
        """Check if token is still valid
        :param dict with token data
        :return True if valid else False
        """

        now = int(time.time())
        return token['expires_in'] - now > 100


class SpotifyCaller(object):
    """Auxiliary structure for Spotify communication"""

    @staticmethod
    def get_authorize_user_url():
        """Authorize user url
        :return url"""
        return SpotifyOauthCaller.get_authorize_url()

    @staticmethod
    def get_access_token(user_session, code=None):
        """Retrieve access token.
        :param user_session
        :param code
        """
        return SpotifyOauthCaller.get_access_token(user_session, code)

    @classmethod
    def _make_call(cls, url, user_session):
        """
        Communicate with Spotify API.
        :param url - API endpoint url
        :param user_session
        :return json data
        """
        access_token = cls.get_access_token(user_session)
        if access_token is None:
            return None

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(access_token)
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise SpotifyException(response.reason)

        return response.json()

    @classmethod
    def me(cls, user_session):
        """
        Get data about logged user.
        :param: user_session
        :return json with data
        """

        url = '{}{}'.format(settings.SPOTIFY_API_URL, '/me')
        json_data = cls._make_call(url, user_session)
        return json_data

    @classmethod
    def search(cls, user_session, query_string):
        """
        Searching in spotify,
        :param user_session
        :param query_string - string with query
        :return json with data
        """
        url = '{}{}?{}'.format(settings.SPOTIFY_API_URL, '/search', query_string)
        json_data = cls._make_call(url, user_session)
        return json_data
