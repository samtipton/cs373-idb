from django.db import models

class Team(models.Model) :
    """
    The team model represents information about a team that participated in a superbowl.
    Each team instance uniquely represents that team in the history of the NFL.

    team_name - The official name of the team. (e.g. Seattle Seahawks)
    team_city - The name of the home city for the team. (e.g. Seattle, WA)
    owner - The name of the owner (or entity) of the team. (e.g. Paul Allen)
    """
    team_name = models.CharField(max_length = 500)
    team_city = models.CharField(max_length = 500)
    owner = models.CharField(max_length = 500)

    def __str__ (self) :
        return self.team_name

class Player(models.Model) :
    """
    The player model represents information about a player that played in a superbowl.
    Each player instance uniquely represents that player in the history of the NFL.

    first_name - (e.g. Peyton)
    last_name - (e.g. Manning)
    birth_date - The date when the player was born in ISO-8601 format. (e.g. 1976-03-24)
    birth_town - The town the player was born in. (e.g. New Orleans, LA)
    high_school - The high school the player went to. (e.g. New Orleans Newman)
    college - The college the player went to. (e.g. University of Tennessee)
    """
    first_name = models.CharField(max_length = 500)
    last_name = models.CharField(max_length = 500)
    birth_date = models.CharField(max_length = 500)
    birth_town = models.CharField(max_length = 500)
    high_school = models.CharField(max_length = 500)
    college = models.CharField(max_length = 500)

    def __str__ (self) :
        return self.first_name + " " + self.last_name

class Venue(models.Model) :
    """
    The venue model represents the stadium where a superbowl took place. Each venue
    instance uniquely represents it in the history of the NFL.

    name - The offical name of the stadium. (e.g. Lucas Oil Stadium)
    address - The street address of the statidum. (e.g. 500 S Capitol Ave)
    city - The city the stadium is located in. (e.g. Indianapolis)
    state - The state the stadium is located in. (e.g. IN)
    zip_code - The zip code of the area the statudium is in. (e.g. 46225)
    """
    name = models.CharField(max_length = 500)
    address = models.CharField(max_length = 500)
    city = models.CharField(max_length = 500)
    state = models.CharField(max_length = 2)
    zip_code = models.CharField(max_length = 15)

    def __str__(self) :
        return self.name

class Game(models.Model) :
    """
    The Game model represents a superbowl. The instance uniquely represents
    that superbowl in the history of the NFL.

    winning_team - The team that won the game.
    loosing_team - The team that lost the game.
    winning_score - The score of the winning team. (e.g. 43)
    loosing_score - The score of the loosing team. (e.g. 8)
    venue - The venue the game was played in. (e.g. MetLife Stadium)
    game_day - The day the was was played (in ISO-8601 format). (e.g. 2014-02-02)
    game_number - The roman numeral symbol for the game. (e.g. XLVIII)
    """
    winning_team = models.ForeignKey(Team, related_name = "winning_team")
    loosing_team = models.ForeignKey(Team, related_name = "loosing_team")
    winning_score = models.IntegerField(default = 0)
    loosing_score = models.IntegerField(default = 0)
    venue = models.ForeignKey(Venue)
    game_day = models.DateField()
    game_number = models.CharField(max_length = 500)

    def __str__ (self) :
        return "SuperBowl " + self.game_number

class Roster(models.Model) :
    """
    The Roster model represents the relationship between a player and a team.
    Each instance represents information about that player for a specific year
    with a team.

    player - The player.
    team - The team.
    position - The position the player was assigned that year. (e.g. QB)
    player_number - The t-shirt number the player wore that year. (e.g. 18)
    year - The year number that this roster entry is representings. (e.g. 2013)
    """
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    position = models.CharField(max_length = 500)
    player_number = models.CharField(max_length = 500)
    year = models.IntegerField()

    def __str__(self) :
        return self.team.team_name
