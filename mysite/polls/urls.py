from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('question/', views.QuestionList.as_view(), name='list'),
    path('upload-question/', views.ExtQuestionCreate.as_view(), name='ExtQuestionCreate'),
    path('question/<int:question_id>/', views.QuestionDetail.as_view(), name='details'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
