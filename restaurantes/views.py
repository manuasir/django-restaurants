from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from django.conf import settings
import tweepy
import pymongo
from bson.json_util import dumps
import json
from bson.objectid import ObjectId
client = settings.CLIENT.test_database
db = client.restdb

# Consumer keys and access tokens, used for OAuth
consumer_key = '6vkYF2VfmOOGCmwWM9QrIxFuG'
consumer_secret = 'vGehBnoPY3llI3RUzeq33UEMAbZs2nPVMZkGplr8e4HrbP74j3'
access_token = '3060608854-U0UnxBnXN8fWxo8cJ1w9z2YbWKkbrozFDIeeo7k'
access_token_secret = 'd17lGcO3qpCvMvvzPMTJ1GWeXiHOdXOq27zYTeK3UuKFZ'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Creation of the actual interface, using authentication
api = tweepy.API(auth)


# Create your views here.
@csrf_exempt
def index(request):
	return render(request,'restaurantes/home.html',{})

@csrf_exempt
def home(request):
	return render(request,'restaurantes/home.html',{})

@csrf_exempt
@login_required(login_url='/accounts/login/')
def restaurantes(request):
	return render(request,'restaurantes/restaurantes.html',{})

@csrf_exempt
@login_required(login_url='/accounts/login/')
def getrestaurantes(request):
	restaurantes = db.restaurantes
	print "GET RESTAURANTES"
	if request.META['HTTP_DESPLAZAMIENTO']:
		desplazamiento = request.META['HTTP_DESPLAZAMIENTO']
		print desplazamiento
	else:
		desplazamiento = 0
	restaurante_id = restaurantes.find().sort('$natural', pymongo.ASCENDING).limit(3).skip(int(desplazamiento))

	#restaurante_id = restaurantes.find()
	return HttpResponse(dumps(restaurante_id))	

@csrf_exempt
@login_required(login_url='/accounts/login/')
def addrestaurantes(request):
	restaurantes = db.restaurantes
	cp = request.POST.get("cp",'')
	nombre = request.POST.get("nombre",'')
	direccion = request.POST.get("direccion",'')
	restaurante_id = restaurantes.insert({'nombre': nombre, 'direccion': direccion , 'cp': cp, 'puntuacion':5})
	return HttpResponse(dumps(restaurante_id))	

@csrf_exempt
@login_required(login_url='/accounts/login/')
def getinfo(request):
	restaurantes = db.restaurantes
	myid = request.META["HTTP_ID"]
	restaurante_id = restaurantes.find({'_id': ObjectId(myid)})
	#print restaurante_id
	return HttpResponse(dumps(restaurante_id))

@csrf_exempt
@login_required(login_url='/accounts/login/')
def getallrestaurantes(request):
	restaurantes = db.restaurantes
	print "GET ALL RESTAURANTES"
	restaurante_id = restaurantes.find()
	print restaurante_id
	return HttpResponse(dumps(restaurante_id))

@csrf_exempt
@login_required(login_url='/accounts/login/')
def gettweets(request):
	print "GET TWEETS"
	if 'HTTP_QUERY' in request.META:
		qu = str(request.META['HTTP_QUERY'])
	else:
		qu = 'restaurantes granada'
	tt=tweepy.Cursor(api.search, q = qu).items(5)
	dic = {'textos': []}
	for t in tt:
	    dic["textos"].append(t.text);
	    print "---"
	return HttpResponse(dumps(dic))

@csrf_exempt
@login_required(login_url='/accounts/login/')
def puntuarestaurante(request):
	restaurantes = db.restaurantes
	puntuaciones = db.puntuaciones
	myid = request.POST.get("id",'')
	puntos = request.POST.get("puntos",'')
	restaurante_id = {}
	print "puntua"
	print myid
	print int(puntos)
	
	#direccion = request.form['direccion']
	puntuacion_id = puntuaciones.insert( {'puntuacion': int(puntos) ,'idRestaurante': ObjectId(myid)})
	#restaurante_id = restaurantes.update_one({'_id': ObjectId(myid),{'$inc': {'puntuacion': int(puntos)}}})
	 #puntuacion_id = puntuaciones.insert({'idRestaurante': ObjectId(myid)},{'puntuacion'})
	if restaurante_id:
		return HttpResponse(200)
	else:
		return HttpResponse(404)