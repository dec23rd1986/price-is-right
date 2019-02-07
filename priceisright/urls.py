from django.contrib import admin
from django.urls import path, include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from game import views as game_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/', include('game.urls')),
    path('retailPrice', include('retailPrice.urls')),
    path('about', views.about),
    path('', game_views.game_start, name="home"),
    path('', game_views.signup),
]

urlpatterns += staticfiles_urlpatterns()
