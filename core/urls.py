from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('admin/', admin.site.urls),
    path('signup/', views.registeration_page, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('league/<str:league_id>/', views.league_view, name='league_detail'),
    path('teams/<str:team_id>/', views.teams_view, name='team_detail'),
    path('players/<str:player_id>/', views.players_view, name='player_detail'),
]
