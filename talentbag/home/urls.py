from django.conf.urls import url

from .views import *

urlpatterns = [
	
	url(r'^$', HomeView.as_view(), name="home")
	
]