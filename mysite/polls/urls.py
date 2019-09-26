from django.urls import path

from . import views




app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path(r'question/', views.QuestionList.as_view(), name = 'list'),
    path(r'question/<int:question_id>', views.QuestionDetail.as_view(), name = 'details'),
    #path(r'choice/', views.ChoiceList.as_view(), name = 'list'),
    #path(r'choice/<int:question_id>', views.ChoiceDetail.as_view(), name = 'details'),
    # ex: /polls/5/
    path('<int:question_id>/', views.ChoiceDetail.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
