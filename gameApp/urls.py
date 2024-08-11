from django.urls import path
from .views import game_view, submit_score

app_name = 'gameApp'

urlpatterns = [
    path('', game_view, name='game'),
    path('submit/', submit_score, name='submit_score'),
]
