from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
import requests, json


option = False

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

def league_view(request, league_id):
    if request.user.is_authenticated:

        headers = {
            "X-RapidAPI-Key": "ed2ae62bb0msh62b561893e29e7fp1eb907jsn4c321d4d3a00",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        if option == True:
            url = "https://api-football-v1.p.rapidapi.com/v3/standings"

            querystring = {"season":"2023","league":str(league_id)}

            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()
        else:
            with open('core\spain.json', 'r') as json_file:
                data = json.load(json_file)
        
        standings = data["response"][0]["league"]["standings"]
        league_name = data["response"][0]["league"]["name"]

        league_data = []


        for standing in standings[0]:
            league_data.append({
                "rank":standing["rank"],
                "name":standing["team"]["name"],
                "id":standing["team"]["id"],
                "played":standing["all"]["played"],
                "win":standing["all"]["win"],
                "draw":standing["all"]["draw"],
                "lose":standing["all"]["lose"],
                "gd":standing["goalsDiff"],
                "points":standing["points"],
            })

        
        if option == True:
            url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"

            querystring = {"league":str(league_id),"season":"2023"}

            response = requests.get(url, headers=headers, params=querystring)

            data_scorers = response.json()
        else:
            with open('core\scorers.json', 'r') as json_file:
                data_scorers = json.load(json_file)

        scorers = data_scorers["response"]

        score_data = []

        for i in range(5):
            score_data.append({
                "id":scorers[i]["player"]["id"],
                "name":scorers[i]["player"]["name"],
                "goals":scorers[i]["statistics"][0]["goals"]["total"],
                "assists":scorers[i]["statistics"][0]["goals"]["assists"],
            })
            
        for item in score_data:
            if item['assists'] is None:
                item['assists'] = 0

        
        if option == True:
            url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

            querystring = {"league":str(league_id),"season":"2023"}

            response = requests.get(url, headers=headers, params=querystring)

            data_fix = response.json()
        else:
            with open(r'core\fixtures.json', 'r') as json_file:
                data_fix = json.load(json_file)

        fixtures = data_fix["response"]

        fixtures_data = []

        for fixture in fixtures:
            fixtures_data.append({
                "home_team":fixture["teams"]["home"]["name"],
                "away_team":fixture["teams"]["away"]["name"],
                "home_team_id":fixture["teams"]["home"]["id"],
                "away_team_id":fixture["teams"]["away"]["id"],
                "home_goals":fixture["goals"]["home"],
                "away_goals":fixture["goals"]["away"],
            })

        for item in fixtures_data:
            if item['home_goals'] is None:
                item['home_goals'] = "-"
            if item['away_goals'] is None:
                item['away_goals'] = "-"

        context = {
            "leagueData":league_data,
            "leagueName":league_name,
            "scoreData":score_data,
            "fixturesData":fixtures_data,
        }

        return render(request, 'country_league.html', context)
    else:
        return redirect('/')


def teams_view(request, team_id):
    if request.user.is_authenticated:
        headers = {
            "X-RapidAPI-Key": "ed2ae62bb0msh62b561893e29e7fp1eb907jsn4c321d4d3a00",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        if option == True:
            url = "https://api-football-v1.p.rapidapi.com/v3/teams"

            querystring = {"id":str(team_id)}

            response = requests.get(url, headers=headers, params=querystring)

            data_teams = response.json()
        else:
            with open(r'core\real.json', 'r') as json_file:
                data_teams = json.load(json_file)


        data_team = {
            "name":data_teams["response"][0]["team"]["name"],
            "country":data_teams["response"][0]["team"]["country"],
            "year":data_teams["response"][0]["team"]["founded"],
            "logo":data_teams["response"][0]["team"]["logo"],
            "stadium":data_teams["response"][0]["venue"]["name"],
            "capacity":data_teams["response"][0]["venue"]["name"],
        }

        if option == True:
            url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

            querystring = {"season":"2023","team":str(team_id)}

            response = requests.get(url, headers=headers, params=querystring)

            data_fix = response.json()
        else:
            with open(r'core\fixteam.json', 'r') as json_file:
                data_fix = json.load(json_file)

        fixtures = data_fix["response"]

        fixtures_data = []

        for fixture in fixtures:
            fixtures_data.append({
                "home_team":fixture["teams"]["home"]["name"],
                "away_team":fixture["teams"]["away"]["name"],
                "home_team_id":fixture["teams"]["home"]["id"],
                "away_team_id":fixture["teams"]["away"]["id"],
                "home_goals":fixture["goals"]["home"],
                "away_goals":fixture["goals"]["away"],
            })

        for item in fixtures_data:
            if item['home_goals'] is None:
                item['home_goals'] = "-"
            if item['away_goals'] is None:
                item['away_goals'] = "-"


        context = {
            "teamData":data_team,
            "fixturesData":fixtures_data,
        }

        return render(request, 'team_page.html', context)
    else:
        return redirect('/')

def players_view(request, player_id):
    if request.user.is_authenticated:
        headers = {
            "X-RapidAPI-Key": "ed2ae62bb0msh62b561893e29e7fp1eb907jsn4c321d4d3a00",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        if option == True:
            url = "https://api-football-v1.p.rapidapi.com/v3/players"

            querystring = {"id":str(player_id),"season":"2023"}


            response = requests.get(url, headers=headers, params=querystring)

            data_players = response.json()
        else:
            with open(r'core\players.json', 'r') as json_file:
                data_players = json.load(json_file)


        data_player = {
            "name":data_players["response"][0]["player"]["name"],
            "age":data_players["response"][0]["player"]["age"],
            "photo":data_players["response"][0]["player"]["photo"],
            "club":data_players["response"][0]["statistics"][0]["team"]["name"],
        }

        context = {
            "playerData":data_player           
        }

        return render(request, 'players_page.html', context)
    else:
        return redirect('/')
