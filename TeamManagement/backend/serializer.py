from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from backend.models import Team, User, UserTeam, UserTeamRequest


class TeamSerializer(ModelSerializer):
    # team = serializers.CharField(source="team.name", read_only=True)

    class Meta:
        model = Team

        fields = [
            'name',
            'category',
            'admin'
        ]


class UserSerializer(ModelSerializer):
    # user = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = User

        fields = [
            'id',
            'name',
            'email',
            'password'
        ]


class UserTeamSerializer(ModelSerializer):
    class Meta:
        model = UserTeam
        fields = '__all__'

        user = serializers.PrimaryKeyRelatedField(read_only=True)
        team = serializers.PrimaryKeyRelatedField(read_only=True)


class UserTeamRequestSerializer(ModelSerializer):
    class Meta:
        model = UserTeamRequest
        fields = '__all__'

        user = serializers.PrimaryKeyRelatedField(read_only=True)
        team = serializers.PrimaryKeyRelatedField(read_only=True)