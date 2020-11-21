from django.urls import path,include,re_path

from quizz.views import get_questions, leaderboard, score

urlpatterns = [
	path('questions' , get_questions , name = 'questions'),
	path('leaderboard' , leaderboard , name = 'leaderboard'),
	re_path(r'^score/(?P<score>[0-9]+)/$' , score , name = 'score'),
]