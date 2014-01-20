from django.shortcuts import render_to_response
from django.template import Context

def index(request, template_name='game/index.html', extra_context=None):
	context = Context(Context(current_app='game'))

	if extra_context is not None:
		context.update(extra_context)

	return render_to_response(template_name, context_instance=context)

def colony(request, name, template_name='game/colony.html', extra_context=None):
	context = Context(Context(current_app='game'))

	if extra_context is not None:
		context.update(extra_context)

	return render_to_response(template_name, context_instance=context)

def map(request, template_name='game/map.html', extra_context=None):
	context = Context(Context(current_app='game'))

	if extra_context is not None:
		context.update(extra_context)

	return render_to_response(template_name, context_instance=context)
