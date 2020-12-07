import numpy as np
import pandas as pd
import re

match = pd.read_json('./data/match.json')
team = pd.read_csv('./data/team.csv')

match = pd.merge(match, team, left_on='home_team_api_id',
                 right_on='team_api_id')
match = pd.merge(match, team, left_on='away_team_api_id',
                 right_on='team_api_id')

final_list = []
match1 = match
# for df_row in range(2):
for df_row in range(match1['home_team_api_id'].shape[0]):
    team1 = match1['home_team_api_id'].iloc[df_row]
    team2 = match1['away_team_api_id'].iloc[df_row]
    team1_matches = match1[(match1['home_team_api_id'] == team1) | (
        match1['away_team_api_id'] == team1)]
    team1_matches['match_api_id'] = 1
    team2_matches = match1[(match1['home_team_api_id'] == team2) | (
        match1['away_team_api_id'] == team2)]
    team2_matches['match_api_id'] = 1
    spec_match = match1[match1['match_api_id']
                        == match1['match_api_id'].iloc[df_row]]
    stats = ['goal', 'shoton', 'shotoff',
             'foulcommit', 'card', 'cross', 'corner']
    a = str(team1)
    b = str(team2)
    home_list = []
    away_list = []
    for i in stats:
        try:
            spec_match.fillna('')
            split_up = re.split('>|<', spec_match[i].iloc[0])
            a = str(spec_match['home_team_api_id'].iloc[0])
            b = str(spec_match['away_team_api_id'].iloc[0])
            home_stats = 0
            away_stats = 0
            for i in split_up:
                if a in i:
                    home_stats += 1

                if b in i:
                    away_stats += 1
        except Exception:
            home_stats = 0
            away_stats = 0
        home_list.append(home_stats)
        away_list.append(away_stats)
    try:
        split_up2 = re.split('<homepos>|</homepos>',
                             spec_match['possession'].iloc[0])
    except Exception:
        split_up2 = [1]
    try:
        home_poss = split_up2[7]
    except IndexError:
        home_poss = 0
    home_poss = int(home_poss)
    home_list.append(home_poss)
    try:
        split_up3 = re.split('<awaypos>|</awaypos>',
                             spec_match['possession'].iloc[0])
    except Exception:
        split_up3 = [0]
    try:
        away_poss = split_up3[7]
    except IndexError:
        away_poss = 0
    away_poss = int(away_poss)
    away_list.append(away_poss)
    home_list.extend(away_list)
    temp = [match1['match_api_id'].iloc[df_row]]
    temp.extend(home_list)
    final_list.append(temp)
comp_stats = pd.DataFrame(final_list, columns=['match_id', 'Home_Goals', 'Home_Shots_on_Goal', 'Home_Shots_off_Goal', 'Home_Fouls_Committed', 'Home_Yellow_Red_Cards', 'Home_Crosses', 'Home_Corner_Kicks',
                                               'Home_Possessions', 'Away_Goals', 'Away_Shots_on_Goal', 'Away_Shots_off_Goal', 'Away_Fouls_Committed', 'Away_Yellow_Red_Cards', 'Away_Crosses', 'Away_Corner_Kicks', 'Away_Possessions'])
comp_stats.to_csv(r'./match_stats.csv', index=False)
