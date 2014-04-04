BEGIN;

INSERT INTO "idb_mvp" VALUES(1,'Malcolm','Smith','OLB','1989-07-05','Woodland Hills, CA','Woodland Hills (CA) Taft','Southern California',2011,1::boolean,465000,'MalcSmitty','446422781169651712','zfB8hCsHwLE',34.1683,-118.605);
INSERT INTO "idb_mvp" VALUES(2,'Joe','Flacco','QB','1985-01-16','Audubon, NJ','Audubon (NJ) Audubon','Delaware',2008,1::boolean,20100000,'JoeFlacco','446422363865755648','fod3tDCNZ80',39.8901,-75.0724);
INSERT INTO "idb_mvp" VALUES(3,'Eli','Manning','QB','1981-01-03','New Orleans, LA','New Orleans (LA) Newman','Mississippi',2004,1::boolean,13000000,'EliManning','446087270404075520','I7vZ1dVSe6I',29.9667,-90.05);
INSERT INTO "idb_mvp" VALUES(4,'Aaron','Rodgers','QB','1983-12-02','Chico, CA','Chico (CA) Pleasant Valley','California',2005,1::boolean,900000,'theaaronrodgers','451545403163287553','BHvCUulipS0',39.74,-121.8356);
INSERT INTO "idb_mvp" VALUES(5,'Drew','Brees','QB','1979-01-15','Austin, TX','Austin (TX) Westlake','Purdue',2001,1::boolean,9750000,'DB9NFL','451546253852037120','6iv8WVzbXEg',32.9825,-97.205);
INSERT INTO "idb_mvp" VALUES(6,'Santonio','Holmes','WR','1984-03-03','Belle Glade, FL','Belle Glade (FL) Glades Central','Ohio State',2006,1::boolean,7500000,'santonioholmes','451546782057500673','pNakPqb98Sk',26.6853,-80.6714);
INSERT INTO "idb_mvp" VALUES(7,'Peyton','Manning','QB','1976-03-24','New Orleans, LA','New Orleans (LA) Newman','Tennessee',1998,1::boolean,18000000,'pages/Peyton-Manning/109563725729117','451547106910535680','UzZi_GuWXmk',29.9667,90.05);
INSERT INTO "idb_mvp" VALUES(8,'Hines','Ward','WR','1976-03-08','Seoul, South Korea','Forest Park (GA) Forest Park','Georgia',1998,0::boolean,3000000,'officialhinesward','451547574294417409','6KPC5SbfMLw',37.5665,126.978);
INSERT INTO "idb_mvp" VALUES(9,'Deion','Branch','WR','1979-07-18','Albany, GA','Albany (GA) Monroe','Louisville',2002,1::boolean,925000,'pages/Deion-Branch/108196942541674','451547753600913408','3rCDogcKhPM',31.5822,-84.1656);
INSERT INTO "idb_mvp" VALUES(10,'Tom','Brady','QB','1977-08-03','San Mateo, CA','San Mateo (CA) Junipero Serra','Michigan',2000,1::boolean,2000000,'TomBrady','451547916428001280','X8toiXDuzn4',37.5542,-122.3131);
INSERT INTO "idb_franchise_mvps" VALUES(1,1,1);
INSERT INTO "idb_franchise_mvps" VALUES(2,2,2);
INSERT INTO "idb_franchise_mvps" VALUES(3,3,3);
INSERT INTO "idb_franchise_mvps" VALUES(4,4,4);
INSERT INTO "idb_franchise_mvps" VALUES(5,5,5);
INSERT INTO "idb_franchise_mvps" VALUES(6,6,8);
INSERT INTO "idb_franchise_mvps" VALUES(7,6,6);
INSERT INTO "idb_franchise_mvps" VALUES(8,7,7);
INSERT INTO "idb_franchise_mvps" VALUES(9,8,9);
INSERT INTO "idb_franchise_mvps" VALUES(10,8,10);
INSERT INTO "idb_franchise" VALUES(1,'Seahawks','Seattle','WA','Paul Allen','John Schneider','Pete Carroll',1974,1::boolean,'CenturyLink Field','NFC West','Seahawks','446422083765956608','l9-NicPH-58',47.5953,-122.3317);
INSERT INTO "idb_franchise" VALUES(2,'Ravens','Baltimore','MD','Steve Bisciotti','Ozzie Newsome','John Harbaugh',1996,1::boolean,'M&T Bank Stadium','AFC North','baltimoreravens','446421801954852864','xvkYrio5JYg',39.2781,-76.6228);
INSERT INTO "idb_franchise" VALUES(3,'Giants','New York','NJ','John Mara','Jerry Reese','Tom Coughlin',1925,1::boolean,'MetLife Stadium','NFC East','newyorkgiants','446421524447117312','HAhCCm-_0Ig',40.8136,-74.0744);
INSERT INTO "idb_franchise" VALUES(4,'Packers','Green Bay','WI','Green Bay Packers, Inc.','Ted Thompson','Mike McCarthy',1919,1::boolean,'Lambeau Field','NFC North','Packers','451544186739634176','pr9dq6Wa8ao',44.5014,-88.0622);
INSERT INTO "idb_franchise" VALUES(5,'Saints','New Orleans','LA','Tom Benson','Mickey Loomis','Sean Payton',1967,1::boolean,'Mercedes-Benz Superdome','NFC South','neworleanssaints','451544324249882624','z23NV3pvrvw',29.9508,-90.0811);
INSERT INTO "idb_franchise" VALUES(6,'Steelers','Pittsburgh','PA','Dan Rooney','Kevin Colbert','Mike Tomlin',1933,1::boolean,'Heinz Field','NFC North','steelers','451544466084478976','4R9PUh2JoHE',40.4467,-80.0158);
INSERT INTO "idb_franchise" VALUES(7,'Colts','Indianapolis','IN','Jim Irsay','Ryan Grigson','Chuck Pagano',1953,1::boolean,'Lucas Oil Stadium','AFC South','colts','451544637786697728','0MLKaIexSeM',39.7601,-86.1638);
INSERT INTO "idb_franchise" VALUES(8,'Patriots','New England','MA','Robert Kraft','Bill Belichick','Bill Belichick',1959,1::boolean,'Gillette Stadium','AFC East','newenglandpatriots','451544728324939777','o8Bpa59pGnA',42.0909,-71.2643);
INSERT INTO "idb_franchise" VALUES(9,'Eagles','Philadelphia','PA','Jeffrey Lurie','Howie Roseman','Chip Kelly',1933,1::boolean,'Lincoln Financial Field','NFC East','philadelphiaeagles','451544818934493184','3uaF5FYGiis',39.9008,-75.1675);
INSERT INTO "idb_franchise" VALUES(10,'Bears','Chicago','IL','Virginia Halas McCaskey','Phil Emery','Marc Trestman',1919,1::boolean,'Soldier Field','NFC North','ChicagoBears','451544950295912448','yp6PSPu8qVg',41.8625,-87.6167);
INSERT INTO "idb_franchise" VALUES(11,'Cardinals','Arizona','AZ','Bill Bidwill','Steve Keim','Bruce Arians',1898,1::boolean,'University of Phoenix Stadium','NFC West','arizonacardinals','451545069774848000','WErrzXz6D7I',33.5275,-112.2625);
INSERT INTO "idb_franchise" VALUES(12,'49ers','San Francisco','CA','Jed York','Trent Baalke','Jim Harbaugh',1946,1::boolean,'Levi''s Stadium','NFC West','SANFRANCISCO49ERS','451545166600355840','587Oow7Ckko',37.4034,-121.9703);
INSERT INTO "idb_franchise" VALUES(13,'Broncos','Denver','CO','Pat Bowlen','John Elway','John Fox',1960,1::boolean,'Sports Authority Field','AFC West','DenverBroncos','451545258929577984','HGMbmbnu2Oc',39.7439,-105.02);
INSERT INTO "idb_franchise" VALUES(14,'Panthers','Carolina','NC','Jerry Richardson','Dave Gettleman','Ron Rivera',1993,1::boolean,'Bank of America Stadium','NFC South','CarolinaPanthers','451545705941708801','cJlTyJletUw',35.2258,-80.8528);
INSERT INTO "idb_superbowl" VALUES(1,8,9,9,'11 REC 122 YDS 0 TD 12 TGTS','Deion Branch became the third offensive player to win the SB MVP without accounting for a touchdown.

His 11 receptions tied a Super Bowl record.',24,21,'Alltel Stadium','Jacksonville','FL','2005-02-06',78125,'XXXIX','Paul McCartney','451548563755909120','b6XIln9M2CY',30.3239,-81.6375);
INSERT INTO "idb_superbowl" VALUES(2,6,1,8,'5 REC 123 YDS 1 TD 11 TGTS
1CAR 18 YDS','Legendary Steeler Hines Ward lifted the Steelers to their 5th Super Bowl victory while winning his only Super Bowl MVP.

Known as a ferocious blocker, Ward led the Steelers in receptions and yards, acting as a security blanket for second-year QB Ben Roethlisberger.',21,10,'Ford Field','Detroit','MI','2006-02-05',68206,'XL','The Rolling Stones','451548898230677504','p5YA9Ah2Z1Y',42.34,-83.0456);
INSERT INTO "idb_superbowl" VALUES(3,7,10,7,'25/38 247 YDS 1 TD 1 INT
1 CAR 0 YDS','Peyton Manning led the Indianapolis Colts to their second Super Bowl championship.

Manning capped off a season in which he threw 31 TD and only 9 INT by throwing for 1 TD and 1 INT',29,17,'Dolphin Stadium','Miami Gardens','FL','2007-02-04',74512,'XLI','Prince','451549050467135488','8cVMzkCIV6E',29.9581,-80.2389);
INSERT INTO "idb_superbowl" VALUES(4,3,8,3,'19/34 255 YDS 2 TD 1 INT
3 CAR 4 YDS','Eli Manning and the Giants upset the heavily favored Patriots on a late game heave to WR David Tyree.

His 2 fourth quarter TDs lifted the Giants over the Patriots, who had yet to lose a game that season.',17,14,'University of Phoenix Stadium','Glendale','AZ','2008-02-03',71101,'XLII','Tom Petty and the Heartbreakers','451549401190629377','0o8XmdQ7Zjo',33.5275,-112.2625);
INSERT INTO "idb_superbowl" VALUES(5,6,11,6,'9 REC 131 YDS 1 TD 13 TGTS','Santonio Holmes game winning 6 yd TD catch resulted in the Steelers'' sixth Super Bowl championship.

The catch was one of the all time greats in SB history, and was one of his nine spectacular receptions that game.',27,23,'Raymond James Stadium','Tampa','FL','2009-02-01',70774,'XLIII','Bruce Springsteen and the E Street Band','451549592362811392','PzDawiYEpFU',27.9758,-82.5033);
INSERT INTO "idb_superbowl" VALUES(6,5,7,5,'32/39 288 YDS 2 TD 0 INT
1 CAR -1 YDS','Four years after Hurricane Katrina devastated New Orleans, Drew Brees led the Saints to their first Super Bowl championship.

His 32 completions tied Tom Brady''s record for the most in Super Bowl history.',31,17,'Sun Life Stadium','Miami Gardens','FL','2010-02-07',74059,'XLIV','The Who','451549854502637568','M1OIISkx9Hk',25.9581,-80.2389);
INSERT INTO "idb_superbowl" VALUES(7,4,6,4,'24/39 304 YDS 3 TD 0 INT
 2 CAR -2 YDS','In his third year as a starter for the Green Bay Packers, Rodgers calmly led the team its fourth Super Bowl championship.

His 3 TDs reminded fans of the retired Brett Favre and ensured Packers fans of success in years to come.',31,25,'Cowboys Stadium','Arlington','TX','2011-02-06',103219,'XLV','The Black Eyed Peas','451550049890074624','bKMVg7p5rto',32.7478,-97.0928);
INSERT INTO "idb_superbowl" VALUES(8,3,8,3,'30/40 296 YDS 1 TD 0 INT
1 CAR -1 YDS','Once again, Eli Manning played spoiler to the New England Patriots and won his second SB MVP award.

He started the game completing his first 9 attempts becoming the first quarterback to do so and put together a crucial drive with 3 1/2 minutes left that sealed the victory for the Giants.',21,17,'Lucas Oil Stadium','Indianapolis','IN','2012-02-05',68658,'XLVI','Madonna','451550367377928192','8eJapFSnICI',39.7601,-861638.0);
INSERT INTO "idb_superbowl" VALUES(9,2,12,2,'22/33 287 YDS 3 TD 0 INT
0 CAR 0 YDS','Joe Flacco capped his spectacular postseason with an impressive performance against a 49er defense that was considered one of the league''s best.

While all 3 TDs were in the first half, Flacco coolly converted third down after third down to hold off a late 49er surge.',34,31,'Mercedes-Benz Superdome','New Orleans','LA','2013-02-03',71024,'XLVII','Beyonce','451550572752015360','ynQApEB4VXg',29.9508,-90.0811);
INSERT INTO "idb_superbowl" VALUES(10,1,13,1,'1 INT 1 FR 1 TD 9 T','Malcolm Smith was the de-facto SB MVP for a legendary Seattle defense.

While he was a relative unknown at the start of the season, a game-sealing interception in the NFC Championship as well as two takeaways in the Super Bowl served as a coming out party for the young linebacker.',43,8,'MetLife Stadium','East Rutherford','NJ','2014-02-02',82529,'XLVIII','Bruno Mars','446419923376418818','NbcA1UISfG0',40.8136,-74.0744);
INSERT INTO "idb_superbowl" VALUES(11,8,14,10,'32/48 354 YDS 3 TD 1 INT
2 CAR 12 YDS','Tom Brady led the Patriots to victory while winning his second Super Bowl MVP.

His 32 completions are the most in SB history and his 354 yds are the 5th best total in SB history.',32,29,'Reliant Stadium','Houston','TX','2004-02-01',71525,'XXXVIII','Janet Jackson','451553657423527936','7CCWCWOUf',29.6847,-95.4108);

COMMIT;

