from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet


class CoursesView(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class ModuleView(ModelViewSet):
    queryset = Modules.objects.all()
    serializer_class = ModulesSerializer

class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TestCasesView(ModelViewSet):
    queryset = TestCases.objects.all()
    serializer_class = TestCasesSerializer

from rest_framework.decorators import APIView
import subprocess
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

class SubmissionsView(APIView):

    @swagger_auto_schema(
        request_body=SubmissionsSerializer,
        responses={
            201: 'Created',
            400: 'Validation error' })
    def post(self,request):
        serializer = SubmissionsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task = serializer.validated_data.get('task_id')
        code = serializer.validated_data.get('code')
        user = request.user

        submission = Submissions.objects.create(user = user,code = code,task_id=task)
        test_cases = TestCases.objects.filter(task=task)

        for test in test_cases:
            result = subprocess.run(['python','-c',code],text=True,capture_output=True,input=test.input)
            if result.stdout.strip()!=test.output:
                submission.status = 'WRONG_ANSWER'
                submission.save()
                return Response({
                  'id':submission.id,
                  'code':code,
                  'input':test.input,
                  'expacted_output':test.output,
                  'yout output':result.stdout.strip(),
                  'status':submission.status  
                })
        submission.status = 'ACCEPTED'
        submission.save()
        return Response({
                          'id':submission.id,
                          'code':code,
                          'status':submission.status  
                        })





