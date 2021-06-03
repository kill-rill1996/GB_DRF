from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from rest_framework.routers import DefaultRouter

from library.views import AuthorModelViewSet,BookModelViewSet
from users.views import UserModelViewSet
from to_do.views import ProjectModelViewSet, TodoModelViewSet


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include(router.urls)),
    path('data/', include('data.urls')),

]
