from django.contrib.auth.models import User
from rest_framework import serializers
from polls.models import Question


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'last_login')


class QuestionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)

    def get_email(self, obj):
        return obj.author.email if obj.author else ''

    class Meta:
        model = Question
        fields = ('id', 'email', 'question_text', 'description', 'pub_date', 'author')

