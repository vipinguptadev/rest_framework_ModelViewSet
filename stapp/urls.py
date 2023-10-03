from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .views import *
router.register('studentapi',StudentView,basename="student")


urlpatterns = [
    path('',include(router.urls)),

]