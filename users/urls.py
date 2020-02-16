from django.urls import include, path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/v1/users/',views.UsersAll.as_view()),
    path('api/v1/users/<int:id>/', views.UserDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)