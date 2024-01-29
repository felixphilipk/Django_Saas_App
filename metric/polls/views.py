from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.


def detail(request,question_id):
      return HttpResponse("Your'e looking at question %s." % question_id)

def results(request,question_id):
     response = "Your'e looking at the results of question %s."
     return HttpResponse(response %question_id)

def vote(request,question_id):
     return HttpResponse("Your'e voting on question %s" % question_id)

def index(request):
     latest_questions_list = Question.objects.order_by("-pub_date")[:5]
     output = ",".join([q.question_text for q in latest_questions_list])
     return HttpResponse(output)

