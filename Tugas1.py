import pandas as pd
import plotly.express as px
import streamlit as st

url = 'https://raw.githubusercontent.com/Adlibaari/Visual/main/factbook.csv'
Data = pd.read_csv(url)

with st.sidebar:
      Size = st.selectbox(
      'Size',
      (Data.columns.values))
      Color = st.selectbox(
      'Color',
      (Data.columns.values))
      Circle_area = st.slider('Circle Area', 0, 100, 60)

with st.sidebar:
      Size = st.selectbox(
      'Size',
      (Data.columns.values))
      Color = st.selectbox(
      'Color',
      (Data.columns.values))
      Circle_area = st.slider('Circle Area', 0, 100, 60)

      st.write('Size:', Size)
      st.write('Color:', Color)
      st.write("Circle Area:", Circle_area)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
      X1 = st.selectbox(
      'X',
      (Data.columns.values), key='Chart1')
      Y1 = st.selectbox(
      'Y',
      (Data.columns.values), key='Chart2')
      fig = px.scatter(data_frame=Data,x=X1, y=Y1,size =Size,color=Color,log_x=True,log_y=True,size_max=Circle_area)
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col2:
      X2 = st.selectbox(
      'X',
      (Data.columns.values), key='Chart3')
      Y2 = st.selectbox(
      'Y',
      (Data.columns.values),  key='Chart4')
      fig = px.scatter(data_frame=Data,x=X2, y=Y2,size =Size,color=Color,log_x=True,log_y=True,size_max=Circle_area)
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col3:
      X3 = st.selectbox(
      'X',
      (Data.columns.values), key='Chart5')
      Y3 = st.selectbox(
      'Y',
      (Data.columns.values),  key='Chart6')
      fig = px.scatter(data_frame=Data,x=X3, y=Y3,size =Size,color=Color,log_x=True,log_y=True,size_max=Circle_area)
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with col4:
      X4 = st.selectbox(
      'X',
      (Data.columns.values), key='Chart7')
      Y4 = st.selectbox(
      'Y',
      (Data.columns.values), key='Chart8') 
      fig = px.scatter(data_frame=Data,x=X4, y=Y4,size =Size,color=Color,log_x=True,log_y=True,size_max=Circle_area)
      st.plotly_chart(fig, theme="streamlit", use_container_width=True)

