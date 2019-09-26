from rest_framework import serializers
from polls.models import Question
from polls.models import Choice
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text', 'votes')

class QuestionSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    choice = ChoiceSerializer()
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'author', 'choice_text', 'votes')


