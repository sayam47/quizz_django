from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
# Create your views here.

import random
from quizz.models import QuizQna, UserScore

def _get_score(data):
	score = 0
	for i in range(10):
		a = eval('(data["selected_'+str(i)+'"] == data["correct_'+str(i)+'"])')
		if a:
			score += 1
	return score

@login_required
def get_questions(request):
	if request.POST:
		score = _get_score(request.POST.dict())
		user = request.user
		try:
			obj = UserScore.objects.get(user = user)
			setattr(obj, 'score', obj.score + score)
			obj.save()
		except UserScore.DoesNotExist:
			obj = Person(user = user , score = score)
			obj.save()
		return redirect('score', score = score)
	list_indexs = random.sample(range(0,50) , 10)
	objts = QuizQna.objects.all()
	print("Length : " , len(objts))
	final_objects = [objts[i] for i in list_indexs]
	context={
	'qna':final_objects,
	}
	return render(request, "questions.html" , context)

@login_required
def score(request , score):
	context = {
	'score':score
	}
	return render(request, "score.html" , context)

def leaderboard(request):
	objts = UserScore.objects.all().order_by('-score')
	context={
	'scores':objts,
	}
	return render(request, "leaderboard.html" , context)