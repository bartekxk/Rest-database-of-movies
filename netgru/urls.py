from django.urls import include, path
from rest_framework import routers
from restapi import views

router = routers.DefaultRouter()
router.register(r'movies', views.MoviesViewSet)


urlpatterns = [
    path('^comments/(?P<Movie_ID>.+)/$', views.CommentsViewSet.as_view(), name='comments'),
    path(r'comments', views.CommentsViewSet.as_view(), name='comments'),
    path(r'comments/', views.CommentsViewSet.as_view(), name='comments'),
    path('^top/(?P<date_from>.+)/$&P<date_to>.+)/$', views.TopViewSet.as_view(), name='comments'),
    path(r'top', views.TopViewSet.as_view(), name='comments'),
    path(r'top/', views.TopViewSet.as_view(), name='comments'),
    path(r'', include(router.urls)),
]