from django.conf.urls import include, url
from rest_framework import routers

from notes import views

note_routers = routers.DefaultRouter()
note_routers.register(r'words', views.UserWordViewSet, base_name='user-words')

urlpatterns = [
    url(r'', include(note_routers.urls)),
]
