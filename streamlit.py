import os
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def load_data():
    path = os.getcwd()
    file = '\\token_count.csv'
    file_p = path + file
    df = pd.read_csv(file_p,
                     dtype={'token':'object', 'count':'int64'},
                     encoding='utf-8')
    return df

def draw_graph(df):
    x_token = df['token'].tolist()[:45]
    y_count = df['count'].tolist()[:45]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=y_count,
                         y=x_token,
                         orientation='h',))
    fig.update_layout(xaxis_title='計數(篇)',
                      yaxis_title='斷詞',
                      yaxis={'categoryorder': 'total ascending'},
                      font=dict(size=13),
                      height=1000)
    return fig

if __name__ == '__main__':
    df = load_data()
    fig = draw_graph(df)

    st.set_page_config(page_title='NLP-Dcard Job')  # Browser <head> 
    st.title('文字探勘 ー Dcard 工作板')   # <body> → <title>

    st.plotly_chart(fig, use_container_width=True)