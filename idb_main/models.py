from django.db import models 

class Team(models.Model) : 
    team_name  = models.CharField(max_length = 500) 
    team_city  = models.CharField(max_length = 500)
    owner = models.CharField(max_length = 500)

    def __str__ (self) : 
        return self.team_name 

class Player(models.Model) : 
    first_name = models.CharField(max_length = 500) 
    last_name = models.CharField(max_length = 500) 
    birth_date = models.CharField(max_length = 500) 
    birth_town = models.CharField(max_length = 500) 
    high_school = models.CharField(max_length = 500) 
    college = models.CharField(max_length = 500) 
  
    def __str__ (self) : 
        return self.first_name + " " + self.last_name

class Venue(models.Model) : 
    name = models.CharField(max_length = 500)
    address = models.CharField(max_length = 500) 
    city = models.CharField(max_length = 500) 
    state = models.CharField(max_length = 500) 
    zip = models.CharField(max_length = 500) 

    def __str__(self) : 
        return self.name    

class Game(models.Model) : 
    home_team = models.ForeignKey(Team, related_name = "home_team")
    away_team = models.ForeignKey(Team, related_name = "away_team")
    home_score = models.IntegerField(default = 0)
    away_score = models.IntegerField(default = 0)
    venue = models.ForeignKey(Venue)
    game_day = models.DateField()
    game_number = models.CharField(max_length = 500)
  
    def __str__ (self) :    
        return "SuperBowl " + self.game_number 

class Roster(models.Model) : 
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    position = models.CharField(max_length = 500)
    player_number = models.CharField(max_length = 500)
    year = models.IntegerField()

    def __str__(self) : 
        return self.team.team_name



