
from django.urls import path
from .views import EmpList,EmpDetail,DpmntList,DpmntDetail

urlpatterns = [
    path('emp/',EmpList.as_view()),
    path('emp/<int:pk>/',EmpDetail.as_view()),
    path('dpmnt/',DpmntList.as_view()),
    path('dpmnt/<int:pk>/',DpmntDetail.as_view()),
    
]