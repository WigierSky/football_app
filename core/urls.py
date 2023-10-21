from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('admin/', admin.site.urls),
    path('signup/', views.registeration_page, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('country/<str:league_id>/', views.country_league, name='country_detail'),
]
