from django.urls import path
from backend.views import create_team, create_user, login_user


urlpatterns = [
    path('create_team/', create_team),
    path('create_user/', create_user),
    path('login_user/', login_user),
]
