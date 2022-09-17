from django.urls import path, include
from challenges import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# bn3ml al base name lma mybash fe query set aw lw 3aiz a3ml modify
router.register('hello-viewset', views.HelloViewSet, basename='hello_viewsets')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('hello-view', views.Helloapiview.as_view()),
    path('', include(router.urls)),
]
