import streamlit as st

import warnings
warnings.filterwarnings('ignore')

import os
import glob

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib as mpl
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import plotly
import plotly.express as px

# 폰트 이름
font_name = 'NanumBarunGothic'
# 폰트 경로
font_path = [f.fname for f in fm.fontManager.ttflist if font_name in f.name][0]

font = fm.FontProperties(fname = font_path,size = 15).get_name()
plt.rc('font', family = font)
mpl.rc('axes', unicode_minus=False)
# unicode minus를 사용하지 않기 위한 설정 (minus 깨짐현상 방지)
plt.rcParams['axes.unicode_minus'] = False
# ggplot 으로 그래프 스타일 설정
plt.style.use('ggplot')

st.set_page_config(layout = 'wide')

# 파일 불러오기
@st.cache
def load_data():
    file_path = os.path.abspath(glob.glob('*.csv')[0])
    data = pd.read_csv(file_path) 
    # date_col 타입 변경
    date_cols = data.columns[data.columns.str.contains('date')]
    for col in date_cols:
        data[col] = pd.to_datetime(data[col], format = '%Y-%m-%d')
    return data

df = load_data()

row0_spacer1, row0_1 = st.columns((.1, 3.1))
with row0_1:
    st.title("📼Youtube 인기동영상 데이터 분석")
## num of channels by category

row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 1.9, .1))
st.write(" ")
with row1_1:
    st.markdown("+ 목적 : 데이터('21.03.25-21.07.29' Youtube 인기동영상) 분석내용을 _**plotly**_ 를 통해 인터랙티브하게 시각화하고 _**streamlit**_ 사용해 공유하고자 합니다.")
    st.markdown("+ 내용 : Youtube 인기 동영상이 어떤 특징을 가지는지에 대해 시각화한 자료로 카테고리별/월별/주별 인기비디오의 특징에 대한 분석내용을 포함하고 있습니다.")
    st.markdown("+ 참고 : 분석 과정 및 상세 코드는 [Github repository](https://github.com/pitapatat/Data_Analysis_Visualization/tree/main/%5BDA%5D_youtube_analysis)를 통해 확인하실 수 있습니다.")

    num_of_channel_by_cat = df.groupby(['category_name'])['channel_id'].count()
    df = df.set_index('published_date').sort_index()
st.write('')

row11_space1, row11_1, row11_space2 = st.columns((.1, 3.1, .1))
with row11_1:
    st.subheader("카테고리별 채널의 비디오 개수")

    tot_cat = df.category_name.value_counts(normalize = True).head().index
    tot_cat_v = df.category_name.value_counts(normalize = True).head()

    fig , ax = plt.subplots(figsize = (13,7))
    dfg = df.groupby(['category_name'], as_index = False)['channel_id'].count()
    ax = px.histogram(df,y = 'category_name', color = df.index.month, color_discrete_sequence=px.colors.qualitative.Vivid)
    ax.update_layout(yaxis={'title': ' '}, xaxis = {'title': ' '})
    st.plotly_chart(ax)



## daily by category
daily_pivot = df.pivot_table(index = [df.index, 'category_name'],values = ['channel_id'],aggfunc = ['count'], fill_value= 0)
daily = daily_pivot.unstack()
daily.columns = [daily.columns[i][2] for i in range(df.category_name.nunique())]

st.write('')
row2_spacer1, row2_1, row2_spacer2 = st.columns((.1, 3.1, .1))
with row2_1:
    st.subheader("카테고리별 인기동영상 비디오의 분포(daily)")

    fig, ax = plt.subplots(figsize = (25,10))
    ax= px.line(daily, x = daily.index, y = daily.columns, markers = False, color_discrete_sequence=px.colors.qualitative.Plotly)
    ax.update_layout(yaxis={'title': ' '}, xaxis = {'title': ' '})
    st.plotly_chart(ax, use_container_width=True)

st.write('')
row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns((.1, 1.5, .1, 1.5, .1))

with row3_1:
    st.subheader("월별 카테고리별 채널의 추이")

    monthly_pivot = df.pivot_table(index = [df.index.month, 'category_name'],values = ['channel_id'], aggfunc = ['count'], fill_value= 0)
    monthly = monthly_pivot.unstack()
    monthly.columns = [monthly.columns[i][2] for i in range(df.category_name.nunique())]

    fig, ax = plt.subplots()
    ax= px.line(monthly, x = monthly.index, y = monthly.columns, markers = True )
    ax.update_layout(yaxis={'title': ' '}, xaxis = {'title': ' '})
    st.plotly_chart(ax, use_container_width=True)

with row3_2:
    st.subheader("월별 카테고리별 채널의 구성")

    monthly_pivot_t = df.pivot_table(index = [df.index.month, 'category_name'],values = ['channel_id'], aggfunc = ['count'], fill_value= 0).T
    melted_monthly = pd.melt(monthly_pivot_t)
    fig, ax = plt.subplots()
    sns.set_palette('Set3')
    ax = px.bar(melted_monthly, x = 'published_date', y= 'value', color = 'category_name', barmode = 'group')
    ax.update_layout(yaxis={'title': ' '}, xaxis = {'title': ' '})
    st.plotly_chart(ax, use_container_width=True)

row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns((.1, 1.5, .1, 1.5, .1))

with row4_1:
    st.subheader('주별 카테고리별 채널의 추이')

    weekly_pivot = df.pivot_table(index = [df.index.week, 'category_name'],values = ['channel_id'], aggfunc = ['count'], fill_value = 0)
    weekly = weekly_pivot.unstack()
    weekly.columns = [weekly.columns[i][2] for i in range(df.category_name.nunique())]

    fig, ax = plt.subplots(figsize = (25,10))
    ax= px.line(weekly, x = weekly.index, y = weekly.columns, markers = True )
    ax.update_layout(yaxis={'title': ' '}, xaxis = {'title': ' '})
    st.plotly_chart(ax, use_container_width=True)

with row4_2:
    st.subheader('주별 카테고리별 채널의 구성')

    weekly_pivot_t = weekly_pivot.T
    melted_weekly = pd.melt(weekly_pivot_t)

    fig, ax = plt.subplots(figsize = (25,7))
    ax = px.bar(melted_weekly, x = 'published_date', y= 'value', color = 'category_name')
    ax.update_layout(yaxis={'title': ' '}, xaxis = {'title': ' '})
    st.plotly_chart(ax, use_container_width=True)

row5_spacer1, row5_1, row5_spacer2 = st.columns((.1, 3.1, .1))

### 월별 카테고리별 top10 구하기 
month_ch = df.pivot_table(index = [df.index.month, 'channel_id'],values = ['video_id'], aggfunc = ['count'], fill_value= 0).unstack()
def top10_dict(df):
    top10_dict = {}
    top10_video_num = {}
 
    for i in range(3,8):
        top10_dict[f'{i}'] = []
        top10s = df.loc[i].nlargest(10).index
        top10_video_num[f'{i}'] = df.loc[i].nlargest(10).values
        for j in range(10):
            top10_dict[f'{i}'].append(top10s[j][2])
    return top10_dict, top10_video_num

month_top10, month_top10_num = top10_dict(month_ch)

### 월별 top10 채널들의 카테고리 추출
month_top10_cat = {}
for i in range(3,8):
    month_top10_cat[f'{i}'] = []
    for j in range(len(month_top10[f'{i}'])):
        month_top10_cat[f'{i}'].append(df.category_name[df.channel_id == month_top10[f'{i}'][j]][0])
top10_cat = pd.DataFrame(month_top10_cat)

with row5_1:
    st.subheader('월별 카테고리별 top10 채널은 무엇일까?')
row6_spacer1, row6_1, row6_spacer2, row6_2, row6_spacer3, row6_3, row6_spacer4  = st.columns((.1, .3, .1, 1.5, .2, 1, .1))

with row6_1:
    mon = st.selectbox("월(month) 선택", [str(i) for i in range(3,8)])  
with row6_2:
    fig, ax = plt.subplots()
    if mon != None:
        ax = px.pie(top10_cat[mon], names = top10_cat[mon], hole=.3)
        ax.update_traces(textposition='inside', textinfo='percent+label')
        ax.update_layout(yaxis={'title': ' '}, xaxis = {'title': ' '})
        st.plotly_chart(ax, use_container_width=True)
    else:
        st.warning("몇 월을 선택할지 골라주세요!")

with row6_3: 
    st.markdown("**📺어떤 채널이 속해 있을까?**")

    month_top10_n={}
    for i in range(3,8):
        month_top10_n[mon] = []
        for ch, cat in zip(month_top10[mon], month_top10_cat[mon]):
            month_top10_n[mon].append((ch,cat))

    top10 = pd.DataFrame(month_top10_n)
    st.dataframe(top10)


row8_spacer1, row8_1, row8_spacer2 = st.columns((.1,2.1, .1))

#### 주간 top10 
week_ch = df.pivot_table(index = [df.index.week, 'channel_id'],values = ['video_id'], 
                               aggfunc = ['count'], fill_value= 0).unstack()

def top5_dict(df):
    top5_dict = {}
    top5_video_num = {}

    for i in range(12,31):
        top5_dict[f'{i}'] = []
        top5s = df.loc[i].nlargest(10).index
        top5_video_num[f'{i}'] = df.loc[i].nlargest(10).values
        for j in range(10):
            top5_dict[f'{i}'].append(top5s[j][2])
    return top5_dict, top5_video_num
week_top5, week_top5_num = top5_dict(week_ch)

week_tops = []
for i in range(12,31):
    week_tops.extend(week_top5[f'{i}'])

week_top5_cat = {}
for i in range(12,31):
    week_top5_cat[f'{i}'] = []
    for j in range(len(week_top5[f'{i}'])):
        week_top5_cat[f'{i}'].append(df.category_name[df.channel_id == week_top5[f'{i}'][j]][0])
top5_cat = pd.DataFrame(week_top5_cat)

with row8_1:
    st.subheader('주별 카테고리별 top10채널은 무엇일까?')
row9_spacer1, row9_1, row9_spacer2, row9_2, row9_spacer3, row9_3, row9_spacer4  = st.columns((.1, .3, .1, 1.5, .2, 1, .1))
with row9_1:
    wk = st.selectbox("주(week) 선택", [str(i) for i in range(12,31)])
with row9_2:
    fig, ax = plt.subplots()
    if wk != None:
        ax = px.pie(top5_cat[wk], names = top5_cat[wk], hole=.3)
        ax.update_traces(textposition='inside', textinfo='percent+label')
        ax.update_layout(yaxis={'title': ' '},xaxis = {'title': ' '})
        st.plotly_chart(ax, use_container_width=True)
    else:
        st.warning("어떤 주를 선택할지 골라주세요!")

with row9_3: 
    st.markdown("**📺어떤 채널이 속해 있을까?**")

    week_top5_n={}
    for i in range(12,31):
        week_top5_n[wk] = []
        for ch, cat in zip(week_top5[wk], week_top5_cat[wk]):
            week_top5_n[wk].append((ch,cat))

    top10 = pd.DataFrame(week_top5_n)
    st.dataframe(top10)
