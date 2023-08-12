from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import urlHashmap
from analytics.models import ShortUrlUsage
from django.contrib.auth.forms import AuthenticationForm
from user_agents import parse
from analytics.views import cronFillUrlUsageTable

import random

import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


@api_view(['GET'])
def mainPage(request):
	if request.user.is_anonymous:
		template = loader.get_template("api/main_page.html")
		context = {
		}
		return HttpResponse(template.render(context, request))
	else:
		template = loader.get_template("api/main_page_logged_in.html")
		context = {
		}
		return HttpResponse(template.render(context, request))


def makeShortUrl(request):
	if request.user.is_anonymous:
		form = AuthenticationForm()
		return render(request, 'user/login.html', {'form': form, 'title': 'log in'})
	if request.method == 'POST':
		data = request.POST['longurl']
		if not data:
			template = loader.get_template("api/get_long_url.html")
			context = {
			}
			return HttpResponse(template.render(context, request))
		try:
			pre_defined = urlHashmap.objects.get(user=request.user, longurl=data)
		except urlHashmap.DoesNotExist:
			pre_defined = None
		if pre_defined:
			template = loader.get_template("api/url_generated.html")
			context = {
				'longurl': data,
				'shorturl': "http://127.0.0.1:8000/r/" + pre_defined.shorturl
			}
			return HttpResponse(template.render(context, request))
		s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!*^$-_"
		if 'short_url_suggest' in request.POST:
			if request.POST['short_url_suggest']:
				shorturl = request.POST['short_url_suggest']
				while urlHashmap.objects.filter(shorturl=shorturl).exists():
					shorturl = shorturl + '$'
		else:
			while True:
				shorturl = ''.join(random.sample(s, 6))
				if not urlHashmap.objects.filter(shorturl=shorturl).exists():
					break
		urlHashmap.objects.create(
			user=request.user,
			longurl=data,
			shorturl=shorturl,
		)

		template = loader.get_template("api/url_generated.html")
		context = {
			'longurl': data,
			'shorturl': "http://127.0.0.1:8000/r/" + shorturl
		}
		return HttpResponse(template.render(context, request))
	else:
		template = loader.get_template("api/get_long_url.html")
		context = {
		}
		return HttpResponse(template.render(context, request))


def redirection(request, shorturl):

	user_agent = parse(request.META['HTTP_USER_AGENT'])
	longurl = redis_client.get(shorturl)
	if longurl is not None:
		ShortUrlUsage.objects.create(
			shorturl=shorturl,
			csrf_token=request.COOKIES['csrftoken'] if 'csrftoken' in request.COOKIES else 'anonymous',
			device='mobile' if user_agent.is_mobile else 'pc',
			browser=user_agent.browser.family,
		)
		return redirect(longurl)

	try:
		obj = urlHashmap.objects.get(shorturl=shorturl)
	except urlHashmap.DoesNotExist:
		obj = None

	if obj is not None:
		redis_client.set(shorturl, obj.longurl)
		ShortUrlUsage.objects.create(
			shorturl=shorturl,
			csrf_token=request.META.get('CSRF_COOKIE') or 'anonymous',
			device='mobile' if user_agent.is_mobile else 'pc',
			browser=user_agent.browser.family,
		)
		return redirect(obj.longurl)
	else:
		template = loader.get_template("api/wrong_short_url.html")
		return HttpResponse(template.render({}, request))
# raise Http404("Short URL does not exist")
