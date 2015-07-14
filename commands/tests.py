from django.test import TestCase
from .models import TrelloClient

class TrelloTest(TestCase):
	def test_bug(self):
		TrelloClient.create_card('This is a test', 'bug')

