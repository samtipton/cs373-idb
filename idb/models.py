from django.db import models

# This import is not used but it is required for
# epydoc to be able to know about the 'date' type.
from datetime import date

class MVP(models.Model) :
    #information
    first_name = models.CharField(max_length = 500)
    last_name = models.CharField(max_length = 500)
    position = models.CharField(max_length = 4)
    birth_date = models.DateField()
    birth_town = models.CharField(max_length = 500)
    high_school = models.CharField(max_length = 500)
    college = models.CharField(max_length = 500)
    draft_year = models.IntegerField()
    active = models.BooleanField()
    salary = models.IntegerField()

    facebook_id = models.CharField(max_length = 500)
    twitter_id = models.CharField(max_length = 500)

    def __str__ (self) :
        return self.first_name + " " + self.last_name

class Franchise(models.Model) :
    mvp = models.ManyToManyField(MVP, verbose_name ="Most Valuable Player")
    #information
    team_name = models.CharField(max_length = 500)
    team_city = models.CharField(max_length = 500)
    team_state = models.CharField(max_length = 2)
    current_owner = models.CharField(max_length = 500)
    current_gm = models.CharField(max_length = 500)
    current_head_coach =  models.CharField(max_length = 500)
    year_founded = models.CharField(max_length = 500)
    active = models.BooleanField()
    home_stadium = models.CharField(max_length = 500)
    division = models.CharField(max_length = 500)

    facebook_id = models.CharField(max_length = 500)
    twitter_id = models.CharField(max_length = 500)

    def __str__ (self) :
        return self.team_name

class SuperBowl(models.Model) :
    winning_franchise = models.ForeignKey(Franchise, related_name = "winner")
    losing_franchise = models.ForeignKey(Franchise, related_name = "loser")
    mvp = models.ForeignKey(MVP)
    #information
    winning_score = models.IntegerField(default = 0)
    losing_score = models.IntegerField(default = 0)
    venue_name = models.CharField(max_length = 500)
    venue_city = models.CharField(max_length = 500)
    venue_state = models.CharField(max_length = 500)
    game_day = models.DateField()
    attendance = models.IntegerField(default = 0)
    game_number = models.CharField(max_length = 500)
    halftime_performer = models.CharField(max_length = 500)

    facebook_id = models.CharField(max_length = 500)
    twitter_id = models.CharField(max_length = 500)

    def __str__ (self) :
        return "SuperBowl " + self.game_number

