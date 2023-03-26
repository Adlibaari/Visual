import pandas as pd
import plotly.express as px
import streamlit as st

with st.sidebar:
      Size = st.selectbox(
      'Size',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'))
      Color = st.selectbox(
      'Color',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'))
      Circle_area = st.slider('Circle Area', 0, 100, 60)

      st.write('Size:', Size)
      st.write('Color:', Color)
      st.write("Circle Area:", Circle_area)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

url = 'https://raw.githubusercontent.com/Adlibaari/Visual/main/factbook.csv'
Data = pd.read_csv(url, index_col=0)

with col1:
      X1 = st.selectbox(
      'X',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'), key='Chart1')
      Y1 = st.selectbox(
      'Y',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'), key='Chart2')
      fig = px.scatter(data_frame=Data,x=X1, y=Y1,size =Size,color=Color,log_x=True,log_y=True,size_max=Circle_area, hover_name="Country", hover_data=['  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'])
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:
      X2 = st.selectbox(
      'X',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'), key='Chart3')
      Y2 = st.selectbox(
      'Y',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'),  key='Chart4')
      fig = px.scatter(data_frame=Data,x=X2, y=Y2,size =Size,color=Color,log_x=True,log_y=True,size_max=Circle_area, hover_name="Country", hover_data=['  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'])
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col3:
      X3 = st.selectbox(
      'X',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'), key='Chart5')
      Y3 = st.selectbox(
      'Y',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'),  key='Chart6')
      fig = px.scatter(data_frame=Data,x=X3, y=Y3,size =Size,color=Color,log_x=True,log_y=True,size_max=Circle_area, hover_name="Country", hover_data=['  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'])
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col4:
      X4 = st.selectbox(
      'X',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'), key='Chart7')
      Y4 = st.selectbox(
      'Y',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'), key='Chart8')
      fig = px.scatter(data_frame=Data,x=X4, y=Y4,size =Size,color=Color,log_x=True,log_y=True,size_max=Circle_area, hover_name="Country", hover_data=['  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'])
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)


