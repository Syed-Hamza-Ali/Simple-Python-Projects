import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.offline as pyo
import plotly.graph_objs as go

import preprocessor
import helper


df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df, region_df)

st.sidebar.header('Olympics Analysis')
st.sidebar.image('olympc.png')

user = st.sidebar.radio(
    'Select an option',
    ('Medal wise', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)
#st.dataframe(df)
if user == 'Medal wise':
    st.sidebar.header('Medal_tally')
    year, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year", year)
    selected_country = st.sidebar.selectbox("Select Country", country)
    #medal_tally = helper.medals_tally(df)
    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_country=='Overall' and selected_year=='Overall':
        st.title("Overall Tally")
    elif selected_country=='Overall' and selected_year!='Overall':
        st.title(f"Medal-Tally in {selected_year} Olympics")
    elif selected_country!='Overall' and selected_year=='Overall':
        st.title(f"{selected_country}'s  Overall Tally")
    elif selected_country!='Overall' and selected_year!='Overall':
        st.title(f"{selected_country} Performance in {selected_year} Olympics")
    st.table(medal_tally)
    st.title(f"Total Medals of {selected_country}")
    country_total=helper.total_medal_region(df,selected_country)
    st.table(country_total)
if user=='Overall Analysis':
    editions=df['Year'].unique().shape[0]-1
    cities=df['City'].unique().shape[0]
    events=df['Event'].unique().shape[0]
    sports=df['Sport'].unique().shape[0]
    atheletes=df['Name'].unique().shape[0]
    region=df['region'].unique().shape[0]
    st.title('Top Statitics')
    col1,col2,col3=st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Nations')
        st.title(region)
    with col3:
        st.header('Athletes')
        st.title(atheletes)

    nations_over_time=helper.data_overtime(df,'region')
    fig = px.line(nations_over_time, x="Editions", y='region')
    st.title("Participating Nations Over Time")
    st.plotly_chart(fig)

    events_over_time = helper.data_overtime(df, 'Event')
    fig = px.line(events_over_time, x="Editions", y="Event")
    st.title("Events Over Time")
    st.plotly_chart(fig)

    athelete_over_time = helper.data_overtime(df, 'Name')
    fig = px.line(athelete_over_time, x="Editions", y="Name")
    st.title("Athletes Over Time")
    st.plotly_chart(fig)
    st.title('No.of Events over time(Every Sport)')
    fig,ax=plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax=sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int),
                annot=True)
    st.pyplot(fig)

    st.title('Most Successful Athletes')
    sports_list=df['Sport'].unique().tolist()
    sports_list.sort()
    sports_list.insert(0,'Overall')
    selected_sport=st.selectbox('Select a Sport',sports_list)

    X=helper.most_successful(df,selected_sport)
    st.table(X)
if user=='Country-wise Analysis':
    st.sidebar.title('Country-Wise Analysis')
    country_list=df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_Country = st.sidebar.selectbox('Select a Country', country_list)

    country_over_year=helper.country_wise(df,selected_Country)
    fig = px.line(country_over_year, x="Year", y="Medal")
    st.title(f"{selected_Country} Over Time")
    st.plotly_chart(fig)

    st.title(f"{selected_Country} excel's in following Sports ")
    pt=helper.country_heatmap(df,selected_Country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title(f'Top 10  Athletes of {selected_Country}')
    Y = helper.most_successful_conrtywise(df, selected_Country)
    st.table(Y)

    sport_list = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                  'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                  'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                  'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                  'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                  'Tennis', 'Golf', 'Softball', 'Archery',
                  'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                  'Rhythmic Gymnastics', 'Rugby Sevens',
                  'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    f_country_list = df['region'].dropna().unique().tolist()
    f_country_list.sort()
    s_country_list = df['region'].dropna().unique().tolist()
    s_country_list.sort()

    st.title("Competitive Analysis of Countries")

    first_Country = st.selectbox('Select first Country', f_country_list,key=1)
    second_Country = st.selectbox('Select second Country', s_country_list,key=2)

    all_sport_list=helper.total_sports(df)
    select_sport=st.selectbox('Select a Sport', all_sport_list,key=3)

    comp_stats=helper.comp_tally(df,first_Country,second_Country,select_sport)
    st.table(comp_stats)

    graph_a,graph_b=helper.comp_graph(df,first_Country,second_Country,select_sport)
    trace = go.Bar(x=graph_a['Sport'], y=graph_a['Total'], name=first_Country, marker={'color': '#00a65a'})
    trace1 = go.Bar(x=graph_b['Sport'], y=graph_b['Total'], name=second_Country, marker={'color': '#a6a65a'})
    data = [trace, trace1]
    layout = go.Layout(title='Medal wise',
                       xaxis={'title': 'Sports'},
                       yaxis={'title': 'Medals'})
    fig = go.Figure(data=data, layout=layout)
    st.title('Comparison via Bar graph')
    st.plotly_chart(fig)

if user=='Athlete-wise Analysis':
    athele_df = df.drop_duplicates(subset=['Name', 'region'])
    x1 = athele_df['Age'].dropna()
    x2 = athele_df[athele_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athele_df[athele_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athele_df[athele_df['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title('Distribution of Age')
    st.plotly_chart(fig)

    PM = []
    name = []
    sport_list = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                  'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                  'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                  'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                  'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                  'Tennis', 'Golf', 'Softball', 'Archery',
                  'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                  'Rhythmic Gymnastics', 'Rugby Sevens',
                  'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']


    medal_list=['Gold','Silver']
    #selected_medal = st.sidebar.selectbox('Select a Medal', medal_list)
    for sport in sport_list:
        temp_df = athele_df[athele_df['Sport'] == sport]
        PM.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)
    fig = ff.create_distplot(PM, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title('Distribution of Age wrt Sports')
    st.plotly_chart(fig)

    st.title('Height vs Weight')
    selected_sport=st.selectbox('Select a Sport',sport_list)
    temp_df=helper.weight_height(df,selected_sport)
    fig, ax = plt.subplots()
    ax=sns.scatterplot(temp_df,x=temp_df['Weight'],y=temp_df['Height'],hue=temp_df['Medal'],size=100,style=temp_df['Sex'])
    st.pyplot(fig)

    st.title('Men Vs Women Participation Over the Years')
    final=helper.men_x_women(df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)