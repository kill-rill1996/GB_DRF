from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from library.views import AuthorModelViewSets
from users.views import UserModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSets)
router.register('users', UserModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

]
