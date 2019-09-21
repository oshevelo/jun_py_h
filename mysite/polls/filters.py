import django_filters
#from django_filters import rest_framework as filters

from polls.models import Question
from django_filters.rest_framework import FilterSet


class PollsFilter(FilterSet):

    def filter_email(self, value):
        return qs.filter(
            Q(email__icontains=value)
        )

    def filter_question_texts(self, value ):#qs, question_texts, value):
        print('asdasd')
        return qs.filter(question_texts=value)

    question_texts = django_filters.filters.CharFilter(method='filter_question_texts')
    email = django_filters.filters.CharFilter(method='filter_email')
    def filter_queryset(self, self_request, queryset, mod):
        return super().filter_queryset(queryset)
    class Meta:
        model = Question
        fields = ['email', 'question_texts']
