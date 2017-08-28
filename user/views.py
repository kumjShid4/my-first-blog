from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from .forms import UserCreateForm

def logout_view(request):
    """Logout"""
    logout(request)
    return HttpResponseRedirect(reverse('blog:post_list'))

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        #Display blank register form
        form = UserCreateForm()
    else:
        #Process completed form
        print(request.POST)
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            print(form.cleaned_data)

            #Log the user and redirect to homce page.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blog:post_list'))
    return render(request, 'user/register.html', {'form':form})