from django.conf.urls import url
from .import views

app_name = 'accounts'

urlpatterns = [
    path('', game_views.game_start, name="home"),
]
