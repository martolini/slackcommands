from django.conf.urls import include, url

from django.conf import settings

urlpatterns = [
	url(r'^(?P<name>\w+)/$', 'commands.views.handle_command'),
]