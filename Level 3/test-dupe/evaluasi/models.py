from django.db import models

# Create your models here.

class Questions(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_three = models.CharField(max_length=50)
    option_four = models.CharField(max_length=50)
    ans = models.CharField(max_length=50)

class Answer(models.Model):
    Name = models.CharField(max_length=50)
    question1 = models.TextField()
    option_one1 = models.CharField(max_length=50)
    option_two1 = models.CharField(max_length=50)
    option_three1 = models.CharField(max_length=50)
    option_four1 = models.CharField(max_length=50)
    ans1 = models.CharField(max_length=50)
    yourAnswer1 = models.CharField(max_length=50)
    question2 = models.TextField()
    option_one2 = models.CharField(max_length=50)
    option_two2 = models.CharField(max_length=50)
    option_three2 = models.CharField(max_length=50)
    option_four2 = models.CharField(max_length=50)
    ans2 = models.CharField(max_length=50)
    yourAnswer2 = models.CharField(max_length=50)
    def answers_id(self):
        return self.id