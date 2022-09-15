from django.urls import path ,include
from challenges import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello_viewsets')


urlpatterns = [
    path('hello-view',views.Helloapiview.as_view()),
    path('',include(router.urls))
]
