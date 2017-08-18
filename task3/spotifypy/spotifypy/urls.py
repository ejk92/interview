from django.conf.urls import url
from django.contrib import admin

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^spotify_authorize_callback/', views.spotify_authorize_callback, name='spotify-authorize-callback'),
    url(r'^spotify_login/', views.spotify_login, name='spotify-login'),
    url(r'^spotify_logout/', views.spotify_logout, name='spotify-logout'),
    url(r'^search/', views.search, name='search')
]
