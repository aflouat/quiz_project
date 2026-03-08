# quiz_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('results/', views.results_view, name='results'),
    path('create_sample/', views.create_sample_questions, name='create_sample'),
]
