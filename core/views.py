from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
import requests, json


def mainpage(request):
    if request.user.is_authenticated:
        current_user = request.user.username

        context = {'current_user': current_user}

        return render(request, 'main_page.html', context)
    else:
        
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Credentials invalid!")
                return redirect('/')
        else:
            return render(request, 'main_page_login.html')
    
def registeration_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken!")
                return redirect('/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username is taken!")
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)       
                return redirect('/')
        else:
            messages.info(request, "Password Not Matching!")
            return redirect('signup')
    else:
        return render(request, "registeration_page.html")
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def country_league(request, league_id):
    if request.user.is_authenticated:
        # url = "https://api-football-v1.p.rapidapi.com/v3/standings"

        # querystring = {"season":"2023","league":str(league_id)}
        # headers = {
	    #     "X-RapidAPI-Key": "ed2ae62bb0msh62b561893e29e7fp1eb907jsn4c321d4d3a00",
	    #     "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        # }

        # response = requests.get(url, headers=headers, params=querystring)
        #data = response.json()

        with open('core\data.json', 'r') as json_file:
            data = json.load(json_file)
        
        standings = data["response"][0]["league"]["standings"]
        leagueName = data["response"][0]["league"]["name"]

        leagueData = []


        for standing in standings[0]:
            leagueData.append({
                "rank":standing["rank"],
                "name":standing["team"]["name"],
                "played":standing["all"]["played"],
                "win":standing["all"]["win"],
                "draw":standing["all"]["draw"],
                "lose":standing["all"]["lose"],
                "points":standing["points"],
            })

        context = {
            "leagueData":leagueData,
            "leagueName":leagueName
        }

        return render(request, 'country_league.html', context)
    else:
        return redirect('/')
