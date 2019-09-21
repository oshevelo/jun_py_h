from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Question(models.Model):
    external_id = models.CharField(max_length=1000)
    question_text = models.CharField(max_length=15, default='1')
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.question_text


class ExtQuestion(models.Model):

    external_id = models.CharField(max_length=1000)
    raw_data = models.CharField(max_length=1000)
    received_date = models.DateTimeField('received date')

    question = models.ForeignKey(
        Question, 
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    processed = models.BooleanField('processed date', default=False)
    processed_date = models.DateTimeField(
        'processed date',
        null=True,
        blank=True
    )
    processed_error = models.TextField(
        'processed error',
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{} processed {} on {}'.format(
            self.external_id, 
            self.processed,
            self.processed_date
        )


@receiver(post_save,  sender=ExtQuestion)
def process_ext_question(sender, instance, created, *args, **kwargs):
    print('#'*100)
    print(instance)
    print('#'*100)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
