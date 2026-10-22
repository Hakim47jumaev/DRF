from rest_framework import serializers
from .models import *

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    is_solved_by_me = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ['title','content','module','is_solved_by_me']

    def get_is_solved_by_me(self,obj):
        user = self.context.get('request').user
        return Submissions.objects.filter(user=user,task_id=obj,status='ACCEPTED').exists()

class TestCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCases
        fields = '__all__'

class SubmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submissions
        fields = '__all__'
        read_only_fields = ['user','status']