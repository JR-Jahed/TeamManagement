from django.contrib import admin
from .models import Team, User, UserTeam, UserTeamRequest


admin.site.register(Team)
admin.site.register(User)
admin.site.register(UserTeam)
admin.site.register(UserTeamRequest)
