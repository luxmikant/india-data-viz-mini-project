import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
df = pd.read_csv('india.csv')

list_of_state = list(df['State'].unique())

list_of_state.insert(0,'Overall India')

st.sidebar.title('india visualization')

selected_state = st.sidebar.selectbox('select a state',list_of_state)
primary = st.sidebar.selectbox('select primary parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('select secondary parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('plot Graph')

if plot:
    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)
