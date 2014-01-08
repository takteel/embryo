from django.shortcuts import render_to_response
from django.template import Context

def index(request, template='game/index.html'):
	return render_to_response(template, context_instance=Context(current_app='game'))

def colony(request, name, template='game/colony.html'):
	return render_to_response(template, context_instance=Context(current_app='game'))

def map(request, template='game/map.html'):
	return render_to_response(template, context_instance=Context(current_app='game'))
