from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import TrelloClient

@csrf_exempt
def handle_command(request, name):
	if name not in settings.SLACK_COMMANDS:
		return HttpResponse("This is not a valid command")
	if request.POST:
		text = request.POST.get('text', None)
		if text is None:
			return HttpResponse("Send in a name of the card, please.")
		resp = TrelloClient.create_card(text, name)
		if resp is None:
			return HttpResponse("Could not create card")
		return HttpResponse("Created card {}!".format(request.POST.get('text')))
	return HttpResponse("Please send a post request")