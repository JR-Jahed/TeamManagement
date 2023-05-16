from django.urls import path
from backend.views import create_team, create_user, login_user, get_teams_of_user,\
    get_team_details, add_member_list, invite_user, teams_invited, accept_invitation, decline_invitation


urlpatterns = [
    path('create_team/', create_team),
    path('create_user/', create_user),
    path('login_user/', login_user),
    path('get_teams_of_user/', get_teams_of_user),
    path('get_team_details/', get_team_details),
    path('add_member_list/', add_member_list),
    path('invite_user/', invite_user),
    path('teams_invited/', teams_invited),
    path('accept_invitation/', accept_invitation),
    path('decline_invitation/', decline_invitation),
]
