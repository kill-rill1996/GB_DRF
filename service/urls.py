from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from graphene_django.views import GraphQLView

from rest_framework.routers import DefaultRouter

from library.views import AuthorModelViewSet,BookModelViewSet
from users.views import UserListAPIView
from to_do.views import ProjectModelViewSet, TodoModelViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include(router.urls)),
    path('data/', include('data.urls')),
    re_path(r'^api/(?P<version>\d\.\d)/users/$', UserListAPIView.as_view()),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path("graphql/", GraphQLView.as_view(graphiql=True)),   # Для тестирования с использ-ем интерфейса (не для прод)
]
