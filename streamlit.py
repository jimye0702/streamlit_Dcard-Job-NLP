import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def load_data():
    file = 'token_count.csv'
    
    df = pd.read_csv(file,
                     dtype={'token':'object', 'count':'int64'},
                     encoding='utf-8')

    return df

def draw_graph(df, token_filter):
    set_ind_df = df.set_index(keys='token')
    set_ind_df = set_ind_df.loc[token_filter]
    x_token = list(set_ind_df.index)
    y_count = list(set_ind_df['count'])
    fig = go.Figure()
    fig.add_trace(go.Bar(x=y_count,
                         y=x_token,
                         orientation='h',))
    fig.update_layout(xaxis_title='計數(篇)',
                      yaxis_title='斷詞',
                      yaxis={'categoryorder': 'total ascending'}, # 依 總數「降冪」排序
                      font=dict(size=13),
                      height=1000)
    return fig

def widget_multiselect(df): # sidebar >> retuen a 「list」 of the selected option.
    token = list(df['token'])
    token_filter = st.sidebar.multiselect('關鍵詞飾選：',
                                         options=token,
                                         default=token[:25])
    return token_filter

if __name__ == '__main__':
    df = load_data()

    st.set_page_config(page_title='NLP-Dcard Job')  # Browser <head> 
    st.title('文字探勘 ー Dcard 工作板')   # <body> → <title>
    token_filter = widget_multiselect(df)
    
    fig = draw_graph(df, token_filter)
    st.plotly_chart(fig, use_container_width=True)