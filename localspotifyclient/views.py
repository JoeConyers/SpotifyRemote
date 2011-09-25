from django.shortcuts import render_to_response
from spotipy import Spotipy
from django.http import HttpResponse
spotify = Spotipy()

def home(request):
	return render_to_response('localspotifyclient/index.html')
	
def playpause(request):
	spotify.play_pause()
	html = "<html><body>Play/Pause</body></html>"
	return HttpResponse(html)

def next(request):
	spotify.next()
	html = "<html><body>Next</body></html>"
	return HttpResponse(html)

def previous(request):
	spotify.previous()
	html = "<html><body>Previous</body></html>"
	return HttpResponse(html)	
	
def shuffle(request):
		spotify.shuffle()
		html = "<html><body>Shuffle</body></html>"
		return HttpResponse(html)	
		
def shuffle(request):
		spotify.repeat()
		html = "<html><body>Repeat</body></html>"
		return HttpResponse(html)	
		
def volumeup(request):
		spotify.volume_up()
		html = "<html><body>Repeat</body></html>"
		return HttpResponse(html)
		
def volumedown(request):
		spotify.volume_down()
		html = "<html><body>Volume Down</body></html>"
		return HttpResponse(html)
		
def mute(request):
		spotify.mute()
		html = "<html><body>Mute</body></html>"
		return HttpResponse(html)		