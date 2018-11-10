import operator
import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

'''Read in matchinfo.csv as our dataset'''

match_info_file = open('data/leagueoflegends/matchinfo.csv')
match_info = csv.reader(match_info_file)

'''Preparing my empty graph'''
G = nx.DiGraph()
'''
This will be a dictionary of all games that have been played.
The keys will be team names. Each value is a dictionary.
The subdictionaries keys will be team names that have played the
superdictionary team and the subdictionary value will be the number
of times that the superdictionary team has beaten the subdictionary team
'''
team_history = {}

rownum = 0

for row in match_info:	
	
	if rownum == 0:
		rownum += 1 #this is just a factor to skip the first line
	else:

		blueTeam = row[4]
		redTeam = row[7]
		
		'''This initiates the subdictionaries'''
		if blueTeam not in team_history:
			team_history[blueTeam] = {}
		if redTeam not in team_history:
			team_history[redTeam] = {}

		blueWin = row[5]

		'''These conditions assign victory values in subdictionaries'''
		if blueWin:
			if redTeam not in team_history[blueTeam]:
				team_history[blueTeam][redTeam] = 1
				team_history[redTeam][blueTeam] = 0
			else:
				team_history[blueTeam][redTeam] += 1
		else:
			if blueTeam not in team_history[redTeam]:
				team_history[redTeam][blueTeam] = 1
				team_history[blueTeam][redTeam] = 0
			else:
				team_history[redTeam][blueTeam] += 1

'''This sets up the weights between each team to be their W/L ratios'''

for team in team_history:
	for counterTeam in team_history[team]:
		w = team_history[team][counterTeam]
		l = team_history[counterTeam][team]
		if l != 0:
			G.add_edge(team, counterTeam, weight=float(w / l))
		else:
			G.add_edge(team, counterTeam, weight=100.0)

print(G['CREW'])
print(G['D9'])
print(G['RED'])
print(G['ONE'])

ranks = {}

for team in G:
	ranks[team] = sum([np.log(G[team][n]['weight']+1) for n in G[team]])

ranks = sorted(ranks.items(), key=operator.itemgetter(1))
print(ranks)
