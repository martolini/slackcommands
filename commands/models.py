from django.db import models
import requests

class TrelloClient(object):
	listids = {
		'bug': '54dcd88be020659f6bfacf14',
		'ideas': '54d92005365133026da94f95',
		'features': '54d920076de332204a69e29d'
	}
	def_payload = {'key': '591b45c0cbfe4b611a72e7984a482b9d', 'token': 'da4de1ca6da96cc5d1253079ed822dde1f6d5411644cc424b8501e4300c70922', 'idBoard': '54d91fa3170685886defba3f'}

	@classmethod
	def create_card(cls, name, listname):
		payload = {'name': name, 'idList': cls.listids[listname]}
		payload.update(cls.def_payload)
		r = requests.post(url='https://trello.com/1/cards/', data=payload)
		if r.status_code == 200:
			return r
		else:
			return None


