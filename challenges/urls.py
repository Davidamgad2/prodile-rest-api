from django.urls import path ,include
from challenges import views

urlpatterns = [
    path('hello-view',views.Helloapiview.as_view()),
]
