from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register('v1/groups', GroupViewSet, basename='Group')
router.register('v1/posts', PostViewSet, basename='Post')
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='Comment'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token, name='token-auth'),
    path('', include(router.urls)),

]
