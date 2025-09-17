from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PollViewSet

router = DefaultRouter()
router.register("polls", PollViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
