import pandas as pd


def fetch_team_performance(ipl_df2, year, team):
    if year == "Overall" and team == "Overall":
        temp_df = ipl_df2
    if year == "Overall" and team != "Overall":
        temp_df = ipl_df2[(ipl_df2.team1 == team) | (ipl_df2.team2 == team)]
    if year != "Overall" and team == "Overall":
        temp_df = ipl_df2[ipl_df2.date == int(year)]
    if year != "Overall" and team != "Overall":
        temp_df = ipl_df2[((ipl_df2.team1 == team) | (ipl_df2.team2 == team)) & (ipl_df2.date == year)]
    d = []
    ipl_team_list = temp_df.team1.unique().tolist()
    if team == 'Overall' and year == 'Overall':
        for team in ipl_team_list:
            d.append({'Team': team,
                      'Number of Matches': len(temp_df[(temp_df.team1 == team) | (temp_df.team2 == team)]),
                      'Won': temp_df[temp_df.winner == team].winner.count(),
                      'Lost/No Result': len(temp_df[(temp_df.team1 == team) | (temp_df.team2 == team)]) - (
                          temp_df[temp_df.winner == team].winner.count()),
                      'Win Percentage(%)': int((temp_df[temp_df.winner == team].winner.count() / len(
                          temp_df[(temp_df.team1 == team) | (temp_df.team2 == team)])) * 100)
                      })
        team_df = pd.DataFrame(d)
        Trophies = [0, 0, 0, 5, 2, 1, 1, 3, 0, 0, 1, 0, 0, 0]
        team_df['Trophies'] = Trophies
        team_df.sort_values('Trophies', ascending=False, inplace=True)
        return team_df
        team = 'Overall'
    if team == 'Overall' and year != 'Overall':
        for team in ipl_team_list:
            d.append({'Team': team,
                      'Number of Matches': len(temp_df[(temp_df.team1 == team) | (temp_df.team2 == team)]),
                      'Won': temp_df[temp_df.winner == team].winner.count(),
                      'Lost/No Result': len(temp_df[(temp_df.team1 == team) | (temp_df.team2 == team)]) - (
                          temp_df[temp_df.winner == team].winner.count()),
                      'Win Percantage(%)': int((temp_df[temp_df.winner == team].winner.count() / len(
                          temp_df[(temp_df.team1 == team) | (temp_df.team2 == team)])) * 100)
                      })
        team_df = pd.DataFrame(d)
        team_df.sort_values('Won', ascending=False, inplace=True)
        return team_df
        team = "Overall"
    if team != 'Overall':
        d.append({'Team': team,
                  'Number of Matches': len(temp_df[(temp_df.team1 == team) | (temp_df.team2 == team)]),
                  'Won': temp_df[temp_df.winner == team].winner.count(),
                  'Lost/No Result': len(temp_df[(temp_df.team1 == team) | (temp_df.team2 == team)]) - (
                      temp_df[temp_df.winner == team].winner.count()),
                  'Win Percantage(%)': int((temp_df[temp_df.winner == team].winner.count() / len(
                      temp_df[(temp_df.team1 == team) | (temp_df.team2 == team)])) * 100)
                  })
        team_df = pd.DataFrame(d)
        team_df.sort_values('Won', ascending=False, inplace=True)
        return team_df


def ipl_teams(ipl_df):
    ipl_team_list = ipl_df.team1.unique().tolist()
    d = []
    for team in ipl_team_list:
        d.append({'Team': team,
                  'Number of Matches': len(ipl_df[(ipl_df.team1 == team) | (ipl_df.team2 == team)]),
                  'Won': ipl_df[ipl_df.winner == team].winner.count(),
                  'Lost': len(ipl_df[(ipl_df.team1 == team) | (ipl_df.team2 == team)]) - (
                      ipl_df[ipl_df.winner == team].winner.count()),
                  'Win Percentage(%)': int((ipl_df[ipl_df.winner == team].winner.count() / len(
                      ipl_df[(ipl_df.team1 == team) | (ipl_df.team2 == team)])) * 100)
                  })
    team_df = pd.DataFrame(d)
    team_df['Win Percentage(%)'] = team_df['Win Percentage(%)'].astype(int)
    Trophies = [0, 0, 0, 5, 2, 1, 1, 3, 0, 0, 1, 0, 0, 0]
    team_df['Trophies'] = Trophies
    team_df.rename(columns={'Lost': 'Lost/No Result'}, inplace=True)
    team_df.sort_values('Trophies', ascending=False, inplace=True)
    return team_df
def year_team_list(ipl_df):
    ipl_df['date'] = pd.DatetimeIndex(ipl_df['date']).year
    Years = ipl_df.date.unique().tolist()
    Years.insert(0,'Overall')
    Ipl_team_list = ipl_df.team1.unique().tolist()
    Ipl_team_list.insert(0,'Overall')
    return Years,Ipl_team_list
def year_list(ipl_df):
    ipl_df['date'] = pd.DatetimeIndex(ipl_df['date']).year
    Years = ipl_df.date.unique().tolist()
    Years.insert(0, 'Overall')
    return Years
# most runs in a season
def most_runs_year(df,Year):
    return df[df.Year == Year].Player[:1].values[0]

# best avg in a season
def best_avg_year(df,Year):
    return df[df.Year == Year].sort_values('Avg',ascending=False).Player[:1].values[0]

# Best SR in a season
def best_sr_year(df,Year):
    return df[df.Year == Year].sort_values('SR',ascending=False).Player[:1].values[0]

# highest number of sixes
def most_6s_year(df,Year):
    return df[df.Year == Year].sort_values('6s',ascending=False).Player[:1].values[0]

#fastest fifty
def fastest_fifty(df,Year):
    return df[df.Year == Year].Player[:1].values[0]

# most wickets
def most_wickets(df,Year):
    return df[df.Year == Year].Player[:1].values[0]

# Best economy
def best_economy(df,Year):
    return df[(df.Ov>= 40) & (df.Year == Year)].sort_values('Econ',ascending=True).Player[:1].values[0]

#best avg
def best_avg(df,Year):
    return df[(df.Ov>= 40) & (df.Year == Year)].sort_values('Avg',ascending=True).Player[:1].values[0]

#best bowling figures
def best_bowling_figure(df,Year):
    return df[(df.Ov>= 40) & (df.Year == Year)].sort_values(by=['5w','4w'],ascending=True).Player[:1].values[0]

# top 10 run scorer
def top_batsman(df):
    top_batsmans = df.groupby('batsman').batsman_runs.sum().sort_values(ascending=False)[:10]
    return top_batsman