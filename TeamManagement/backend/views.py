from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from backend.models import Team, User, UserTeam, UserTeamRequest
from backend.serializer import TeamSerializer, UserSerializer, UserTeamSerializer, UserTeamRequestSerializer


@api_view(['POST'])
def create_user(request):
    data = request.data

    user = User.objects.create(
        name=data['name'],
        email=data['email'],
        password=data['password'],
    )

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def login_user(request):
    data = request.data

    user = User.objects.get(email__exact=data['email'])

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['GET'])
def get_users():
    users = User.objects.all()

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def create_team(request):

    data = request.data

    user = User.objects.get(pk=data['user_id'])

    team = Team.objects.create(
        name=data['team_name'],
        category=data['team_category'],
        admin=data['user_id']
    )

    UserTeam.objects.create(
        user=user,
        team=team,
    )

    serializer = TeamSerializer(team, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def get_teams_of_user(request):
    print(request.data)

    userId = request.data["id"]

    user = User.objects.get(pk=userId)

    userTeam = UserTeam.objects.filter(user=user)

    serializer = UserTeamSerializer(userTeam, many=True)

    return Response(
        {
            "teams": serializer.data
        }
    )


@api_view(['POST'])
def get_team_details(request):

    team = Team.objects.get(pk=request.data['team_name'])

    team_serializer = TeamSerializer(team, many=False)

    members = UserTeam.objects.filter(team=team)
    members_serializer = UserTeamSerializer(members, many=True)

    members_list = []

    for member in members_serializer.data:
        user = User.objects.get(pk=member['user'])
        user_serializer = UserSerializer(user, many=False)
        members_list.append(user_serializer.data)

    return Response(
        {
            "team_name": team_serializer.data['name'],
            "team_category": team_serializer.data['category'],
            "admin": team_serializer.data['admin'],
            "members": members_list,
        }
    )


@api_view(['POST'])
def add_member_list(request):

    team = Team.objects.get(pk=request.data['team_name'])

    users = User.objects.all()

    candidate_users = []

    for user in users:
        c1 = Q(team=team)
        c2 = Q(user=user)

        res = UserTeam.objects.filter(c1 & c2)

        if len(res) == 0:
            candidate_users.append(user)

    serializer = UserSerializer(candidate_users, many=True)

    return Response(
        {
            "candidate_users": serializer.data
        }
    )


@api_view(['POST'])
def invite_user(request):

    user = User.objects.get(pk=request.data['id'])
    team = Team.objects.get(pk=request.data['team_name'])

    userTeamRequest = UserTeamRequest.objects.create(
        user=user,
        team=team,
    )

    serializer = UserTeamRequestSerializer(userTeamRequest, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def teams_invited(request):

    user = User.objects.get(pk=request.data['id'])

    userTeamRequest = UserTeamRequest.objects.filter(user=user)

    serializer = UserTeamRequestSerializer(userTeamRequest, many=True)

    return Response(
        {
            "teams": serializer.data
        }
    )


@api_view(['POST'])
def accept_invitation(request):
    user = User.objects.get(pk=request.data['id'])
    team = Team.objects.get(pk=request.data['team_name'])

    c1 = Q(team=team)
    c2 = Q(user=user)

    UserTeamRequest.objects.filter(c1 & c2).delete()
    UserTeam.objects.create(
        user=user,
        team=team,
    )

    userTeamRequest = UserTeamRequest.objects.filter(user=user)
    serializer = UserTeamRequestSerializer(userTeamRequest, many=True)
    return Response(
        {
            "teams": serializer.data
        }
    )


@api_view(['POST'])
def decline_invitation(request):
    user = User.objects.get(pk=request.data['id'])
    team = Team.objects.get(pk=request.data['team_name'])

    c1 = Q(team=team)
    c2 = Q(user=user)

    UserTeamRequest.objects.filter(c1 & c2).delete()

    userTeamRequest = UserTeamRequest.objects.filter(user=user)
    serializer = UserTeamRequestSerializer(userTeamRequest, many=True)
    return Response(
        {
            "teams": serializer.data
        }
    )











