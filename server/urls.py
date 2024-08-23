from django.urls import path

from server import views

urlpatterns = [

    # The home page
    path('check/', views.CheckProject.as_view()),
]
