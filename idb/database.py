#!/usr/bin/env python

from idb.models import MVP, Franchise, SuperBowl

def reset_database():
    """ This helper function drops the data and refills it. """
    
    def m(*vals):
        """ This is a helper function to build and save an MVP object. """
        columns = ("first_name","last_name","position","birth_date","birth_town","high_school","college","draft_year","active","salary","facebook_id","twitter_id","youtube_id","latitude","longitude")
        mvp = MVP(**dict(zip(columns, vals)))
        mvp.save()
        return mvp

    def f(mvps, *vals):
        """ This is a helper function to build and save a Franchise object. """
        columns = ("team_name","team_city","team_state","current_owner","current_gm","current_head_coach","year_founded","active","home_stadium","division","facebook_id","twitter_id","youtube_id","latitude","longitude")
        franchise = Franchise(**dict(zip(columns, vals)))
        franchise.save()
        franchise.mvps.add(*mvps)
        return franchise

    def s(winner, loser, mvp, *vals):
        """ This is a helper function to build and save a Super Bowl object. """
        columns = ("mvp_stats","winning_score","losing_score","venue_name","venue_city","venue_state","game_day","attendance","game_number","halftime_performer","twitter_id","youtube_id","latitude","longitude","mvp_blurb")
        superbowl = SuperBowl(**dict(zip(columns, vals)))
        superbowl.winning_franchise = winner
        superbowl.losing_franchise = loser
        superbowl.mvp = mvp
        superbowl.save()
        return superbowl
    
    MVP.objects.all().delete()
    Franchise.objects.all().delete()
    SuperBowl.objects.all().delete()
    
    malcolm_smith   = m('Malcolm',  'Smith',   'OLB', '1989-07-05', 'Woodland Hills, CA', 'Woodland Hills (CA) Taft',        'Southern California', 2011, True,  465000,   'MalcSmitty',                           '446422781169651712', 'zfB8hCsHwLE', 34.1683, -118.605)
    joe_flacco      = m('Joe',      'Flacco',  'QB',  '1985-01-16', 'Audubon, NJ',        'Audubon (NJ) Audubon',            'Delaware',            2008, True,  20100000, 'JoeFlacco',                            '446422363865755648', 'fod3tDCNZ80', 39.8901, -75.0724)
    eli_manning     = m('Eli',      'Manning', 'QB',  '1981-01-03', 'New Orleans, LA',    'New Orleans (LA) Newman',         'Mississippi',         2004, True,  13000000, 'EliManning',                           '446087270404075520', 'I7vZ1dVSe6I', 29.9667, -90.05)
    aaron_rogers    = m('Aaron',    'Rodgers', 'QB',  '1983-12-02', 'Chico, CA',          'Chico (CA) Pleasant Valley',      'California',          2005, True,  900000,   'theaaronrodgers',                      '451545403163287553', 'BHvCUulipS0', 39.74,   -121.8356)
    drew_brees      = m('Drew',     'Brees',   'QB',  '1979-01-15', 'Austin, TX',         'Austin (TX) Westlake',            'Purdue',              2001, True,  9750000,  'DB9NFL',                               '451546253852037120', '6iv8WVzbXEg', 32.9825, -97.205)
    santonio_holmes = m('Santonio', 'Holmes',  'WR',  '1984-03-03', 'Belle Glade, FL',    'Belle Glade (FL) Glades Central', 'Ohio State',          2006, True,  7500000,  'santonioholmes',                       '451546782057500673', 'pNakPqb98Sk', 26.6853, -80.6714)
    peyton_manning  = m('Peyton',   'Manning', 'QB',  '1976-03-24', 'New Orleans, LA',    'New Orleans (LA) Newman',         'Tennessee',           1998, True,  18000000, 'pages/Peyton-Manning/109563725729117', '451547106910535680', 'UzZi_GuWXmk', 29.9667, -90.05)
    hines_ward      = m('Hines',    'Ward',    'WR',  '1976-03-08', 'Seoul, South Korea', 'Forest Park (GA) Forest Park',    'Georgia',             1998, False, 3000000,  'officialhinesward',                    '451547574294417409', '6KPC5SbfMLw', 37.5665, 126.978)
    deion_branch    = m('Deion',    'Branch',  'WR',  '1979-07-18', 'Albany, GA',         'Albany (GA) Monroe',              'Louisville',          2002, True,  925000,   'pages/Deion-Branch/108196942541674',   '451547753600913408', '3rCDogcKhPM', 31.5822, -84.1656)
    tom_brady       = m('Tom',      'Brady',   'QB',  '1977-08-03', 'San Mateo, CA',      'San Mateo (CA) Junipero Serra',   'Michigan',            2000, True,  2000000,  'TomBrady',                             '451547916428001280', 'X8toiXDuzn4', 37.5542, -122.3131)
    
    seahawks  = f([malcolm_smith],               'Seahawks',  'Seattle',      'WA', 'Paul Allen',              'John Schneider', 'Pete Carroll',   1974, True, 'CenturyLink Field',             'NFC West',  'Seahawks',           '446422083765956608', 'l9-NicPH-58', 47.5953, -122.3317)
    ravens    = f([joe_flacco],                  'Ravens',    'Baltimore',    'MD', 'Steve Bisciotti',         'Ozzie Newsome',  'John Harbaugh',  1996, True, 'M&T Bank Stadium',              'AFC North', 'baltimoreravens',    '446421801954852864', 'xvkYrio5JYg', 39.2781, -76.6228)
    giants    = f([eli_manning],                 'Giants',    'New York',     'NJ', 'John Mara',               'Jerry Reese',    'Tom Coughlin',   1925, True, 'MetLife Stadium',               'NFC East',  'newyorkgiants',      '446421524447117312', 'HAhCCm-_0Ig', 40.8136, -74.0744)
    packers   = f([aaron_rogers],                'Packers',   'Green Bay',    'WI', 'Green Bay Packers, Inc.', 'Ted Thompson',   'Mike McCarthy',  1919, True, 'Lambeau Field',                 'NFC North', 'Packers',            '451544186739634176', 'pr9dq6Wa8ao', 44.5014, -88.0622)
    saints    = f([drew_brees],                  'Saints',    'New Orleans',  'LA', 'Tom Benson',              'Mickey Loomis',  'Sean Payton',    1967, True, 'Mercedes-Benz Superdome',       'NFC South', 'neworleanssaints',   '451544324249882624', 'z23NV3pvrvw', 29.9508, -90.0811)
    steelers  = f([santonio_holmes, hines_ward], 'Steelers',  'Pittsburgh',   'PA', 'Dan Rooney',              'Kevin Colbert',  'Mike Tomlin',    1933, True, 'Heinz Field',                   'NFC North', 'steelers',           '451544466084478976', '4R9PUh2JoHE', 40.4467, -80.0158)
    colts     = f([peyton_manning],              'Colts',     'Indianapolis', 'IN', 'Jim Irsay',               'Ryan Grigson',   'Chuck Pagano',   1953, True, 'Lucas Oil Stadium',             'AFC South', 'colts',              '451544637786697728', '0MLKaIexSeM', 39.7601, -86.1638)
    patriots  = f([deion_branch, tom_brady],     'Patriots',  'New England',  'MA', 'Robert Kraft',            'Bill Belichick', 'Bill Belichick', 1959, True, 'Gillette Stadium',              'AFC East',  'newenglandpatriots', '451544728324939777', 'o8Bpa59pGnA', 42.0909, -71.2643)
    eagles    = f([],                            'Eagles',    'Philadelphia', 'PA', 'Jeffrey Lurie',           'Howie Roseman',  'Chip Kelly',     1933, True, 'Lincoln Financial Field',       'NFC East',  'philadelphiaeagles', '451544818934493184', '3uaF5FYGiis', 39.9008, -75.1675)
    bears     = f([],                            'Bears',     'Chicago',      'IL', 'Virginia Halas McCaskey', 'Phil Emery',     'Marc Trestman',  1919, True, 'Soldier Field',                 'NFC North', 'ChicagoBears',       '451544950295912448', 'yp6PSPu8qVg', 41.8625, -87.6167)
    cardinals = f([],                            'Cardinals', 'Arizona',      'AZ', 'Bill Bidwill',            'Steve Keim',     'Bruce Arians',   1898, True, 'University of Phoenix Stadium', 'NFC West',  'arizonacardinals',   '451545069774848000', 'WErrzXz6D7I', 33.5275, -112.2625)
    niners    = f([],                            '49ers',     'San Francisco','CA', 'Jed York',                'Trent Baalke',   'Jim Harbaugh',   1946, True, 'Levi\'s Stadium',               'NFC West',  'SANFRANCISCO49ERS',  '451545166600355840', '587Oow7Ckko', 37.4034, -121.9703)
    broncos   = f([],                            'Broncos',   'Denver',       'CO', 'Pat Bowlen',              'John Elway',     'John Fox',       1960, True, 'Sports Authority Field',        'AFC West',  'DenverBroncos',      '451545258929577984', 'HGMbmbnu2Oc', 39.7439, -105.02)
    panthers  = f([],                            'Panthers',  'Carolina',     'NC', 'Jerry Richardson',        'Dave Gettleman', 'Ron Rivera',     1993, True, 'Bank of America Stadium',       'NFC South', 'CarolinaPanthers',   '451545705941708801', 'cJlTyJletUw', 35.2258, -80.8528)
    
    sb39 = s(patriots, eagles,    deion_branch,    '11 REC 122 YDS 0 TD 12 TGTS',             24, 21, 'Alltel Stadium',                'Jacksonville',    'FL', '2005-02-06', 78125,  'XXXIX',   'Paul McCartney',                          '451548563755909120', 'b6XIln9M2CY', 30.3239, -81.6375,  'Deion Branch became the third offensive player to win the SB MVP without accounting for a touchdown. His 11 receptions tied a Super Bowl record.')
    sb40 = s(steelers, seahawks,  hines_ward,      '5 REC 123 YDS 1 TD 11 TGTS 1 CAR 18 YDS', 21, 10, 'Ford Field',                    'Detroit',         'MI', '2006-02-05', 68206,  'XL',      'The Rolling Stones',                      '451548898230677504', 'p5YA9Ah2Z1Y', 42.34,   -83.0456,  'Legendary Steeler Hines Ward lifted the Steelers to their 5th Super Bowl victory while winning his only Super Bowl MVP. Known as a ferocious blocker, Ward led the Steelers in receptions and yards, acting as a security blanket for second-year QB Ben Roethlisberger.')
    sb41 = s(colts,    bears,     peyton_manning,  '25/38 247 YDS 1 TD 1 INT 1 CAR 0 YDS',    29, 17, 'Dolphin Stadium',               'Miami Gardens',   'FL', '2007-02-04', 74512,  'XLI',     'Prince',                                  '451549050467135488', '8cVMzkCIV6E', 29.9581, -80.2389,  'Peyton Manning led the Indianapolis Colts to their second Super Bowl championship. Manning capped off a season in which he threw 31 TD and only 9 INT by throwing for 1 TD and 1 INT')
    sb42 = s(giants,   patriots,  eli_manning,     '19/34 255 YDS 2 TD 1 INT 3 CAR 4 YDS',    17, 14, 'University of Phoenix Stadium', 'Glendale',        'AZ', '2008-02-03', 71101,  'XLII',    'Tom Petty and the Heartbreakers',         '451549401190629377', '0o8XmdQ7Zjo', 33.5275, -112.2625, 'Eli Manning and the Giants upset the heavily favored Patriots on a late game heave to WR David Tyree. His 2 fourth quarter TDs lifted the Giants over the Patriots, who had yet to lose a game that season.')
    sb43 = s(steelers, cardinals, santonio_holmes, '9 REC 131 YDS 1 TD 13 TGTS',              27, 23, 'Raymond James Stadium',         'Tampa',           'FL', '2009-02-01', 70774,  'XLIII',   'Bruce Springsteen and the E Street Band', '451549592362811392', 'PzDawiYEpFU', 27.9758, -82.5033,  'Santonio Holmes game winning 6 yd TD catch resulted in the Steelers\' sixth Super Bowl championship. The catch was one of the all time greats in SB history, and was one of his nine spectacular receptions that game.')
    sb44 = s(saints,   colts,     drew_brees,      '32/39 288 YDS 2 TD 0 INT 1 CAR -1 YDS',   31, 17, 'Sun Life Stadium',              'Miami Gardens',   'FL', '2010-02-07', 74059,  'XLIV',    'The Who',                                 '451549854502637568', 'M1OIISkx9Hk', 25.9581, -80.2389,  'Four years after Hurricane Katrina devastated New Orleans, Drew Brees led the Saints to their first Super Bowl championship. His 32 completions tied Tom Brady\'s record for the most in Super Bowl history.')
    sb45 = s(packers,  steelers,  aaron_rogers,    '24/39 304 YDS 3 TD 0 INT 2 CAR -2 YDS',   31, 25, 'Cowboys Stadium',               'Arlington',       'TX', '2011-02-06', 103219, 'XLV',     'The Black Eyed Peas',                     '451550049890074624', 'bKMVg7p5rto', 32.7478, -97.0928,  'In his third year as a starter for the Green Bay Packers, Rodgers calmly led the team its fourth Super Bowl championship. His 3 TDs reminded fans of the retired Brett Favre and ensured Packers fans of success in years to come.')
    sb46 = s(giants,   patriots,  eli_manning,     '30/40 296 YDS 1 TD 0 INT 1 CAR -1 YDS',   21, 17, 'Lucas Oil Stadium',             'Indianapolis',    'IN', '2012-02-05', 68658,  'XLVI',    'Madonna',                                 '451550367377928192', '8eJapFSnICI', 39.7601, -86.1638, 'Once again, Eli Manning played spoiler to the New England Patriots and won his second SB MVP award. He started the game completing his first 9 attempts becoming the first quarterback to do so and put together a crucial drive with 3 1/2 minutes left that sealed the victory for the Giants.')
    sb47 = s(ravens,   niners,    joe_flacco,      '22/33 287 YDS 3 TD 0 INT 0 CAR 0 YDS',    34, 31, 'Mercedes-Benz Superdome',       'New Orleans',     'LA', '2013-02-03', 71024,  'XLVII',   'Beyonce',                                 '451550572752015360', 'ynQApEB4VXg', 29.9508, -90.0811,  'Joe Flacco capped his spectacular postseason with an impressive performance against a 49er defense that was considered one of the league\'s best. While all 3 TDs were in the first half, Flacco coolly converted third down after third down to hold off a late 49er surge.')
    sb48 = s(seahawks, broncos,   malcolm_smith,   '1 INT 1 FR 1 TD 9 T',                     43, 8,  'MetLife Stadium',               'East Rutherford', 'NJ', '2014-02-02', 82529,  'XLVIII',  'Bruno Mars',                              '446419923376418818', 'NbcA1UISfG0', 40.8136, -74.0744,  'Malcolm Smith was the de-facto SB MVP for a legendary Seattle defense. While he was a relative unknown at the start of the season, a game-sealing interception in the NFC Championship as well as two takeaways in the Super Bowl served as a coming out party for the young linebacker.')
    sb38 = s(patriots, panthers,  tom_brady,       '32/48 354 YDS 3 TD 1 INT 2 CAR 12 YDS',   32, 29, 'Reliant Stadium',               'Houston',         'TX', '2004-02-01', 71525,  'XXXVIII', 'Janet Jackson',                           '451553657423527936', '7CCWCWOUf',   29.6847, -95.4108,  'Tom Brady led the Patriots to victory while winning his second Super Bowl MVP. His 32 completions are the most in SB history and his 354 yds are the 5th best total in SB history.')
