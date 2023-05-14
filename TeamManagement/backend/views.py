from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import Team, User
from backend.serializer import TeamSerializer, UserSerializer, UserTeam


@api_view(['POST'])
def create_user(request):
    data = request.data

    print(data)

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

    print(data)

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
