from django.db import models


class Team(models.Model):
    name = models.CharField(primary_key=True, max_length=50, blank=False, null=False)
    category = models.CharField(max_length=50, blank=False, null=False)
    admin = models.IntegerField(blank=False, null=False)


class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)


class UserTeam(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'team'], name='pk_userteam')
        ]


class UserTeamRequest(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'team'], name='pk_userteam_request')
        ]























