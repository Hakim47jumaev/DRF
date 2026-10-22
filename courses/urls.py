from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
 
router.register('courses', CoursesView)
router.register('modules', ModuleView)
router.register('task', TaskView)
router.register('test-case', TestCasesView)
 

urlpatterns = [
    path('submit',SubmissionsView.as_view()),
]

urlpatterns+=(router.urls)
