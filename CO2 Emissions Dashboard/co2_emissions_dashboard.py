import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and width
st.set_page_config(page_title='CO₂ Emissions Dashboard', page_icon=':chart_with_upwards_trend:', layout='wide')

# Set app header
st.header('CO₂ Emissions Dashboard')

# Load data from GitHub
url = 'https://raw.githubusercontent.com/lk-learner/Streamlit-deployment/main/CO2%20Emissions%20Dashboard/Data/countries_df.csv'
df = pd.read_csv(url, usecols=['Entity', 'Year', 'Code', 'Annual CO₂ emissions'])

# Convert 'Year' column to Python int
df['Year'] = df['Year'].astype(int)

# Create a slider to select a year
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
selected_year = st.slider('Select a year', min_value=min_year, max_value=max_year, value=min_year)

# Filter data for the selected year
data = df[df['Year'] == selected_year]

# Create two columns for the charts
col1, col2 = st.columns(2)

# Add choropleth map to the first column
with col1:
    fig = px.choropleth(data_frame=data,
                        locations='Code',
                        color='Annual CO₂ emissions',
                        hover_name='Entity',
                        title=f'CO₂ Emissions Map ({selected_year})')
    st.plotly_chart(fig)

# Add bar chart to the second column
with col2:
    # Create a selectbox to select countries
    countries = st.multiselect('Select one or more countries', options=data['Entity'].unique())

    # Filter data for selected countries
    data = data[data['Entity'].isin(countries)]

    fig = px.bar(data_frame=data,
                 x='Entity',
                 y='Annual CO₂ emissions',
                 color='Entity',
                 title=f'CO₂ Emissions Bar Chart ({selected_year})')
    st.plotly_chart(fig)