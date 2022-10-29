from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name= models.CharField(max_length=30)
    upload = models.FileField(upload_to='')


