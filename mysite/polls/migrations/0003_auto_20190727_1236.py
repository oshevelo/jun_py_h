# Generated by Django 2.2.3 on 2019-07-27 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(),
        ),
    ]