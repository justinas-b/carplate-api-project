# api/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view

from api import views

urlpatterns = [
    re_path('^app$', views.AppList().as_view(), name='app-list'),
    re_path('^app/get/(?P<pk>.*)$', views.AppDetails.as_view(), name='app-details'),
    re_path('^app/get/(?P<pk>.*)$', views.AppDetails.as_view(), name='app-details'),
    re_path('^app/delete/(?P<pk>.*)$', views.AppDelete.as_view(), name='app-delete'),
    re_path('^app/create$', views.AppCreate.as_view(), name='app-create'),
    re_path('^api$', views.RegistrationList.as_view(), name='registration-list'),
    path('api/<int:pk>', views.RegistrationDetail.as_view(), name='registration-detail'),
    re_path(r'^api/plate/(?P<plate>.*)/$', views.RegistrationDetailFind.as_view(), name='registration-detail-find'),
    re_path(r'^docs/', get_swagger_view(title='Car Plate API documentation'), name='api-documentation'),
    path('', views.api_root),
]

# Add URLs for static images
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
