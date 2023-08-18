from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm


# index
def index(request):
	return render(request, 'user/index.html', {'title': 'index'})


# register here
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST) or None
		if form.is_valid():
			form.save()
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title': 'register here'})


# login forms
def logIn(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is None:
			user = authenticate(request, email=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('api:main_page')
		else:
			form = AuthenticationForm()
			context = {
				'error_message': 'account does not exit please try again',
				'form': form,
				'title': 'log in'
			}
			return render(request, 'user/login.html', context)
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form': form, 'title': 'log in'})
