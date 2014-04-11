from django.db import models

# This import is not used but it is required for
# epydoc to be able to know about the 'date' type.
from datetime import date

class MVP(models.Model) :
    """
    This model represents the information about the Most-Valuable-Player (MVP)
    of a Super Bowl U{NFL<http://nfl.com>}.
    @ivar first_name: The first name of the MVP. (e.g. Drew)
    @type first_name: L{str}
    @ivar last_name: The last name of the MVP. (e.g. Brees)
    @type last_name: L{str}
    @ivar position: The position the MVP played that year. (e.g. QB)
    @type position: L{str}
    @ivar birth_date: The birth date of the MVP. (e.g. 1982-12-29)
    @type birth_date: L{date}
    @ivar birth_town: The town the MVP was born in. (e.g. Austin)
    @type birth_town: L{str}
    @ivar high_school: The high school the MVP attended. (e.g. Westlake High School)
    @type high_school: L{str}
    @ivar college: The college the MVP attended. (e.g. Purdue)
    @type college: L{str}
    @ivar draft_year: The year the MVP was drafted in. (e.g. 2002)
    @type draft_year: L{int}
    @ivar active: Boolean value indicating whether the MVP is still active. (e.g. True)
    @type active: L{bool}
    @ivar salary: The yearly salary for the MVP. (e.g. 2000000)
    @type salary: L{int}
    @ivar facebook_id: The unique value that is needed to embed a facebook like box for
    that MVP into a page. (e.g. DB9NFL)
    @type facebook_id: L{str}
    @ivar twitter_id: the unique value that is needed to embed a twitter feed relating to
    the MVP into a page. (e.g. 934578475)
    @type twitter_id: L{str}
    @ivar youtube_id: The unique value that is needed to embed a youtube video relating to
    the MVP into a page. (e.g. 6ivghds)
    @type youtube_id: L{str}
    @ivar latitude: The latitude coordinate of the home town of the MVP. (e.g. 204.333)
    @type latitude: L{float}
    @ivar longitude: The longitude coordinate of the home town of the MVP. (e.g. 122.678)
    @type longitude: L{float}
    """
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
    youtube_id = models.CharField(max_length = 500)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Franchise(models.Model) :
    """
    This model represents information about an U{NFL<http://nfl.com>} franchise that
    has participated in a Super Bowl.
    @ivar mvps: The list of players who have won Super Bowl MVP for this franchise.
    @type mvps: L{list}
    @ivar team_name: The official name of the team. (e.g. Seattle Seahawks)
    @type team_name: L{str}
    @ivar team_city: The name of the home city for the team. (e.g. Seattle, WA)
    @type team_city: L{str}
    @ivar team_state: The name of the home state for the team. (e.g. WA)
    @type team_state: L{str}
    @ivar current_owner: The name of the current owner (or entity) of the team. (e.g. Paul Allen)
    @type current_owner: L{str}
    @ivar current_gm: The name of the current general manager of the team. (e.g. John Schneider)
    @type current_gm: L{str}
    @ivar current_head_coach: The name of the current head coach of the team. (e.g. Pete Carroll)
    @type current_head_coach: L{str}
    @ivar year_founded: The year the franchise was founded. (e.g. 1974)
    @type year_founded: L{int}
    @ivar active: Boolean indicating whether the franchise is active. (e.g. True)
    @type active: L{bool}
    @ivar home_stadium: The home stadium of the team. (e.g. CenturyLink Field)
    @type home_stadium: L{str}
    @ivar division: The division the team plays in. (e.g. NFC West)
    @type division: L{str}
    @ivar facebook_id: The unique value that is needed to embed a facebook like box relating
    to the team into a page. (e.g. Hawks)
    @type facebook_id: L{str}
    @ivar twitter_id: The unique value that is needed to embed a twitter feed relating to
    the team into a page. (e.g. 347858)
    @type twitter_id: L{str}
    @ivar youtube_id: The unique value that is needed to embed a youtube video relating to
    the team into a page. (e.g. v6k=e9)
    @type youtube_id: L{str}
    @ivar latitude: The latitude coordinate of the stadium the team plays at. (e.g. 145.70)
    @type latitude: L{float}
    @ivar longitude: The longitude coordinate of the stadium the team plays at. (e.g. 200.00)
    @type longitude: L{float}
    """
    mvps = models.ManyToManyField(MVP)
    team_name = models.CharField(max_length = 500)
    team_city = models.CharField(max_length = 500)
    team_state = models.CharField(max_length = 2)
    current_owner = models.CharField(max_length = 500)
    current_gm = models.CharField(max_length = 500)
    current_head_coach =  models.CharField(max_length = 500)
    year_founded = models.IntegerField()
    active = models.BooleanField()
    home_stadium = models.CharField(max_length = 500)
    division = models.CharField(max_length = 500)
    facebook_id = models.CharField(max_length = 500)
    twitter_id = models.CharField(max_length = 500)
    youtube_id = models.CharField(max_length = 500)
    latitude = models.FloatField()
    longitude = models.FloatField()

class SuperBowl(models.Model) :
    """
    This model represents a U{Super Bowl<http://en.wikipedia.org/wiki/Superbowl>}. Each
    instance uniquely represents a Super Bowl game in the history of the U{NFL<http://nfl.com>}.
    @ivar winning_franchise: The franchise that won the game. (e.g. Broncos)
    @type winning_franchise: L{Franchise}
    @ivar losing_franchise: The franchise that lost the game. (e.g. Panthers)
    @type losing_franchise: L{Franchise}
    @ivar mvp: The MVP for that particular Super Bowl. (e.g. Eli Manning)
    @type mvp: L{MVP}
    @ivar players: The list of notable players that participated in this Super Bowl. These
    are players that have won a Super Bowl MVP title at least once. (e.g. Eli Manning, Tom Brady)
    @type players: L{list}
    @ivar mvp_stats: The relevant statistics for MVP for that particular Super Bowl. (e.g. 5 TD)
    @type mvp_stats: L{str}
    @ivar mvp_blurb: A summary of notable accomplishments for the MVP for that particular
    Super Bowl. (e.g. Superior perfomance ...)
    @type mvp_blurb : L{str}
    @ivar winning_score: The score of the winning team. (e.g. 43)
    @type winning_score: L{int}
    @ivar losing_score: The score of the losing team. (e.g. 8)
    @type losing_score: L{int}
    @ivar venue_name: The name of the stadium that the Super Bowl was played in. (e.g. AT&T Stadium)
    @type venue_name: L{str}
    @ivar venue_city: The name of the city that the Super Bowl was played in. (e.g. Arlington)
    @type venue_city: L{str}
    @ivar venue_state: The name of the US state that the Super Bowl was played in. (e.g. TX)
    @type venue_state: L{str}
    @ivar game_day: The day the game was played. (e.g. 2014-02-02)
    @type game_day: L{date}
    @ivar attendance: The amount of people attended that particular game. (e.g. 30,000)
    @type attendance: L{int}
    @ivar game_number: The roman numeral symbol for the game. (e.g. XLVIII)
    @type game_number: L{str}
    @ivar halftime_performer: The halftime performer from that Super Bowl. (e.g. Madonna)
    @type halftime_performer: L{str}
    @ivar twitter_id: The unique value that is needed to embed a twitter feed relating to the Super
    Bowl onto a page. (e.g. 57693)
    @type twitter_id: L{str}
    @ivar youtube_id: The unique value that is needed to embed a youtube video relating to the Super
    Bowl onto a page. (e.g. gjrk6)
    @type youtube_id: L{str}
    @ivar latitude: The latitude coordinate of the stadium the game was played at. (e.g. 45.7)
    @type latitude: L{float}
    @ivar longitude: The longitude coordinate of the stadium the game was played. (e.g. 120.5)
    @type longitude: L{float}
   """
    winning_franchise = models.ForeignKey(Franchise, related_name = "superbowls_won")
    losing_franchise = models.ForeignKey(Franchise, related_name = "superbowls_lost")
    mvp = models.ForeignKey(MVP, related_name = "superbowls_awarded")
    players = models.ManyToManyField(MVP, related_name = "superbowls_participated")
    mvp_stats = models.CharField(max_length = 500)
    mvp_blurb = models.CharField(max_length = 500)
    winning_score = models.IntegerField(default = 0)
    losing_score = models.IntegerField(default = 0)
    venue_name = models.CharField(max_length = 500)
    venue_city = models.CharField(max_length = 500)
    venue_state = models.CharField(max_length = 500)
    game_day = models.DateField()
    attendance = models.IntegerField(default = 0)
    game_number = models.CharField(max_length = 500)
    halftime_performer = models.CharField(max_length = 500)
    twitter_id = models.CharField(max_length = 500)
    youtube_id = models.CharField(max_length = 500)
    latitude = models.FloatField()
    longitude = models.FloatField()
