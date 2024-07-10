from django.urls import path
from wordgame.views import home
urlpatterns = [
	path('', home),]