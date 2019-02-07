from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    data = {'form':None, 'user_created': False}
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
          user = form.save()
          # do soemthing with the registered user / redirect to retailprice page
          data['user_created'] = True
    else:
       form = UserCreationForm()
    data['form'] = form
    return data
#login
#logout
