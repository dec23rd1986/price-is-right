from django.shortcuts import render
from .models import Game

def game_start(request):
    games = Game.objects.all().order_by('date') # grabs all records in game in db table, order by date
    return render (request, 'game/game_start.html', {'games':games})
