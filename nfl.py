import nflgame

class Game:
	def __init__ (self, home, away, homeScore, awayScore, homeTimeout, awayTimeout):
		self.home=home
		self.away=away
		self.homeScore=homeScore
		self.awayScore=awayScore
		self.homeTimeout=homeTimeout
		self.awayTimeout=awayTimeout


	def standard_team(team):
		teams=nflgame.standard_team()
		team = team.lower()
		for variants in teams:
			for variant in variants:
				if team == variant.lower():
					return variants[0]
					return None


homeTeam=nflgame.standard_team("texans")
awayTeam=nflgame.standard_team("broncos")

print homeTeam +" vs "+ awayTeam

game1= Game(homeTeam, awayTeam, 0,0,3,3)


class Drive:
	def __init__ (self, possession, number, playType, yardage, touchdown, penalty, timeout, turnover):
		self.possession= possession
		self.number= number
		self.playType= playType
		self.yardage= yardage
		self.touchdown= touchdown
		self.penatly= penalty
		self.timeout= timeout
		self.turnover=turnover

	def find(name, team=None):
		players=nflgame.combine()
		hits = []
		for player in players.itervalues():
			if player.name.lower() == name.lower():
				if team is None or team.lower() == player.team.lower():
					hits.append(player)
					return hits




first= Drive(game1.home, "case keenum", "pass", 34, 0, 0,1,0)

player1=nflgame.find(first.number)
for p in player1:
	player=p


if first.playType=="pass":
	type=" passed"
else:
	type=" ran"

print str(player) +type + " the ball for " +str(first.yardage) + " yards."

if first.touchdown==1:
	game1.homeScore+=7
	print "Touchdown"
	print game1.home +": "+ str(game1.homeScore)
	print game1.away + ": " +str(game1.awayScore)

if first.turnover==1:
	print "Turnover!"

if first.timeout==1:
	game1.homeTimeout=game1.homeTimeout-1
	print game1.home + " has called a timeout. They have " + str(game1.homeTimeout)+ " timeouts left."

print str(first.possession) +" has the ball."






