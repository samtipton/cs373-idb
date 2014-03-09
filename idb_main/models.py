from django.db import models 
  
class Game(models.Model) : 
    winning_team = models.CharField(max_length=200) 
    losing_team  = models.CharField(max_length=200) 
    venue        = models.CharField(max_length=200) 
    score        = models.CharField(max_length=200) 
    game_number  = models.CharField(max_length=200) 
    attendance   = models.IntegerField(default = 0) 
    game_day         = models.DateTimeField('game day') 
  
    def __str__ (self) : 
        return "SuperBowl " + self.game_number 
  
class Team(models.Model) : 
  
    game       = models.ForeignKey(Game) 
  
    team_name  = models.CharField(max_length=200) 
    team_city  = models.CharField(max_length=200) 
    coach_name = models.CharField(max_length=200) 
    num_wins   = models.IntegerField(default = 0) 
      
  
    def __str__ (self) : 
        return self.team_name 
  
class Player(models.Model) : 
  
    team       = models.ForeignKey(Team) 
  
    first_name = models.CharField(max_length=200) 
    last_name  = models.CharField(max_length=200) 
    position   = models.CharField(max_length=200) 
    number     = models.IntegerField(default = 0) 
  
    def __str__ (self) : 
        return self.first_name + " " + self.last_name