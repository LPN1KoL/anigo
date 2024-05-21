from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.db.models import Max
import random


# Create your views here.



def login_view(request):
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
	return render(request, 'login.html')


def logout_view(request):
	return render(request, 'logout.html')


def llog(request):
	logout(request)
	return HttpResponseRedirect('/login')


def register_view(request):
	form = RegForm()
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]
		usr = User.objects.create_user(username=username, password=password)
		usr.save()
		login(request, usr)
		return HttpResponseRedirect('/')
	return render(request, 'register.html', {'form': form})


def home(request):
	return render(request, "home.html")


def profile(request, id):
	user = get_object_or_404(User, id=id)
	if request.user.id != id:
		Not = True
	else:
		Not = False
	return render(request, 'profile.html', {'user': user, 'Not': Not})


def ani(request, id):
	anime = get_object_or_404(Anime, id=id)
	return render(request, 'anime.html', {'anime': anime})


def get_search(request):
	if request.method == "GET":
		animes = [x.to_json() for x in Anime.objects.all()]
		return JsonResponse({'animes': animes})


def rand_m(request):
	max_id = Anime.objects.all().aggregate(max_id=Max("id"))['max_id']
	while True:
		id = random.randint(1, max_id)
		anime = Anime.objects.filter(id=id)
		if anime:
			anime = Anime.objects.get(id=id)
			return HttpResponseRedirect(f'/ani/{anime.id}')

