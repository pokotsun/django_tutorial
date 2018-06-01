# coding: utf-8

from rest_framework import routers
from .views import UserViewSet, EntryViewSet, CustomUserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'custom-users', CustomUserViewSet)
router.register(r'entries', EntryViewSet)
