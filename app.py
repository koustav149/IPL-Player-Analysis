import streamlit as st
import pandas as pd
import preprocessor,helper
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px

ipl_df = pd.read_csv('IPL Matches 2008-2020.csv')
ipl_ball_by_ball = pd.read_csv("IPL Ball-by-Ball 2008-2020.csv")
ipl_runs = pd.read_csv('Most Runs All Seasons Combine.csv')

fastest_fifty_df = pd.read_csv('Fastest Fifties All Seasons Combine.csv')

ipl_wickets = pd.read_csv('Most Wickets All Seasons Combine.csv')
df = preprocessor.preprocess(ipl_df)
st.sidebar.image("ipl_logo.jpg")
st.sidebar.title('IPL Analysis (2008-2020)')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Team-wise Performance', 'Batsman Analysis', 'Bowler Analysis')
)


if user_menu == 'Team-wise Performance':
    st.sidebar.header('IPL Teams')
    years,teams = helper.year_team_list(ipl_df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_team = st.sidebar.selectbox("Select Team",teams)

    ipl_team = helper.fetch_team_performance(ipl_df,selected_year,selected_team)

    if selected_year == 'Overall' and selected_team == 'Overall':
       st.title('Overall Analysis')
    if selected_year != 'Overall' and selected_team == 'Overall':
        st.title('IPL - ' + str(selected_year) + ' Analysis')
    if selected_year != 'Overall' and selected_team != 'Overall':
        st.title(selected_team + " in IPL " + str(selected_year))
    if selected_year == 'Overall' and selected_team != 'Overall':
        st.title('Overall performance of ' + selected_team )
    ipl_team.reset_index(inplace=True)
    ipl_team.drop(columns=['index'],inplace=True)
    st.table(ipl_team)

    if selected_team == "Mumbai Indians":
        st.subheader("Current Players of " + selected_team)
        image = Image.open("MI_team.jpeg")
        st.image(image)

    if selected_team == "Chennai Super Kings":
        st.subheader("Current Players of " + selected_team)
        image = Image.open("CSK_team.jpeg")
        st.image(image)

    if selected_team == "Kolkata Knight Riders":
        st.subheader("Current Players of " + selected_team)
        image = Image.open("KKR_team.jpeg")
        st.image(image)

    if selected_team == "Rajasthan Royals":
        st.subheader("Current Players of " + selected_team)
        image = Image.open("RR_team.jpeg")
        st.image(image)

    if selected_team == "Sunrisers Hyderabad":
        st.subheader("Current Players of " + selected_team)
        image = Image.open("SRH_team.jpeg")
        st.image(image)

    if selected_team == "Royal Challengers Bangalore":
        st.subheader("Current Players of " + selected_team)
        image = Image.open("RCB_team.jpeg")
        st.image(image)

    if selected_team == "Kings XI Punjab":
        st.subheader("Current Players of " + selected_team)
        image = Image.open("KIXP_team.jpeg")
        st.image(image)


    if selected_team == "Delhi Capitals" or selected_team =="Delhi Daredevils":
        st.subheader("Current Players of " + selected_team)
        image = Image.open("DD_team.jpeg")
        st.image(image)                      

    if selected_team == "Deccan Chargers" or selected_team =="Kochi Tuskers Kerala" or selected_team =="Pune Warriors" or selected_team =="Gujarat Lions" or selected_team =="Rising Pune Supergiant":
        st.subheader("This team do not play in the IPL anymore")


    st.markdown("""---""")
    image = Image.open("toss_dicission.png")
    st.image(image)

    st.markdown("""---""")
    image = Image.open("toss_win_match_win.png")
    st.image(image)


    st.markdown("""---""")
    image = Image.open("top_10_host.png")
    st.image(image)


    st.markdown("""---""")
    image = Image.open("umpire.png")
    st.image(image)





if user_menu == "Batsman Analysis":
    years = helper.year_list(ipl_df)


    selected_year = st.sidebar.selectbox("Select Year",years)
    st.title("Top Batting Stats of IPL - " + str(selected_year))

    st.markdown("""---""")

    if selected_year == "Overall":
        col1, col2 = st.columns(2)
        with col1:
            st.header("Most Runs")
            st.subheader(ipl_ball_by_ball.groupby('batsman').batsman_runs.sum().sort_values(ascending=False).index[:1].values[0])
        with col2:
            st.header("Highest Avg")
            st.subheader(ipl_runs.groupby('Player')['Avg'].median().sort_values(ascending=False).index[:1].values[0])

        col1, col2 = st.columns(2)
        with col1:
            st.header("Most 6s")
            st.subheader(ipl_runs.groupby('Player')['6s'].sum().sort_values(ascending=False).index[:1].values[0])
        with col2:
            st.header("Fastest Fifty")
            st.subheader('KL Rahul')






    if selected_year != 'Overall':
        most_runs = helper.most_runs_year(ipl_runs, selected_year)
        best_sr = helper.best_sr_year(ipl_runs, selected_year)
        highest_avg = helper.best_avg_year(ipl_runs, selected_year)
        most_6s = helper.most_6s_year(ipl_runs, selected_year)
        fastest_fifty = helper.fastest_fifty(fastest_fifty_df, selected_year)
        col1,col2 = st.columns(2)
        with col1:
          st.header("Most Runs")
          st.subheader(most_runs)
        with col2:
          st.header("Highest Avg")
          st.subheader(highest_avg)

        col1,col2 = st.columns(2)
        with col1:
          st.header("Most 6s")
          st.subheader(most_6s)
        with col2:
          st.header("Fastest Fifty")
          st.subheader(fastest_fifty)


    st.markdown("""---""")

    st.title("IPL(2008-2020) Overall Analysis")
    st.markdown("""---""")

    st.subheader("Top Run Scorers in IPL :")

    top_batsmans = ipl_ball_by_ball.groupby('batsman').batsman_runs.sum().sort_values(ascending=False)[:10]
    fig = plt.figure(figsize=(12, 6))
    sns.barplot(x=top_batsmans.values, y=top_batsmans.index, palette="mako")
    plt.rcParams['font.size'] = 14
    plt.xlabel("Runs")
    plt.ylabel("Batsman")
    st.pyplot(fig)

    st.markdown("""---""")

    st.subheader("Top 10 Six Hitters in IPL :")
    top_6_hitters = ipl_runs.groupby('Player')['6s'].sum().sort_values(ascending=False)[:10]
    fig = plt.figure(figsize=(12,6))
    sns.barplot(x=top_6_hitters.values,y=top_6_hitters.index,palette="magma")
    plt.rcParams['font.size'] = 14
    plt.xlabel("6s")
    plt.ylabel("Batsman")
    st.pyplot(fig)


    st.markdown("""---""")

    image = Image.open('run_over_the_year.png')
    st.image(image, caption='Total per Season Over the Year')

    st.markdown("""---""")

    image = Image.open("best_batting_in_a_match.png")
    st.image(image, caption="Best Batting Performance in a Match")

    st.markdown("""---""") 







if user_menu == "Bowler Analysis":
    years = helper.year_list(ipl_df)


    selected_year = st.sidebar.selectbox("Select Year",years)
    st.title("Top Bowling Stats of IPL - " + str(selected_year))

    st.markdown("""---""")

    if selected_year == "Overall":
        col1, col2 = st.columns(2)
        with col1:
            st.header("Most Wickets")
            st.subheader("Dwayne Bravo")
        with col2:
            st.header("Best Economy")
            st.subheader("Rashid Khan")

        col1, col2 = st.columns(2)
        with col1:
            st.header("Best Avg")
            st.subheader("Dwayne Bravo")
        with col2:
            st.header("Best Bowling Figures")
            st.subheader('Alzarri Joseph')


    if selected_year != "Overall":

     most_wickets = helper.most_wickets(ipl_wickets,selected_year)
     best_economy = helper.best_economy(ipl_wickets,selected_year)
     best_avg = helper.best_avg(ipl_wickets,selected_year)
     best_bowling_figure = helper.best_bowling_figure(ipl_wickets,selected_year)

     col1, col2 = st.columns(2)
     with col1:
        st.header("Most Wickets")
        st.subheader(most_wickets)
     with col2:
        st.header("Best Economy")
        st.subheader(best_economy)

     col1, col2 = st.columns(2)
     with col1:
        st.header("Best Avg")
        st.subheader(best_avg)
     with col2:
        st.header("Best Bowling Figure")
        st.subheader(best_bowling_figure)

    st.markdown("""---""")
    st.title("IPL(2008-2020) Overall Analysis")

    st.markdown("""---""")
    st.subheader("Top 10 Wicket Takers in IPL:")
    top_bowler = ipl_ball_by_ball.groupby('bowler').is_wicket.sum().sort_values(ascending=False)[:10]
    fig = plt.figure(figsize=(12, 6))
    sns.barplot(x=top_bowler.values, y=top_bowler.index, palette="mako")
    plt.rcParams['font.size'] = 14
    plt.xlabel("Wickets")
    plt.ylabel("Bowlers")
    st.pyplot(fig)

    st.markdown("""---""")
    
    image = Image.open("top_dissmisal_kind.png")
    st.image(image, caption="top_dissmisal_kind")

    st.markdown("""---""")

    image = Image.open("best_bawling_in_a_match.png")
    st.image(image, caption="Best Bowling Performance in a Match")

    st.markdown("""---""")

    