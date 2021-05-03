from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from library.views import AuthorModelViewSets
from users.views import UserModelViewSet
from to_do.views import ProjectModelViewSet, TodoModelViewSet


router = DefaultRouter()
router.register('authors', AuthorModelViewSets)
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

]
