from django.db import models

# This import is not used but it is required for
# epydoc to be able to know about the 'date' type.
from datetime import date

class Game(models.Model) :
    """
    This model represents a U{superbowl<http://en.wikipedia.org/wiki/Superbowl>}. Each
    instance uniquely represents a superbowl game in the history of the
    U{NFL<http://nfl.com>}.

    @ivar winning_team: The team that won the game.
    @type winning_team: L{Team}
    @ivar losing_team: The team that lost the game.
    @type losing_team: L{Team}
    @ivar winning_score: The score of the winning team. (e.g. 43)
    @type winning_score: L{int}
    @ivar losing_score: The score of the losing team. (e.g. 8)
    @type losing_score: L{int}
    @ivar venue: The venue the game was played in. (e.g. MetLife Stadium)
    @type venue: L{Venue}
    @ivar game_day: The day the was was played. (e.g. 2014-02-02)
    @type game_day: L{date}
    @ivar game_number: The roman numeral symbol for the game. (e.g. XLVIII)
    @type game_number: L{str}
    """
    #one to one field means that only one game can have one winning team
    winning_team = models.OneToOneField(Team, related_name = "winning_team")
    losing_team = models.OneToOneField(Team, related_name = "losing_team")
    mvp = models.OneToOneField(Player)
    winning_score = models.IntegerField(default = 0)
    losing_score = models.IntegerField(default = 0)
    venue = models.ForeignKey(Venue)
    game_day = models.DateField()
    game_number = models.CharField(max_length = 500)

    def __str__ (self) :
        return "SuperBowl " + self.game_number


class Team(models.Model) :
    """
    This model represents information about a team that participated in a superbowl.
    Each team instance uniquely represents that team in the history of the
    U{NFL<http://nfl.com>}.

    @ivar team_name: The official name of the team. (e.g. Seattle Seahawks)
    @type team_name: L{str}
    @ivar team_city: The name of the home city for the team. (e.g. Seattle, WA)
    @type team_city: L{str}
    @ivar owner: The name of the owner (or entity) of the team. (e.g. Paul Allen)
    @type owner: L{str}
    """
    
    team_name = models.CharField(max_length = 500)
    team_city = models.CharField(max_length = 500)
    owner = models.CharField(max_length = 500)
    sb_appearances = models.ForeignKey(Game) # like article --> reporters
    mvp_list = models.ForeignKey(Player) # like news company -- > reporters 

    def __str__ (self) :
        return self.team_name

class Player(models.Model) :
    """
    This model represents information about a player that played in a superbowl.
    Each player instance uniquely represents that player in the history of the
    U{NFL<http://nfl.com>}.

    @ivar first_name: (e.g. Peyton)
    @type first_name: L{str}
    @ivar last_name: (e.g. Manning)
    @type last_name: L{str}
    @ivar birth_date: The date when the player was born. (e.g. 1976-03-24)
    @type birth_date: L{date}
    @ivar birth_town: The town the player was born in. (e.g. New Orleans, LA)
    @type birth_town: L{str}
    @ivar high_school: The high school the player went to. (e.g. New Orleans Newman)
    @type high_school: L{str}
    @ivar college: The college the player went to. (e.g. University of Tennessee)
    @type college: L{str}
    @ivar draft_year: The year the player was drafted. (e.g. 1998)
    @type draft_year: L{int}
    @ivar retired: Is the player retired?. (e.g. False)
    @type retired: L{bool}
    """
    first_name = models.CharField(max_length = 500)
    last_name = models.CharField(max_length = 500)
    teams = models.ForeignKey(Team) # will relate back to team (parent relation)
    sb_appearances = models.ForeignKey(Game) # will relate back to SB (parent relation)
    birth_date = models.DateField()
    birth_town = models.CharField(max_length = 500)
    high_school = models.CharField(max_length = 500)
    college = models.CharField(max_length = 500)
    draft_year = models.IntegerField()
    retired = models.BooleanField()

    def __str__ (self) :
        return self.first_name + " " + self.last_name

class Venue(models.Model) :
    """
    This model represents the stadium where a superbowl took place. Each venue
    instance uniquely represents it in the history of the U{NFL<http://nfl.com>}.

    @ivar name: The offical name of the stadium. (e.g. Lucas Oil Stadium)
    @type name: L{str}
    @ivar address: The street address of the statidum. (e.g. 500 S Capitol Ave)
    @type address: L{str}
    @ivar city: The city the stadium is located in. (e.g. Indianapolis)
    @type city: L{str}
    @ivar state: The state the stadium is located in. (e.g. IN)
    @type state: L{str}
    @ivar zip_code: The zip code of the area the statudium is in. (e.g. 46225)
    @type zip_code: L{str}
    """
    name = models.CharField(max_length = 500)
    address = models.CharField(max_length = 500)
    city = models.CharField(max_length = 500)
    state = models.CharField(max_length = 2)
    zip_code = models.CharField(max_length = 15)

    def __str__(self) :
        return self.name



class Roster(models.Model) :
    """
    This model represents the relationship between a L{Player} and a L{Team}. Each
    instance represents information about that player for a specific L{year<Roster.year>}
    with a team.

    @ivar player: The player.
    @type player: L{Player}
    @ivar team: The team.
    @type team: L{Team}
    @ivar position: The position the player was assigned that year. (e.g. QB)
    @type position: L{str}
    @ivar player_number: The t-shirt number the player wore that year. (e.g. 18)
    @type player_number: L{str}
    @ivar year: The year number that this roster entry is representing. (e.g. 2013)
    @type year: L{int}
    """
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    position = models.CharField(max_length = 500)
    player_number = models.CharField(max_length = 500)
    year = models.IntegerField()

    def __str__(self) :
        return self.team.team_name
