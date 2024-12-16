import streamlit as st
import pandas as pd
from utils.db import getHistoryValues, getDateSpecificValue
from datetime import datetime

st.title("DB - Postgres")

def restructureDate(date):
    date_str = str(date)
    return date_str[:4]+"-"+date_str[4:6]+"-"+date_str[6:]

def displayHistoricValues(data):
    df = pd.DataFrame(data)
    df.columns=["date", "hospitalizedCurrently", "positive", "negative", "death"]
    df['date'] = df['date'].apply(restructureDate)
    st.session_state["historicValues"]=df
    
    
def displayMetricOfADate(data):
    df = pd.DataFrame(data)
    df.columns=["hospitalizedCurrently", "positive", "negative", "death", 
    "deathIncrease", "hospitalizedIncrease", "negativeIncrease", "positiveIncrease"]
    
    metricColumn1, metricColumn2 = st.columns(2)
    
    metricColumn1.metric("Hospitalized", 
                         int(df["hospitalizedCurrently"].iloc[0]), 
                         int(df["hospitalizedIncrease"].iloc[0]), 
                         delta_color="inverse")
    metricColumn2.metric("Death", 
                         int(df["death"].iloc[0]), 
                         int(df["deathIncrease"].iloc[0]), 
                         delta_color="inverse")
    
    metricColumn1.metric("Positive",
                         int(df["positive"].iloc[0]), 
                         int(df["positiveIncrease"].iloc[0]),
                         delta_color="inverse")
    metricColumn2.metric("Negative", 
                         int(df["negative"].iloc[0]), 
                         int(df["negativeIncrease"].iloc[0]))
    
def showErrorBanner(error):
    st.error(error)
    
def formatDate(date):
    return date.strftime("%Y%m%d")

if 'historyValues' not in st.session_state:
    getHistoryValues(displayHistoricValues, showErrorBanner)

st.header("All Time Data")
if 'historicValues' in st.session_state:
    st.subheader("Hospitalized and Deaths")
    st.line_chart(st.session_state['historicValues'], 
                  x="date",
                  y=["hospitalizedCurrently", "death"],
                  color=["#008000", "#FF2C2C"])
    st.subheader("Positives and Negatives")
    st.line_chart(st.session_state['historicValues'], 
                  x="date",
                  y=["positive", "negative"],
                  color=["#008000", "#FF2C2C"])

headerColumn1, headerColumn2 = st.columns([0.7, 0.3], vertical_alignment="center")
headerColumn1.header("Metrics on a given Date")

date_picked = headerColumn2.date_input(label="Pick Date", 
                                       value=datetime(2021, 3, 7),
                                       max_value=datetime(2021, 3, 7),
                                       min_value=datetime(2020, 1, 13),
                                       format="YYYY-MM-DD",
                                       label_visibility="hidden")
getDateSpecificValue(formatDate(date_picked), displayMetricOfADate, showErrorBanner)