from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    title = models.CharField( max_length=50)
    description = models.CharField( max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Modules(models.Model):
    title = models.CharField( max_length=50)
    description = models.CharField( max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE,related_name='modules')


class Task(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField()
    module = models.ForeignKey(Modules, on_delete=models.CASCADE,related_name='tasks')


class TestCases(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,related_name='testcases')
    input = models.CharField( max_length=50)
    output = models.CharField( max_length=50)

class Submissions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    code = models.TextField()
    status = models.CharField(max_length=50,default='PENDING')
    created_at = models.DateTimeField( auto_now_add=True)