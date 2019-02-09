from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from accounts.views import signup
from .models import Game


def game_start(request):
    games = Game.objects.all().order_by('date')
    data = {'msg': ''}
    response = signup(request)
    if response['user_created']:
        
       # you can redirect user here to somewhere else when they have been registered.
        data['msg'] = 'Thanks for being the part of our beautiful community!'
    return render(request, 'game/game_start.html', {
                'games':games,
                'form': response['form'],
                'msg': data['msg']
    })
