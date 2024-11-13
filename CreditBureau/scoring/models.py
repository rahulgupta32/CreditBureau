

# # Create your models here.

from django.db import models
# from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=255)
    score_a = models.IntegerField(default = 0)
    score_b = models.IntegerField(default = 0)
    score_c = models.IntegerField(default = 0)
    score_d = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.text
    
# class Question(models.Model):
#     text = models.CharField(max_length=255)
#     option_a = models.CharField(max_length=100)
#     option_b = models.CharField(max_length=100)
#     option_c = models.CharField(max_length=100)
#     option_d = models.CharField(max_length=100)

#     def __str__(self):
#         return self.text

class UserResponse(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1)

    

# scoring/models.py

# from django.db import models
# from django.contrib.auth.models import User

# class Question(models.Model):
#     text = models.TextField()
#     OPTION_CHOICES = [
#         ('A', 'Always'),
#         ('B', 'Often'),
#         ('C', 'Sometimes'),
#         ('D', 'Never'),
#     ]
#     correct_option = models.CharField(max_length=1, choices=OPTION_CHOICES, default='A')  # Default set to 'A'

#     def __str__(self):
#         return self.text

# class UserResponse(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.CharField(max_length=1, choices=Question.OPTION_CHOICES)

#     def __str__(self):
#         return f"{self.user.username} - {self.question.text} - {self.answer}"
