from django.urls import path, include
from challenges import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# bn3ml al base name lma mybash fe query set aw lw 3aiz a3ml modify by3rfo mn al model ali at3mlo asign
router.register('hello-viewset', views.HelloViewSet, basename='hello_viewsets')
router.register('profile', views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)



urlpatterns = [
    path('hello-view', views.Helloapiview.as_view()),
    path('login/',views.userloginapiview.as_view()),
    path('', include(router.urls)),
]
