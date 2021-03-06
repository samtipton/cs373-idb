#!/usr/bin/env python3

from idb.models import MVP, Franchise, SuperBowl, Analytic

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
        """ This is a helper function to build and save a SuperBowl object. """
        columns = ("mvp_stats","winning_score","losing_score","venue_name","venue_city","venue_state","game_day","attendance","game_number","halftime_performer","twitter_id","youtube_id","latitude","longitude","mvp_blurb")
        superbowl = SuperBowl(**dict(zip(columns, vals)))
        superbowl.winning_franchise = winner
        superbowl.losing_franchise = loser
        superbowl.mvp = mvp
        superbowl.save()
        return superbowl

    def a(name, query, desc):
        """ This is a helper function to build and save an Analytic object. """
        analytic = Analytic(name = name, query = query, description = desc)
        analytic.save()
        return analytic
    
    MVP.objects.all().delete()
    Franchise.objects.all().delete()
    SuperBowl.objects.all().delete()
    Analytic.objects.all().delete()

    # Super Bowl Queries
    a('Super Bowl Query', """
SELECT
    s.game_number AS "Game Number",
    s.venue_name AS "Venue",
    s.venue_city AS "City",
    s.venue_state AS "State",
    s.attendance AS "Attendance",
    s.game_day AS "Game Day"
FROM
    idb_superbowl AS s
WHERE
    (s.attendance > (SELECT
                        avg(s1.attendance)
                    FROM
                        idb_superbowl AS s1))
ORDER BY
    s.attendance ASC""",
    "A query that returns Super Bowl games that had a higher attendance than the average attendance.")
    
    a('Super Bowl Query', """
SELECT
    count(*) AS "# of Super Bowls",
    venue_name AS Venue,
    venue_city AS City,
    venue_state AS State
FROM
    idb_superbowl
GROUP BY
    venue_state,
    venue_city,
    venue_name
ORDER BY
    "# of Super Bowls" DESC""",
    'A query that counts the number of super bowls for each venue.')
    
    a('Super Bowl Query', """
SELECT
    max(t.s) AS "Max Points Scored",
    min(t.s) AS "Min Points Scored",
    avg(t.s) AS "Average Points Scored"
FROM
    (SELECT
        winning_score AS s
    FROM
        idb_superbowl
    UNION SELECT
        losing_score AS s
    FROM
        idb_superbowl) AS t""",
    'A query that returns the highest points scored, the lowest points scored, and the average points scored across all Super Bowls.')
    
    a('Super Bowl Query', """
SELECT
    s.game_number AS "Game Number",
    p.first_name AS "First Name",
    p.last_name as "Last Name"
FROM
    idb_superbowl AS s
INNER JOIN
    idb_mvp AS p
    ON s.mvp_id = p.id
ORDER BY
    s.game_number DESC""",
    "A query that returns the MVP recipient for each Super Bowl.")
    
    # Franchise Queries
    a('Franchises Query', """
SELECT
    (f.team_city || ' ' || f.team_name) AS Franchise,
    count(f.id) AS "Number of MVPs"
FROM
    idb_franchise AS f
INNER JOIN
    idb_franchise_mvps AS j
    ON j.franchise_id = f.id
GROUP BY
    f.id
ORDER BY
    "Number of MVPs" DESC""",
    'A query that returns the number of MVPs per franchise (multiple winners excluded)')
    
    a('Franchises Query', """
SELECT
    (f.team_city || ' ' || f.team_name) AS Franchise,
    (SELECT
        count(*)
    FROM
        idb_superbowl AS s
    WHERE
        s.winning_franchise_id = f.id) AS Wins,
    (SELECT
        count(*)
    FROM
        idb_superbowl AS s
    WHERE
        s.losing_franchise_id = f.id) AS Losses
FROM
    idb_franchise AS f
ORDER BY
    Wins DESC,
    Losses ASC,
    Franchise ASC""",
    'A query that returns the number of Super Bowl victories and losses for each franchise, sorted by victories.')
    
    # MVP Queries
    a('Super Bowl MVP Query', """
SELECT
    position, count(*) AS "Number of MVPs"
FROM
    idb_mvp AS p
GROUP BY
    position
ORDER BY
    "Number of MVPs" DESC""",
    "A query that returns the list of MVP award winners sorted by position.")
    
    a('Super Bowl MVP Query', """
SELECT
    position,
    count(*) AS "Number of MVPs"
FROM
    idb_mvp
GROUP BY
    position
ORDER BY
    "Number of MVPs" DESC
LIMIT 3""",
    'A query that returns the top three positions that have received the MVP award.')
    
    a('Super Bowl MVP Query', """
SELECT
    position, count(*) AS "Number of MVPs"
FROM
    idb_mvp
GROUP BY
    position
ORDER BY
    "Number of MVPs" ASC
LIMIT 3""",
    'A query that returns the bottom three positions that have received the MVP award.')
    
    a('Super Bowl MVP Query', """
SELECT
    avg(extract(year from now()) - draft_year) AS "Average Years in NFL"
FROM
    idb_mvp
WHERE
    active""",
    'A query that returns the average number of years in the NFL across all active MVP award winners.')
    
    a('Super Bowl MVP Query', """
SELECT
    first_name AS "First Name",
    last_name AS "Last Name",
    (extract(year from now()) - draft_year) AS "Experience (Years)"
FROM
    idb_mvp
WHERE
    active
ORDER BY
    "Experience (Years)" DESC
LIMIT 3""",
    "The three most tenured Super Bowl MVP winners that are currently active.")
    
    malcolm_smith   = m('Malcolm',  'Smith',    'OLB',  '1989-07-05',   'Woodland Hills, CA',   'Woodland Hills (CA) Taft',         'Southern California',      2011, True,  465000,    'MalcSmitty',                                   '446422781169651712', 'zfB8hCsHwLE', 34.1683, -118.605)
    joe_flacco      = m('Joe',      'Flacco',   'QB',   '1985-01-16',   'Audubon, NJ',          'Audubon (NJ) Audubon',             'Delaware',                 2008, True,  20100000,  'JoeFlacco',                                    '446422363865755648', 'fod3tDCNZ80', 39.8901, -75.0724)
    eli_manning     = m('Eli',      'Manning',  'QB',   '1981-01-03',   'New Orleans, LA',      'New Orleans (LA) Newman',          'Mississippi',              2004, True,  13000000,  'EliManning',                                   '455503803396014080', 'I7vZ1dVSe6I', 29.9667, -90.05)
    aaron_rogers    = m('Aaron',    'Rodgers',  'QB',   '1983-12-02',   'Chico, CA',            'Chico (CA) Pleasant Valley',       'California',               2005, True,  900000,    'theaaronrodgers',                              '451545403163287553', 'BHvCUulipS0', 39.74,   -121.8356)
    drew_brees      = m('Drew',     'Brees',    'QB',   '1979-01-15',   'Austin, TX',           'Austin (TX) Westlake',             'Purdue',                   2001, True,  9750000,   'DB9NFL',                                       '451546253852037120', '6iv8WVzbXEg', 32.9825, -97.205)
    santonio_holmes = m('Santonio', 'Holmes',   'WR',   '1984-03-03',   'Belle Glade, FL',      'Belle Glade (FL) Glades Central',  'Ohio State',               2006, True,  7500000,   'santonioholmes',                               '451546782057500673', 'pNakPqb98Sk', 26.6853, -80.6714)
    peyton_manning  = m('Peyton',   'Manning',  'QB',   '1976-03-24',   'New Orleans, LA',      'New Orleans (LA) Newman',          'Tennessee',                1998, True,  18000000,  'pages/Peyton-Manning/109563725729117',         '455503645946036224', 'UzZi_GuWXmk', 29.9667, -90.05)
    hines_ward      = m('Hines',    'Ward',     'WR',   '1976-03-08',   'Seoul, South Korea',   'Forest Park (GA) Forest Park',     'Georgia',                  1998, False, 3000000,   'officialhinesward',                            '451547574294417409', '6KPC5SbfMLw', 37.5665, 126.978)
    deion_branch    = m('Deion',    'Branch',   'WR',   '1979-07-18',   'Albany, GA',           'Albany (GA) Monroe',               'Louisville',               2002, True,  925000,    'pages/Deion-Branch/108196942541674',           '451547753600913408', '3rCDogcKhPM', 31.5822, -84.1656)
    tom_brady       = m('Tom',      'Brady',    'QB',   '1977-08-03',   'San Mateo, CA',        'San Mateo (CA) Junipero Serra',    'Michigan',                 2000, True,  2000000,   'TomBrady',                                     '451547916428001280', 'X8toiXDuzn4', 37.5542, -122.3131)
    dexter_jackson  = m('Dexter',   'Jackson',  'S',    '1977-07-28',   'Quincy, FL',           'Quincy (FL) Shanks',               'Florida State',            1999, False, 1500000,   'pages/Dexter-Jackson-safety/104148316288933',  '455494468959862784', 've3ommpRIoU', 30.5833, -84.5833)
    ray_lewis       = m('Ray',      'Lewis',    'MLB',  '1975-05-15',   'Bartow, FL',           'Lakeland (FL) Kathleen',           'Miami (FL)',               1996, False, 4950000,   'officialraylewis',                             '455503471102279680', 'iX0MQaBHpDA', 27.8925, -91.8397)
    kurt_warner     = m('Kurt',     'Warner',   'QB',   '1971-06-22',   'Burlington, IA',       'Cedar Rapids (IA) Regis',          'Northern Iowa',            1994, False, 4000000,   'kurt13warner',                                 '455508940206272512', 'kCFnXuTB8zM', 40.8081, -91.1158)
    john_elway      = m('John',     'Elway',    'QB',   '1960-06-28',   'Port Angeles, WA',     'Granada Hills (CA) Granada Hills', 'Stanford',                 1983, False, 3000000,   'JohnElway',                                    '455513700447711232', 'HGMbmbnu2Oc', 48.1131, -123.4408)
    terrell_davis   = m('Terrell',  'Davis',    'RB',   '1972-10-28',   'San Diego, CA',        'San Diego (CA) Lincoln',           'Georgia',                  1995, False, 1833333,   'pages/Terrell-Davis/105958832769440',          '455863693612314625', 'RTza50UcbGo', 32.7150, -117.1625)
    desmond_howard  = m('Desmond',  'Howard',   'KR',   '1970-05-15',   'Cleveland, OH',        'Cleveland (OH) Saint Joseph',      'Michigan',                 1992, False, 851080,    'pages/Desmond-Howard/105632746137784',         '455867203233914881', 'ahjoY-XJ2ZA', 41.4822, -81.6697)
    larry_brown     = m('Larry',    'Brown',    'CB',   '1969-11-30',   'Miami, FL',            'Los Angeles (CA) Los Angeles',     'Texas Christian',          1991, False, 500000,    '',                                           '455870737597751296', 'sm27goWtbuA', 25.7877, -80.2241)
    steve_young     = m('Steve',    'Young',    'QB',   '1961-10-11',   'Salt Lake City, UT',   'Greenwich (CT) Greenwich',         'Brigham Young',            1984, False, 2000000,   'pages/Steve-Young/111800555502672',            '456147759876153346', '5IAE-bSLveY', 40.7500, -111.8833)
    emmitt_smith    = m('Emmitt',   'Smith',    'RB',   '1969-05-15',   'Pensacola, FL',        'Pensacola (FL) Escambia',          'Florida',                  1990, False, 2502400,   'EmmittSmith',                                  '456152015127588866', 'tnYXS8tT8uc', 30.4333, -87.2000)
    troy_aikman     = m('Troy',     'Aikman',   'QB',   '1966-11-21',   'West Covina, CA',      'Henryetta (OK) Henryetta',         'UCLA',                     1989, False, 5916500,   'TroyAikman',                                   '456155452871426049', 'rLMoOB2QJ-4', 34.0567, -117.9186)
    mark_rypien     = m('Mark',     'Rypien',   'QB',   '1962-10-02',   'Calgary, Canada',       'Shadle Park (WA) Shadle Park',     'Washington State',         1986, False, 1500000,   'pages/Mark-Rypien/109510295741903',            '456158170784612352', '5wGeVHz-tdQ', 51.0500, -114.0667)
    ottis_anderson  = m('Ottis',    'Anderson', 'RB',   '1957-01-19',   'West Palm Beach, FL',  'West Palm Beach (FL) Forest Hill', 'Miami',                    1979, False, 450000,    'pages/Ottis-Anderson/112570828755320',         '456164610903511042', 'kMfO5YgTTOY', 26.7097, -80.0642)
    joe_montana     = m('Joe',      'Montana',  'QB',   '1956-06-11',   'New Eagle, PA',        'Carroll (PA) Ringgold',            'Notre Dame',               1979, False, 4000000,   'pages/Joe-Montana/112417838771364',            '456191300836921344', 'b3AR6kctf1E', 40.2075, -79.9531)
    jerry_rice      = m('Jerry',    'Rice',     'WR',   '1962-10-13',   'Starkville, MS',       'Oktoc (MS) Moor',                  'Mississippi Valley State', 1985, False, 4530400,   'jerryrice',                                    '456192898791264256', 'WMzyMglPvw8', 33.4625, -88.8200)
    doug_williams   = m('Doug',     'Williams', 'QB',   '1955-08-09',   'Zachary, LA',          'Zachary (LA) Chaneyville',         'Grambling State',          1978, False, 400000,    'pages/Doug-Williams/109237215762583',          '456196627082903552', 'Xa-eryLtKP0', 36.6550, -91.1567)
    phil_simms      = m('Phil',     'Simms',    'QB',   '1954-11-03',   'Springfield, KY',      'Springfield (KY) Southern',        'Morehead State',           1979, False, 1400000,   'pages/Phil-Simms/103095756397480',             '456199339845496832', 'HwUA5gjImQo', 37.6864, -85.2219)
    richard_dent    = m('Richard',  'Dent',     'DE',   '1960-12-13',   'Atlanta, GA',          'Atlanta (GA) Murphy',              'Tennessee State',          1983, False, 90000,     'pages/Richard-Dent/113226882025284',           '456202102881017857', '6-4aSqViBBM', 33.7550, -84.3900)
    marcus_allen    = m('Marcus',   'Allen',    'RB',   '1960-03-26',   'San Diego, CA',        'San Diego (CA) Lincoln',           'Southern California',      1982, False, 1100000,   'pages/Marcus-Allen/108850645806576',           '456268471928487936', 'RRddQvuWjdA', 32.7150, -117.1625)
    john_riggins    = m('John',     'Riggins',  'RB',   '1949-08-04',   'Seneca, KS',           'Centralia (KS) Centralia',         'Kansas',                   1971, False, 300000,    'riggo44',                                      '456270948979597312', 'PA8zDpHVGVE', 39.8356, -96.0661)
    jim_plunkett    = m('Jim',      'Plunkett', 'QB',   '1947-12-05',   'San Jose, CA',         'San Francisco (CA) Lick',          'Stanford',                 1971, False, 180000,    'pages/Jim-Plunkett/111935175489887',           '456276772384825345', '7Fwaii8abss', 37.3333, -121.9000)
    terry_bradshaw  = m('Terry',    'Bradshaw', 'QB',   '1948-09-02',   'Shreveport, LA',       'Shreveport (LA) Woodlawn',         'Lousiana Tech',            1970, False, 1000000,   'OfficialTerryBradshaw',                        '456621383036833793', '2U1Xtci4PBw', 32.4681, -93.9211)
    harvey_martin   = m('Harvey',   'Martin',   'DE',   '1950-11-16',   'Dallas, TX',           'Dallas (TX) South Oak Cliff',      'East Texas State',         1973, False, 0,          'pages/Harvey-Martin/109525865740587',          '456626031764307968', 'EhxmJNyR_-A', 32.7758, -96.7967)
    fred_biletnikoff = m('Fred',    'Biletnikoff', 'WR', '1943-02-23',  'Erie, PA',             'Erie (PA) Technical Memorial',     'Florida State',            1965, False, 0,          'pages/Fred-Biletnikoff/106147252750285',       '456626186890653698', 'A-bFyBnmS6M', 42.1296, -80.0852)
    lynn_swann      = m('Lynn',     'Swann',     'WR',  '1952-03-07',   'Alcoa, TN',            'San Mateo (CA) Junipero Serra',    'Southern California',      1974, False, 0,          'pages/Lynn-Swann/109274705758597',              '456626350422372353', 'uwt9Es4oidg', 35.8038, -83.9775)
    franco_harris   = m('Franco',   'Harris',   'FB',   '1950-03-07',   'Fort Dix, NJ',         'Mount Holly (NJ) Rancocas Valley', 'Pennsylvania State',       1972, False, 560000,    'pages/Franco-Harris/107626815933595',          '456630317969727488', '6wbfLcflHkA', 40.0192, -74.5228)
    larry_csonka    = m('Larry',    'Csonka',   'FB',   '1946-12-25',   'Stow, OH',             'Stow (OH) Stow',                   'Syracuse',                 1968, False, 64000,     'pages/Larry-Csonka/109735832386997',           '456626657369927681', 'DHX-obVmY5I', 41.1594, -81.4403)
    jake_scott      = m('Jake',     'Scott',    'S',    '1945-07-20',   'Greenwood, SC',        'Arlington (VA) Washington Lee',    'Georgia',                  1970, False, 95000,     '',                                           '',                 '2eVWJhOZFWg', 34.1897, -82.1547)
    roger_staubach  = m('Roger',    'Staubach', 'QB',   '1942-02-05',   'Cincinatti, OH',       'Cincinatti (OH) Purcell',          'Navy',                     1964, False, 25000,     'pages/Roger-Staubach/107791622577054',         '456626779097006081', 'sNJvW8w5JSU', 39.1000, -84.5167)
    chuck_howley    = m('Chuck',    'Howley',   'LB',   '1936-06-28',   'Wheeling, WV',         'Wheeling (WV) Warwood',            'West Virginia',            1955, False, 0,      'pages/Chuck-Howley/108425575849095',           '456627114020569088', 'HgFaUquznoU', 40.0703, -80.6986)
    len_dawson      = m('Len',      'Dawson',   'QB',   '1935-06-20',   'Alliance, OH',         'Alliance (OH) Alliance',           'Purdue',                   1957, False, 25000,     'pages/Len-Dawson/103741019664235',             '456627343620980736', 'W9iGf0DMpwA', 40.9133, -81.1081)
    joe_namath      = m('Joe',      'Namath',   'QB',   '1943-05-31',   'Beaver Falls, PA',     'Beaver Falls (PA) Beaver Falls',   'Alabama',                  1965, False, 427000,    'JoeNamath',                                    '456627597288284160', 'mTPZWj755Ao', 40.4506, -80.1909)
    bart_starr      = m('Bart',     'Starr',    'QB',   '1934-01-09',   'Montgomery, AL',       'Montgomery (AL) Sydney Lanier',    'Alabama',                  1956, False, 100000,    'pages/Bart-Starr/103751799662897',             '456627731749298176', 'F1leMrGVglQ', 32.3617, -86.2792)

    seahawks    = f([malcolm_smith],                                                            'Seahawks',     'Seattle',      'WA', 'Paul Allen',                 'John Schneider',   'Pete Carroll',     1974, True, 'CenturyLink Field',                'NFC West',  'Seahawks',            '446422083765956608', 'l9-NicPH-58', 47.5953, -122.3317)
    ravens      = f([joe_flacco, ray_lewis],                                                    'Ravens',       'Baltimore',    'MD', 'Steve Bisciotti',            'Ozzie Newsome',    'John Harbaugh',    1996, True, 'M&T Bank Stadium',                 'AFC North', 'baltimoreravens',     '446421801954852864', 'xvkYrio5JYg', 39.2781, -76.6228)
    giants      = f([eli_manning, ottis_anderson, phil_simms],                                  'Giants',       'New York',     'NJ', 'John Mara',                  'Jerry Reese',      'Tom Coughlin',     1925, True, 'MetLife Stadium',                  'NFC East',  'newyorkgiants',       '446421524447117312', 'HAhCCm-_0Ig', 40.8136, -74.0744)
    packers     = f([aaron_rogers, desmond_howard, bart_starr],                                 'Packers',      'Green Bay',    'WI', 'Green Bay Packers, Inc.',    'Ted Thompson',     'Mike McCarthy',    1919, True, 'Lambeau Field',                    'NFC North', 'Packers',             '451544186739634176', 'pr9dq6Wa8ao', 44.5014, -88.0622)
    saints      = f([drew_brees],                                                               'Saints',       'New Orleans',  'LA', 'Tom Benson',                 'Mickey Loomis',    'Sean Payton',      1967, True, 'Mercedes-Benz Superdome',          'NFC South', 'neworleanssaints',    '451544324249882624', 'z23NV3pvrvw', 29.9508, -90.0811)
    steelers    = f([santonio_holmes, hines_ward, franco_harris, lynn_swann, terry_bradshaw],   'Steelers',     'Pittsburgh',   'PA', 'Dan Rooney',                 'Kevin Colbert',    'Mike Tomlin',      1933, True, 'Heinz Field',                      'NFC North', 'steelers',            '451544466084478976', '4R9PUh2JoHE', 40.4467, -80.0158)
    colts       = f([peyton_manning,chuck_howley],                                              'Colts',        'Indianapolis', 'IN', 'Jim Irsay',                  'Ryan Grigson',     'Chuck Pagano',     1953, True, 'Lucas Oil Stadium',                'AFC South', 'colts',               '451544637786697728', '0MLKaIexSeM', 39.7601, -86.1638)
    patriots    = f([deion_branch, tom_brady],                                                  'Patriots',     'New England',  'MA', 'Robert Kraft',               'Bill Belichick',   'Bill Belichick',   1959, True, 'Gillette Stadium',                 'AFC East',  'newenglandpatriots',  '451544728324939777', 'o8Bpa59pGnA', 42.0909, -71.2643)
    eagles      = f([],                                                                         'Eagles',       'Philadelphia', 'PA', 'Jeffrey Lurie',              'Howie Roseman',    'Chip Kelly',       1933, True, 'Lincoln Financial Field',          'NFC East',  'philadelphiaeagles',  '451544818934493184', '3uaF5FYGiis', 39.9008, -75.1675)
    bears       = f([richard_dent],                                                             'Bears',        'Chicago',      'IL', 'Virginia Halas McCaskey',    'Phil Emery',       'Marc Trestman',    1919, True, 'Soldier Field',                    'NFC North', 'ChicagoBears',        '451544950295912448', 'yp6PSPu8qVg', 41.8625, -87.6167)
    cardinals   = f([],                                                                         'Cardinals',    'Arizona',      'AZ', 'Bill Bidwill',               'Steve Keim',       'Bruce Arians',     1898, True, 'University of Phoenix Stadium',    'NFC West',  'arizonacardinals',    '451545069774848000', 'WErrzXz6D7I', 33.5275, -112.2625)
    niners      = f([steve_young, joe_montana, jerry_rice],                                     '49ers',        'San Francisco','CA', 'Jed York',                   'Trent Baalke',     'Jim Harbaugh',     1946, True, 'Levi\'s Stadium',                  'NFC West',  'SANFRANCISCO49ERS',   '451545166600355840', '587Oow7Ckko', 37.4034, -121.9703)
    broncos     = f([john_elway, terrell_davis],                                                'Broncos',      'Denver',       'CO', 'Pat Bowlen',                 'John Elway',       'John Fox',         1960, True, 'Sports Authority Field',           'AFC West',  'DenverBroncos',       '451545258929577984', 'HGMbmbnu2Oc', 39.7439, -105.02)
    panthers    = f([],                                                                         'Panthers',     'Carolina',     'NC', 'Jerry Richardson',           'Dave Gettleman',   'Ron Rivera',       1993, True, 'Bank of America Stadium',          'NFC South', 'CarolinaPanthers',    '451545705941708801', 'cJlTyJletUw', 35.2258, -80.8528)
    buccaneers  = f([dexter_jackson],                                                           'Buccaneers',   'Tampa Bay',    'FL', 'Malcolm Glazer',             'Jason Licht',      'Lovie Smith',      1976, True, 'Raymond James Stadium',            'NFC South', 'tampabaybuccaneers',  '455494334251425793', 'BryumQkEB9E', 27.9758, -82.5033)
    raiders     = f([marcus_allen, jim_plunkett, fred_biletnikoff],                             'Raiders',      'Oakland',      'CA', 'Mark Davis',                 'Reggie McKenzie',  'Dennis Allen',     1960, True, 'O.co Coliseum',                    'AFC West',  'Raiders',             '455489209424293888', '4iayn-leI3s', 37.7517, -122.2006)
    rams        = f([kurt_warner],                                                              'Rams',         'Saint Louis',  'MO', 'Stan Kroenke',               'Les Snead',        'Jeff Fisher',      1936, True, 'Edward Jones Dome',                'NFC West',  'Rams',                '455499079301091328', 'xXKcFhMscb8', 38.6328, -90.1886)
    titans      = f([],                                                                         'Titans',       'Tennessee',    'TN', 'Bud Adams',                  'Ruston Webster',   'Ken Whisenhunt',   1960, True, 'LP Field',                         'AFC South', 'titans',              '455510546826002432', 'fjUASLNhSVA', 36.1664, -86.7714)
    falcons     = f([],                                                                         'Falcons',      'Atlanta',      'GA', 'Arthur Blank',               'Thomas Dimitroff', 'Mike Smith',       1966, True,  'Georgia Dome',                     'NFC South', 'atlantafalcons',      '455514543985147904', '1-A6I9ctukw', 33.7575, -84.4008)
    cowboys     = f([larry_brown, emmitt_smith, troy_aikman, roger_staubach, harvey_martin],    'Cowboys',      'Dallas',       'TX', 'Jerry Jones',                'Jerry Jones',      'Jason Garrett',    1960, True, 'AT&T Stadium',                     'NFC East',  'DallasCowboys',       '455871595420995584', 'l76i3jkJbJg', 32.7478, -97.0928)
    chargers    = f([],                                                                         'Chargers',     'San Diego',    'CA', 'Alex Spanos',                'Tom Telesco',      'Mike McCoy',       1960, True, 'Qualcomm Stadium',                 'AFC West',  'chargers',            '456148732640112642', 'rEUW4PoxufY', 32.7831, -117.1194)
    bills       = f([],                                                                         'Bills',        'Buffalo',      'NY', 'Mary Wilson',                'Doug Whaley',      'Doug Marrone',     1960, True, 'Ralph Wilson Stadium',             'AFC East',  'BuffaloBills',        '456152844333101056', 'QsTAKmDayXk', 42.7736, -78.7869)
    redskins    = f([mark_rypien, doug_williams, john_riggins],                                 'Redskins',     'Washington',   'MD', 'Dan Snyder',                 'Bruce Allen',      'Jay Gruden',       1932, True, 'FedEx Field',                      'NFC East',  'redskins',            '456159314340634624', 'I6cS969CI_s', 38.9078, -76.8644)
    bengals     = f([],                                                                         'Bengals',      'Cincinatti',   'OH', 'Mike Brown',                 'Mike Brown',       'Marvin Lewis',     1968, True, 'Paul Brown Stadium',               'NFC North', 'bengals',             '456193763098894337', 'R5DjQyN9Ync', 39.0954, -84.5160)
    dolphins    = f([jake_scott, larry_csonka],                                                 'Dolphins',     'Miami',        'FL', 'Stephen Ross',               'Dennis Hickey',    'Joe Philbin',      1966, True, 'Sun Life Stadium',                 'AFC East',  'MiamiDolphins',       '456205147299782656', 'JBlprt4wHdE', 25.9581, -80.2389)
    vikings     = f([],                                                                         'Vikings',      'Minnesota',    'MN', 'Zygi Wilf',                  'Rick Spielman',    'Mike Zimmer',      1961, True, 'TCF Bank Stadium',                 'NFC North', 'minnesotavikings',    '456635573206126592', '0I3-nsUDtVI', 44.9764, -93.2244)
    jets        = f([joe_namath],                                                               'Jets',         'New York',     'NJ', 'Woody Johnson',              'John Idzik',       'Rex Ryan',         1963, True, 'MetLife Stadium',                  'AFC East',  'jets',                '456635661882122241', 'Vuvz15OjCVc', 40.8136, -74.0744)
    chiefs      = f([len_dawson],                                                               'Chiefs',       'Kansas City',  'MO', 'Clark Hunt',                 'John Dorsey',      'Andy Reid',        1963, True, 'Arrowhead Stadium',                'AFC West',  'KansasCityChiefs',    '456635985632059394', 'h3-6ixzvNY0', 39.0489, -94.4839)

    sb39 = s(patriots,      eagles,     deion_branch,    '11 REC 122 YDS 0 TD 12 TGTS',                 24, 21, 'Alltel Stadium',                'Jacksonville',    'FL', '2005-02-06', 78125,  'XXXIX',   'Paul McCartney',                                    '455506322247536640', 'yo_IAOju128', 30.3239, -81.6375,  'Deion Branch became the third offensive player to win the SB MVP without accounting for a touchdown. His 11 receptions tied a Super Bowl record.')
    sb40 = s(steelers,      seahawks,   hines_ward,      '5 REC 123 YDS 1 TD 11 TGTS 1 CAR 18 YDS',     21, 10, 'Ford Field',                    'Detroit',         'MI', '2006-02-05', 68206,  'XL',      'The Rolling Stones',                                '455506536152850432', 'p5YA9Ah2Z1Y', 42.34,   -83.0456,  'Legendary Steeler Hines Ward lifted the Steelers to their 5th Super Bowl victory while winning his only Super Bowl MVP. Known as a ferocious blocker, Ward led the Steelers in receptions and yards, acting as a security blanket for second-year QB Ben Roethlisberger.')
    sb41 = s(colts,         bears,      peyton_manning,  '25/38 247 YDS 1 TD 1 INT 1 CAR 0 YDS',        29, 17, 'Dolphin Stadium',               'Miami Gardens',   'FL', '2007-02-04', 74512,  'XLI',     'Prince',                                            '455506774993301504', '8cVMzkCIV6E', 29.9581, -80.2389,  'Future Hall of Famer Peyton Manning led the Indianapolis Colts to their second Super Bowl championship. Manning capped off a season in which he threw 31 TD and only 9 INT by throwing for 1 TD and 1 INT')
    sb42 = s(giants,        patriots,   eli_manning,     '19/34 255 YDS 2 TD 1 INT 3 CAR 4 YDS',        17, 14, 'University of Phoenix Stadium', 'Glendale',        'AZ', '2008-02-03', 71101,  'XLII',    'Tom Petty and the Heartbreakers',                   '455506854831874048', '0o8XmdQ7Zjo', 33.5275, -112.2625, 'Eli Manning and the Giants upset the heavily favored Patriots on a late game heave to WR David Tyree. His 2 fourth quarter TDs lifted the Giants over the Patriots, who had yet to lose a game that season.')
    sb43 = s(steelers,      cardinals,  santonio_holmes, '9 REC 131 YDS 1 TD 13 TGTS',                  27, 23, 'Raymond James Stadium',         'Tampa',           'FL', '2009-02-01', 70774,  'XLIII',   'Bruce Springsteen and the E Street Band',           '455506960314421248', 'PzDawiYEpFU', 27.9758, -82.5033,  'Santonio Holmes game winning 6 yd TD catch resulted in the Steelers\' sixth Super Bowl championship. The catch was one of the all time greats in SB history, and was one of his nine spectacular receptions that game.')
    sb44 = s(saints,        colts,      drew_brees,      '32/39 288 YDS 2 TD 0 INT 1 CAR -1 YDS',       31, 17, 'Sun Life Stadium',              'Miami Gardens',   'FL', '2010-02-07', 74059,  'XLIV',    'The Who',                                           '455507032183799809', 'M1OIISkx9Hk', 25.9581, -80.2389,  'Four years after Hurricane Katrina devastated New Orleans, Future Hall of Famer Drew Brees led the Saints to their first Super Bowl championship. His 32 completions tied Tom Brady\'s record for the most in Super Bowl history.')
    sb45 = s(packers,       steelers,   aaron_rogers,    '24/39 304 YDS 3 TD 0 INT 2 CAR -2 YDS',       31, 25, 'Cowboys Stadium',               'Arlington',       'TX', '2011-02-06', 103219, 'XLV',     'The Black Eyed Peas',                               '455507094129483776', 'bKMVg7p5rto', 32.7478, -97.0928,  'In his third year as a starter for the Green Bay Packers, Future Hall of Famer Rodgers calmly led the team its fourth Super Bowl championship. His 3 TDs reminded fans of the retired Brett Favre and ensured Packers fans of success in years to come.')
    sb46 = s(giants,        patriots,   eli_manning,     '30/40 296 YDS 1 TD 0 INT 1 CAR -1 YDS',       21, 17, 'Lucas Oil Stadium',             'Indianapolis',    'IN', '2012-02-05', 68658,  'XLVI',    'Madonna',                                           '455507194885050368', '8eJapFSnICI', 39.7601, -86.1638,  'Once again, Eli Manning played spoiler to the New England Patriots and won his second SB MVP award. He started the game completing his first 9 attempts becoming the first quarterback to do so and put together a crucial drive with 3 1/2 minutes left that sealed the victory for the Giants.')
    sb47 = s(ravens,        niners,     joe_flacco,      '22/33 287 YDS 3 TD 0 INT 0 CAR 0 YDS',        34, 31, 'Mercedes-Benz Superdome',       'New Orleans',     'LA', '2013-02-03', 71024,  'XLVII',   'Beyonce',                                           '455507267148730369', 'ynQApEB4VXg', 29.9508, -90.0811,  'Joe Flacco capped his spectacular postseason with an impressive performance against a 49er defense that was considered one of the league\'s best. While all 3 TDs were in the first half, Flacco coolly converted third down after third down to hold off a late 49er surge.')
    sb48 = s(seahawks,      broncos,    malcolm_smith,   '9 TKLS 1 INT 1 FR 1 TD',                      43, 8,  'MetLife Stadium',               'East Rutherford', 'NJ', '2014-02-02', 82529,  'XLVIII',  'Bruno Mars and the Red Hot Chili Peppers',          '455507391715364865', 'NbcA1UISfG0', 40.8136, -74.0744,  'Malcolm Smith was the de-facto SB MVP for a legendary Seattle defense. While he was a relative unknown at the start of the season, a game-sealing interception in the NFC Championship as well as two takeaways in the Super Bowl served as a coming out party for the young linebacker.')
    sb38 = s(patriots,      panthers,   tom_brady,       '32/48 354 YDS 3 TD 1 INT 2 CAR 12 YDS',       32, 29, 'Reliant Stadium',               'Houston',         'TX', '2004-02-01', 71525,  'XXXVIII', 'Janet Jackson and Justin Timberlake',               '455506147697364993', '7CCWCWOUf',   29.6847, -95.4108,  'Future Hall of Famer Tom Brady led the Patriots to victory while winning his second Super Bowl MVP. His 32 completions are the most in SB history and his 354 yds are the 5th best total in SB history.')
    sb37 = s(buccaneers,    raiders,    dexter_jackson,  '2 TKLS 2 INTS',                               48, 21, 'Qualcomm Stadium',              'San Diego',       'CA', '2003-01-26', 67603,  'XXXVII',  'Shania Twain and No Doubt',                         '455506058132213760', 'N0mW_55nA-s', 32.7831, -117.1194, 'Dexter Jackson led the Tampa Bay Buccaneers to their first and only Super Bowl victory with two interceptions. His two interceptions were part of five for a defense that largely shut down the Oakland Raiders.')
    sb36 = s(patriots,      rams,       tom_brady,       '16/27 145 YDS, 1 TD 0 INT 1 CAR 3 YDS',       20, 17, 'Louisiana Superdome',           'New Orleans',     'LA', '2002-02-03', 72922,  'XXXVI',   'U2',                                                '455505936765829120', 'N3bJuf9it0s', 29.9508, -90.0811,  'Future Hall of Famer and second year QB Tom Brady led an underdog Patriots to a Super Bowl championship where he managed to beat the St. Louis Rams and the \'Greatest Show on Turf\' offense. His passing yardage was third-lowest in SB history, but this year was the first year that included fan votes for SB MVP.')
    sb35 = s(ravens,        giants,     ray_lewis,       '3 TKLS 4 PB',                                 34, 7,  'Raymond James Stadium',         'Tampa Bay',       'FL', '2001-01-28', 71921,  'XXXV',    'Aerosmith and Britney Spears',                      '455505803215003648', 'Emqlw-1s9Qc', 27.9758, -82.5033,  'Future Hall of Famer LB Ray Lewis led the Ravens defense that limited the Giants to only 152 yards. While his stat line was unimpressive, his extraordinary leadership for a legendary defense garnered him the award.')
    sb34 = s(rams,          titans,     kurt_warner,     '24/45 414 YDS 2 TD 0 INT 1 CAR 1 YDS',        23, 16, 'Georgia Dome',                  'Atlanta',         'GA', '2000-01-31', 72625,  'XXXIV',   'Phil Collins and Christina Aguilera',               '455511890488070144', 'qQZZVH-gVk0', 33.7575, -84.4008,  'Kurt Warner led the St. Louis Rams and the Greatest Show on Turf offense to first and only Super Bowl championship. His 414 yards are the most in Super Bowl history, and he became the sixth player to win the Super Bowl and Regular Season MVP awards in the same season.')
    sb33 = s(broncos,       falcons,    john_elway,      '18/29 336 YDS 1 TD 1 INT 3 CAR 2 YDS 1 TD',   31, 19, 'Pro Player Stadium',            'Miami',           'FL', '1999-01-31', 74803,  'XXXIII',  'Gloria Estefan and Stevie Wonder',                  '455515692922445824', 'VNB2Q2eHV14', 25.9581, -80.2389,  'Hall of Famer John Elway led the Denver Broncos to their second consecutive Super Bowl championship with his gritty performance. He was the oldest Super Bowl MVP at 38 years old and retired after the championship.')
    sb32 = s(broncos,       packers,    terrell_davis,   '30 CAR 157 YDS 3 TD 2 REC 8 YDS',             31, 24, 'Qualcomm Stadium',              'San Diego',       'CA', '1998-01-25', 68912,  'XXXII',   'Boyz II Men',                                       '455864726476447744', 'cnpJt4GT0TY', 32.7831, -117.1194, 'Despite missing the most of the second quarter, Terrell Davis came back and scored the game winning touchdown with 1:45 left to play. He returned home to win his first Super Bowl, and his 3 rushing touchdowns are a Super Bowl record.')
    sb31 = s(packers,       patriots,   desmond_howard,  '4 KR 154 YDS 1 TD 6 PR 90 PR YDS',            35, 21, 'Louisiana Superdome',           'New Orleans',     'LA', '1997-01-26', 72301,  'XXXI',    'James Brown',                                       '455868650403028992', 'xqLC1pVLfCk', 29.9508, -90.0811,  'Electrifying athlete Desmond Howard became the first special teams player to win the Super Bowl MVP after sealing the game with a 99 yd kick off return for a touchdown. He went on to become one of the most feared returners in the league, picking up right where he left off as a Heisman trophy winner in college.')
    sb30 = s(cowboys,       steelers,   larry_brown,     '2 INT',                                       27, 17, 'Sun Devil Stadium',             'Tempe',           'AZ', '1996-01-28', 76347,  'XXX',     'Diana Ross',                                        '455872601374474240', 'ajqfz42eBTI', 33.4264, -111.9325, 'Dallas\' Larry Brown became the first cornerback to win the Super Bowl MVP by recording two interceptions that led to Emmitt Smith touchdowns. His two interceptions helped the Cowboys rally back from two deficits and secured Dallas\' fifth Super Bowl Championship.')
    sb29 = s(niners,        chargers,   steve_young,     '24/36 325 YDS 6 TD 0 INT 5 CAR 49 YDS',       49, 26, 'Joe Robbie Stadium',            'Miami',           'FL', '1995-01-29', 74107,  'XXIX',    'Tony Bennett and Patti LaBelle',                    '456149720667127808', 'RpYz-NYRqCY', 25.9581, -80.2389,  'Hall of Famer Steve Young led the Niners to their fifth Super Bowl championship by throwing for a record 6 TDs. He led the Niners in both passing and rushing yards becoming the first Super Bowl MVP to lead his team in both categories.')
    sb28 = s(cowboys,       bills,      emmitt_smith,    '30 CAR 132 YDS 2 TD 4 REC 26 YDS',             30, 13, 'Georgia Dome',                  'Atlanta',         'GA', '1994-01-30', 72817,  'XXVIII',   'The Judds',                                         '456153740337102850', 'iEgWKTxNjww', 33.7575, -84.4008,  'Hall of Famer Emmitt Smith turned in a monster performance to lead the Dallas Cowboys to their fourth Super Bowl Championship. His 158 yards from scrimmage accounted for nearly half of the Cowboys\' yardage.')
    sb27 = s(cowboys,       bills,      troy_aikman,     '22/30 273 YDS 4 TD 0 INT 3 CAR 28 YDS',       52, 17, 'Rose Bowl Stadium',             'Pasadena',        'CA', '1993-01-31', 98374,  'XXVII',   'Michael Jackson',                                   '456156368320212993', 'olb10lOMe3o', 34.1614, -118.1675, 'Hall of Famer Troy Aikman helped the Cowboys win their third Super Bowl Championship with his only Super Bowl MVP in an illustrious career. It was performances like these that grant him the title of the Super Bowl\'s most accurate passer with a completion percentage of 70.0.')
    sb26 = s(redskins,      bills,      mark_rypien,     '18/33 292 YDS 2 TD 1 INT 6 CAR -4 YDS',       37, 24, 'Hubert H. Humphrey Metrodome',  'Minneapolis',     'MN', '1992-01-26', 63130,  'XXVI',    'Gloria Estefan',                                    '456160285577854977', 'cc3t410pzgY', 44.9739, -93.2581,  'As one of the lowest paid quarterbacks in the modern era, Rypien and his great stable of receivers brought the Redskins their third championship. Rypien became the third different quarterback to win a Super Bowl with the Redskins.')
    sb25 = s(giants,        bills,      ottis_anderson,  '21 CAR 102 1 TD 1 REC 7 YDS',                 20, 19, 'Tampa Stadium',                 'Tampa Bay',       'FL', '1991-01-27', 73813,  'XXV',     'New Kids on the Block',                             '456162471766523905', 'UT0r8wBL4QU', 27.5844, -82.3013,  'In the last Super Bowl at Tampa Stadium (before it was demolished), Ottis Anderson led a Giants rushing attack whose ability to hold position kept the explosive Bills offense off the field. Anderson\'s ability to pick up first downs allowed the Giants to hold the ball for nearly 40 minutes.')
    sb24 = s(niners,        broncos,    joe_montana,     '22/29 297 YDS 5 TD 0 INT 2 CAR 15 YDS',       55, 10, 'Louisiana Superdome',           'New Orleans',     'LA', '1990-01-28', 72919,  'XXIV',    'Pete Fountain',                                     '456189771992166400', 'FT2_6DD-B0k', 29.9508, -90.0811,  'Hall of Famer Joe Montana won his third Super Bowl MVP and his fourth Super Bowl with his performance against the Broncos. At one point, he completed a then Super Bowl record 13 straight passes, and he became the third player to win both the regular season MVP and Super Bowl MVP in the same season. His 5 TDs are the second most in Super Bowl history.')
    sb23 = s(niners,        bengals,    jerry_rice,      '11 REC 215 YDS 1 TD 1 CAR 5 YDS',             20, 16, 'Joe Robbie Stadium',            'Miami',           'FL', '1989-01-22', 75597,  'XXIII',   'South Florida-area Dancers',                        '456194831484596224', 'M5Jly6_tMAI', 25.9581, -80.2389,  'Hall of Famer Jerry Rice set a Super Bowl record with 215 receiving yards in the 49ers\' third Super Bowl victory. Performances like these made him one of the most accomplished wide receivers in the history of the Super Bowl.')
    sb22 = s(redskins,      broncos,    doug_williams,   '18/29 340 YDS 4 TD 1 INT 2 CAR -2 YDS',       42, 10, 'Jack Murphy Stadium',           'San Diego',       'CA', '1988-01-31', 73302,  'XXII',    'Chubby Checker and The Rockettes',                  '456197719590064128', '_1HHxCPgd8w', 32.7831, -117.1194, 'After starting the season as a backup, Doug Williams led the Redskins to a beatdown of John Elway\'s Broncos while becoming the first African American quarterback in Super Bowl history. He is the only quarterback to have thrown for 4 TDs in a quarter, and his 340 YDs were a Super Bowl record.')
    sb21 = s(giants,        broncos,    phil_simms,      '22/25 268 YDS 3 TD 0 INT 3 CAR 25 YDS',       39, 20, 'Rose Bowl Stadium',             'Pasadena',        'CA', '1987-01-25', 101063, 'XXI',     'Southern California High School',                   '456200080987389952', '2PHjR54cr64', 34.1614, -118.1675, 'Phil Simms and the \'Big Blue Wrecking Crew\' of the New York Giants demolished John Elway\'s Broncos in Super Bowl XXI. Simms\' accuracy (he posted an 88.0 completion percentage, a Super Bowl record) and a third quarter offensive explosion led the Giants to their first of four Super Bowl championships.')
    sb20 = s(bears,         patriots,   richard_dent,    '1.5 SACK 2 FF 1 PB',                           46, 10, 'Louisiana Superdome',           'New Orleans',     'LA', '1986-01-26', 73818,  'XX',      'Up With People',                                    '456203041071312898', 'H0r2i9KNaFY', 29.9508, -90.0811,  'Hall of Famer Richard Dent led a Bears defense that held the Patriots to 123 total yards. The Dent-led defense set Super Bowl records for sacks (7), fewest rush yards allowed (7), and margin of victory (36 points).')
    sb19 = s(niners,        dolphins,   joe_montana,     '24/35 331 YDS 3 TD 0 INT 5 CAR 59 YDS 1 TD',  38, 16, 'Stanford Stadium',              'Stanford',        'CA', '1985-01-20', 84059,  'XIX',     'World of Children\'s Dreams',                       '456205885556015106', 'XqPeW1a6QCg', 37.4344, -122.1611, 'In a dominating fashion, Joe Montana coordinated the 49ers\' offense to a demolition of the Miami Dolphins. His 59 rushing yards were a Super Bowl record for a QB. It was his second Super Bowl MVP award.')
    sb18 = s(raiders,       redskins,   marcus_allen,    '20 CAR 191 YDS 2 TD 2 REC 18 YDS',            38, 9,  'Tampa Stadium',                 'Tampa Bay',       'FL', '1984-01-22', 72920,  'XVIII',   'Salute to Superstars of the Silver Screen',         '456269417077145600', 'Lok2ZYo9xUg', 27.5844, -82.3013,  'Marcus Allen put the Los Angeles Raiders (at the time) on his back and brought home the trophy in his only Super Bowl appearance in an illustrious Hall of Fame career. His performance in the game yielded him the most rushing yards in Super Bowl history at the time, and his 9.6 yards per carry is an all-time Super Bowl record.')
    sb17 = s(redskins,      dolphins,   john_riggins,    '38 CAR 166 YDS 1 TD 1 REC 15 YDS',            27, 17, 'Rose Bowl Stadium',             'Pasadena',        'CA', '1983-01-30', 103667, 'XVII',    'Bob Jani Productions and the LA Super Drill Team',  '456272219019026434', 'u_Hrv5TNb2Y', 34.1614, -118.1675, 'With the Dolphins coming into the game as a slight favorite, the Redskins maintained possession, ran for a record 276 yards, and won the game thanks to the efforts of Hall of Famer John Riggins. His go-ahead 43 YD touchdown gave him a the Super Bowl record for rushing yards, and his 38 carries are an all-time Super Bowl record.')
    sb16 = s(niners,        bengals,    joe_montana,     '14/22 157 YDS 1 TD 0 INT 6 CAR 18 YDS 1 TD',  26, 21, 'Pontiac Silverdome',            'Pontiac',         'MI', '1982-01-24', 81270,  'XVI',     'Up With People',                                    '456274176202915840', '0nnPsoTYsNk', 42.6458, -83.2550,  'In his most unspectacular Super Bowl performance, Joe Montana led the 49ers to their first Super Bowl title. While they were outgained in both yards and touchdowns, the Niners prevailed mainly due to Montana\'s resilience that made him a 4 time Super Bowl champion.')
    sb15 = s(raiders,       eagles,     jim_plunkett,    '13/21 261 YDS 3 TD 0 INT 3 CAR 9 YDS',        27, 10, 'Louisiana Superdome',           'New Orleans',     'LA', '1981-01-25', 76135,  'XV',      'Jim Skinner Productions',                           '456278118055964672', 'zBRZchpWFTw', 29.9508, -90.0811,  'After bouncing around the league since he arrived as a Heisman Trophy winner, Plunkett was signed to be a back up for the Raiders. When their starting QB went down with an injury, Plunkett stepped up and revived his career by winning his first Super Bowl title at age 33. He became the second Heisman winner to win a Super Bowl MVP.')
    sb14 = s(steelers,       rams,      terry_bradshaw,  '14/21 309 YDS 2 TD 3 INT 3 CAR 9 YDS',     31, 19, 'Rose Bowl',                     'Pasadena',    'CA', '1980-01-20', 103985, 'XIV',  'Up with People',                                            '456588499106295808', 'TowB8FkHSFU', 34.1614, -118.1675, 'Terry Bradshaw became the first to earn back-to-back MVP honors since Green Bay\'s Bart Starr. In a 31-19 victory over the Rams, Bradshaw threw for 309 yards and two touchdowns, completing 14-of-21 passes. Bradshaw twice rallied Pittsburgh from behind, including a 13-10 deficit at the half. Bradshaw teamed with John Stallworth on a 73-yard score to take back the lead for good.')
    sb13 = s(steelers,       cowboys,   terry_bradshaw,  '17/30 318 YDS 4 TD 1 INT CAR -5 YDS 0 TD', 35, 31, 'Orange Bowl',                   'Miami',       'FL', '1979-01-21', 79484,  'XIII', 'Bob Jani',                                                  '456588464243236866', 'yOxggzRRnKA', 25.7780, -80.2198, 'Throwing a Super Bowl record four touchdown passes, quarterback Terry Bradshaw was named the MVP in the Steelers\' 35-31 win over Dallas. Setting a personal best with 318 passing yards, Bradshaw led Pittsburgh to its third Super Bowl championship in five seasons. With 17 completions in 30 attempts, nearly 25 percent of Bradshaw\'s passes went for scores.')
    sb12 = s(cowboys,        broncos,   harvey_martin,   '1 SACK',                                   27, 10, 'Louisiana Superdome',           'New Orleans', 'LA', '1978-01-15', 76400,  'XII',  'Tyler Junior College Apache Belles',                        '456588436120408064', 'r8ad3pDqFO4', 29.9508, -90.0811,  'Defensive tackle Randy White was one of the leaders of a Dallas defense that forced eight Denver turnovers. Bronco quarterbacks had only 8 completions in 25 attempts under the fierce Cowboy rush, led by White.')
    sb11 = s(raiders,        vikings,   fred_biletnikoff,'4 REC 79 YDS 0 TD',                        32, 14, 'Rose Bowl',                     'Pasadena',    'CA', '1977-01-09', 103438, 'XI',   'Los Angeles Unified All-City Band',                         '456588403115438080', 'yn-BJWr7a9M', 34.1614, -118.1675, 'Eye-black blazing and wristbands flashing, wide receiver Fred Biletnikoff helped Oakland win its first NFL title with a 32-14 victory over Minnesota. While Biletnikoff had only 4 receptions for 79 yards, three of his catches set up short Oakland touchdowns.')
    sb10 = s(steelers,       cowboys,   lynn_swann,      '4 REC 161 YDS 1 TD',                       21, 17, 'Orange Bowl',                   'Miami',       'FL', '1976-01-18', 80187,  'X',    'Up with People',                                            '456593528655585281', 'hmgtcehm_lI', 25.7780, -80.2198, 'The Steelers were led by balletic wide receiver Lynn Swann, who set a Super Bowl record with 161 receiving yards on 4 catches and earned the MVP award. A 64-yard touchdown pass from future two-time Super Bowl MVP Terry Bradshaw to Swann late in the fourth quarter proved to be the decisive score.')
    sb09 = s(steelers,       vikings,   franco_harris,   '34 CAR 158 YDS 1 TD',                      16, 6,  'Tulane Stadium',                'New Orleans', 'LA', '1975-01-12', 80997,  'IX',   'Mercer Ellington and Grambling State University Band',      '456588000441270274', '2DVZId4CJjA', 29.9430, -90.1176, 'To earn the first of its four Super Bowl championships, Pittsburgh turned to workhorse running back Franco Harris. Harris rushed 34 times for 158 yards, breaking the record Larry Csonka set one year earlier. After a baseball-like 2-0 halftime score in favor of Pittsburgh, the Steelers took advantage with a Minnesota fumble. Harris\' running and the powerful Steeler defense combined to make that lead stand.')
    sb08 = s(dolphins,       vikings,   larry_csonka,    '33 CAR 145 YDS 2 TD',                      24, 7,  'Rice Stadium',                  'Houston',     'TX', '1974-01-13', 71882,  'VIII', 'The University of Texas Longhorn Band',                     '456587849475706881', 'I4k-Q0TZNbc', 29.7163, -95.4097, 'Powerful running back Larry Csonka powered Miami to its second consecutive Super Bowl championship, a 24-7 victory over Minnesota. Csonka carried the ball 33 times for 145 yards, a Super Bowl record at the time. Csonka\'s 5-yard touchdown run in the first quarter capped off a 62-yard drive and opened the scoring for the Dolphins. Ahead 17-0 in the third quarter, Miami put the game away on with a Csonka 2-yard run.')
    sb07 = s(dolphins,       redskins,  jake_scott,      '2 INT 63 YDS 2/2 4 YDS 0 TD',              14, 7,  'Los Angeles Memorial Coliseum', 'Los Angeles', 'CA', '1973-01-14', 90182,  'VII',  'Woody Herman and the Michigan Marching Band',               '456587641463390209', 'JuWBZ3nrhxU', 34.0142, -118.2878, 'Safety Jake Scott became only the second defensive player to win the MVP. Scott had two interceptions, including one in the end zone during the fourth quarter. That interception and his 55-yard return iced the game for the Dolphins.')
    sb06 = s(cowboys,        dolphins,  roger_staubach,  '12/19 119 YDS 2 TD',                       24, 3,  'Tulane Stadium',                'New Orleans', 'LA', '1972-01-16', 81023,  'VI',   'Ella Fitzgerald and the U.S. Marine Corps Drill Team',      '456587524073218048', 'en-t4YFUEQI', 29.9430, -90.1176, 'Quarterback Roger Staubach earned the MVP award for directing an attack where he completed 12 of 19 passes for 119 yards and 2 touchdowns. Leading 3-0, Dallas made it 10-0 on Staubach\'s 7-yard touchdown pass to Lance Alworth. Staubach finished off the scoring in the fourth quarter with another 7-yard touchdown pass.')
    sb05 = s(colts,          cowboys,    chuck_howley,   '2 INT',                                    16, 13, 'Orange Bowl',                   'Miami',       'FL', '1971-01-17', 80562,  'V',    'Marching Golden Eagles Band with Anita Bryant',             '456584988784197632', 'peAhwO3i9x8', 25.7780, -80.2198, 'Dallas linebacker Chuck Howley became the first defensive player to be named Super Bowl MVP. But the honor had a hollow ring for Howley, who also became the first player from a losing team to be named MVP. Howley intercepted two passes and receovered a fumble to win the honor, although his effort was overshadowed by Baltimore\'s eventual win.')
    sb04 = s(chiefs,         vikings,   len_dawson,      '12/17 142 YDS 1 TD 1 INT 3 CAR 11 YDS',    23, 7,  'Tulane Stadium',                'New Orleans', 'LA', '1970-01-11', 80562,  'IV',   'Carol Channing',                                            '456584864427307011', 'Flrn-d8THgo', 29.9430, -90.1176, 'A series of Dawson-led drives took Kansas City to three field goals before scoring on a short run to give the Chiefs a 16-0 halftime lead. In the fourth quarter, Dawson delivered the clinching score at the end of an 82-yard drive, hitting wide receiver Otis Taylor with a 46-yard touchdown pass.')
    sb03 = s(jets,           colts,     joe_namath,      '17/28 206 YDS 0 TD 0 INT',                 16, 7,  'Orange Bowl',                   'Miami',       'FL', '1969-01-12', 75389,  'III',  'Florida A&M University band',                               '456584217099370496', 'coTlRqft1kk', 25.7780, -80.2198, 'Completing 17-of-28 passes for 206 yards, Namath directed a Jets attack that rolled up 337 yards of total offense. Namath\'s famous run off the field after the game, his index finger waving to let the world know who was "No. 1," is one of the enduring images of the Super Bowl.')
    sb02 = s(packers,        raiders,    bart_starr,     '16/23 250 YDS 2 TD 1 INT',                 35, 10, 'Los Angeles Memorial Coliseum', 'Los Angeles', 'CA', '1967-01-15', 61946,  'I',    'University of Arizona and University of Michigan Bands',    '456582737931927552', 'V7xCXr28dzc', 34.0142, -118.2878, 'In leading the Packers to a 35-10 victory over Kansas City, Starr completed 16 of 23 passes for 250 yards and three touchdowns. His main target in Super Bowl I was reserve wide receiver Max McGee, who caught 7 passes for 138 yards. McGee and Starr hooked up in the first quarter for a 37-yard score, and again at the end of the third quarter for a 13-yard touchdown.')
    sb01 = s(packers,        chiefs,     bart_starr,     '13/24 202 YDS 1 TD 0 INT 1 CAR 14 YDS',    33, 14, 'Orange Bowl',                   'Miami',       'FL', '1968-01-14', 75546,  'II',   'Grambling State University Band',                           '456583597500006401', 'rx0CZqA53nA', 25.7780, -80.2198, 'After a pair of field goals gave Green Bay an early lead, Starr threw a 62-yard touchdown pass to Boyd Dowler. Leading 16-7 at the half, the Packers scored 17 unanswered second-half points to take a commanding lead. Starr completed 13-of-24 passes for 202 yards and 1 touchdown.')
