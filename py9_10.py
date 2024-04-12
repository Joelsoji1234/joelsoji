import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample football DataFrame
football_data = {
    'Team': ['Arsenal', 'Chelsea', 'Liverpool', 'Manchester United', 'Manchester City'],
    'Wins': [20, 25, 30, 18, 28],
    'Losses': [10, 8, 5, 12, 6]
}
df_football = pd.DataFrame(football_data)

# Title of the web app
st.title('Football Team Statistical Analysis')

# Sidebar for user input
st.sidebar.title('Options')
selected_option = st.sidebar.selectbox(
    'Select a statistical representation:',
    ('Bar Plot', 'Pie Chart', 'Box Plot')
)

# Based on user selection, display the corresponding plot
if selected_option == 'Bar Plot':
    st.subheader('Bar Plot')
    st.bar_chart(df_football.set_index('Team'))

elif selected_option == 'Pie Chart':
    st.subheader('Pie Chart')
    fig, ax = plt.subplots()
    ax.pie(df_football['Wins'], labels=df_football['Team'], autopct='%1.1f%%')
    st.pyplot(fig)

elif selected_option == 'Box Plot':
    st.subheader('Box Plot')
    st.write('This is a box plot representation of the data:')
    sns.boxplot(data=df_football.melt(id_vars='Team', var_name='Result', value_name='Count'), x='Team', y='Count', hue='Result')
    st.pyplot()

# Some statistical data representation
st.write('Here are some basic statistics:')
st.write(df_football.describe())
