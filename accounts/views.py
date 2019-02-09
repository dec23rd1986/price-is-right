from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    data = {'form':None, 'user_created': False}
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
          user = form.save()

          # do something with the registered user 
          #getting keyError warning from 'user_created'
          data['user_created'] = True

    else:
       form = UserCreationForm()
    data['form'] = form
    return data
    #return user to homepage
#login
#logout
