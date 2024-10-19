from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('questions/upload-pdf/', views.upload_pdf, name='upload_pdf'),  # Upload PDF URL

]
