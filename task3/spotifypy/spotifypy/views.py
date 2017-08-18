# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.shortcuts import redirect

from .utils import SpotifyCaller
from .forms import SpotifySearchForm


def index(request):
    """Main page"""
    data = SpotifyCaller.me(user_session=request.session)
    spotify_search_form = SpotifySearchForm()
    return TemplateResponse(request, 'index.html', {'data': data, 'search_form': spotify_search_form})


def spotify_authorize_callback(request):
    """Spotify callback handler"""
    code = request.GET.get('code')
    SpotifyCaller.get_access_token(user_session=request.session, code=code)
    return TemplateResponse(request, 'spotify_callback.html', {})


def spotify_login(request):
    """Login(Authorize) view"""
    url = SpotifyCaller.get_authorize_user_url()
    return redirect(url)


def spotify_logout(request):
    """Logout view"""
    if 'token' in request.session.keys():
        del request.session['token']
    return redirect('index')


def search(request):
    """Searching by ajax requests"""
    query_string = request.GET.get('query')
    kind = request.GET.get('kind')
    if query_string:
        data = SpotifyCaller.search(user_session=request.session, query_string=query_string)
        table_rows = [{'name': item['name'], 'link': item['external_urls']['spotify']} for item in data[kind]['items']]
    else:
        table_rows = list()
    response = {
        'headers': ['Name', 'Link'],
        'rows': table_rows
    }
    return JsonResponse(response)
