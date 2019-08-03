from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializer

from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import generics


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    return HttpResponse(template.render(context, request))


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = QuestionSerializer

    def get_object(self):
        print(self.kwargs)
        obj = get_object_or_404(Question, pk=self.kwargs.get('question_id'))
        return obj


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
