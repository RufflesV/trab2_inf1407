
"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function viewsa
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.schemas import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view as yasg_schema_view
from rest_framework.permissions import AllowAny
from rest_framework import routers
from drf_yasg.utils import swagger_auto_schema
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView, SpectacularRedocView
from . import views

#path('games/schema', views.Games_API.as_view()),   ALL GAMES

#path('api/schema', SpectacularAPIView.as_view(), name="schema"),
#path('api/schema/docs', SpectacularSwaggerView.as_view(url_name="schema")),
urlpatterns = [
    path('list_games/<id_arg>', views.Games_API.as_view()),
    path('user/list/<id_arg>', views.User_list.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/swagger', SpectacularSwaggerView.as_view(url_name="schema"), name='swagger'),
    path('api/redoc', SpectacularRedocView.as_view(url_name="schema"), name='redoc'),
    path('login/', views.Login_api.as_view()),
    path('edit/<id_arg>', views.Edit_user.as_view()),
    path('user/<id_arg>', views.UserAPI.as_view()),
    path('game/<game>', views.Game_relation.as_view()),
    path('accounts/token-auth/', views.CustomAuthToken.as_view()),
]
