from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import sys
from appscript import *
from spotipy import Spotipy
from django.http import HttpResponse
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
	return redirect('/')

def next(request):
	spotify.next()
	return redirect('/')

def previous(request):
	spotify.previous()
	return redirect('/')
	
def shuffle(request):
	spotify.shuffle()
		return redirect('/')
		
def volumeup(request):
	spotify.volume_up()
	return redirect('/')
		
def volumedown(request):
	spotify.volume_down()
	return redirect('/')
	
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
	return redirect('/')