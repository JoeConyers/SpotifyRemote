from django.shortcuts import render_to_response
from django.template import RequestContext
import sys
from appscript import *
from spotipy import Spotipy
from django.http import HttpResponse
import datetime
import os

spotify = Spotipy()

def home(request):
	
	try:
		track_name = app(u'Spotify').current_track.name.get()
	except:
		track_name = ''	
	try:	
	  artist_name = app(u'Spotify').current_track.artist.get()
	except:
	  artist_name = ''
	
	try:
		track_time = app(u'Spotify').player_position.get()
		track_time = "%02d:%02d" % divmod(track_time, 60)
	except:
		track_time = '0:00'
	
	return render_to_response('localspotifyclient/index.html', {'TrackName': track_name, 'ArtistName' : artist_name, 'TrackTime' : track_time })
	
def playpause(request):
	spotify.play_pause()
	return render_to_response('localspotifyclient/index.html')

def next(request):
	spotify.next()
	return render_to_response('localspotifyclient/index.html')

def previous(request):
	spotify.previous()
	return render_to_response('localspotifyclient/index.html')	
	
def shuffle(request):
	spotify.shuffle()
	return render_to_response('localspotifyclient/index.html')
		
def volumeup(request):
	spotify.volume_up()
	return render_to_response('localspotifyclient/index.html')
		
def volumedown(request):
	spotify.volume_down()
	return render_to_response('localspotifyclient/index.html')
	
def mute(request):
	spotify.volume_down()
	spotify.volume_down()
	spotify.volume_down()
	spotify.volume_down()
	spotify.volume_down()
	spotify.volume_down()
	spotify.volume_down()
	spotify.volume_down()
	spotify.volume_down()
	spotify.volume_down()
	return render_to_response('localspotifyclient/index.html')