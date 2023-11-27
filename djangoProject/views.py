from .models import User, Game
#Swagger
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
#rest_framework
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, permissions
#outros
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .serializer import GameSerializer, UserSerializer, LoginSerializer

def convert_quotes(data):
    if isinstance(data, dict):
        return {key.replace("'", '"'): value.replace("'", '"') if isinstance(value, str) else value
                for key, value in data.items()}
    return data
class UserAPI(APIView):
    serializer_class = UserSerializer
    def get(self, request, id_arg):
        #ver dados do usuário
        queryset = User.objects.get(pk=id_arg)
        if queryset:
            serializer = UserSerializer(queryset)
            return Response(serializer.data)
        else:
            return Response({'msg': f'Não existe esse usário'}, status.HTTP_400_BAD_REQUEST)
    def post(self, request, id_arg):
        #cria novo usuário
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    def put(self, request, id_arg):
        #edita os dados do usuário
        user = User.objects.get(pk=id_arg)
        serializer = self.serializer_class(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)

        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    def delete(self,request, id_arg):
        #deleta o usuário
        user = User.objects.get(pk=id_arg)
        if user:
            user.delete()
            return Response({'usuario deletado'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': f'item [{id_arg}] não encontrado'}, status.HTTP_404_NOT_FOUND)
class Game_relation(APIView):
    serializer_class = GameSerializer
    def get(self, request, game):
        game = Game.objects.get(name=game)
        if game:
            serializer = GameSerializer(game)
            return Response(serializer.data)
        else:
            return Response({'msg': f'Não foi possível encontrar esse jogo'}, status.HTTP_400_BAD_REQUEST)
    def post(self, request, game):
        #criar novo jogo ( n linka com o usuário)
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    def put(self, request, game):
        #editar jogo
        user = Game.objects.get(name=game)
        serializer = self.serializer_class(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, game):
        #deleta o jogo
        game = Game.objects.get(name=game)
        if game:
            game.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': f'usuário não é adm'}, status.HTTP_404_NOT_FOUND)

class User_list(APIView):
    @extend_schema(
        exclude=True
    )
    def get(self, request, id_arg):
        user = User.objects.get(pk=id_arg)
        if user:
            data_games = list(user.games.all())
            data_list = []
            for i in data_games:
                game = Game.objects.get(name=i)
                data_list.append(str(game.name))
                data_list.append(str(game.developer))
            return Response(data_list,status.HTTP_201_CREATED)
        else:
            return Response({'msg': f'Não existe esse usário'}, status.HTTP_400_BAD_REQUEST)

class Login_api(APIView):
    @extend_schema(
        exclude=True
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            seri = serializer.data.get('name')
            user = User.objects.get(name=seri)
            tested_password = serializer.data.get('password')
            if user.password == tested_password:
                info_list = [str(user.id),user.name, str(user.age), user.password]
                return Response(info_list,status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
class Games_API(APIView):
    #listagem todos os jogos q n pertencem a x usuário
    @extend_schema(
        exclude=True
    )
    def get(self, request, id_arg):
        user = User.objects.get(pk=id_arg)
        user_games = list(user.games.all())
        all_games = Game.objects.all()
        return_list = []
        for i in all_games:
            if i not in user_games:
                return_list.append(str(i.name))
        return Response(return_list,status.HTTP_200_OK)

class Edit_user(APIView):
    serializer_class = UserSerializer
    @extend_schema(
        exclude=True
    )
    def put(self, request, id_arg):
    # edita os dados do usuário
        user = User.objects.get(pk=id_arg)
        serializer = self.serializer_class(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            info_list = [str(user.id), user.name, str(user.age), user.password]
            return Response(info_list, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
class CustomAuthToken(ObtainAuthToken):
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)