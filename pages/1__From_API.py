import streamlit as st
import pandas as pd
from utils.api import getHistoricValues, getMetricOfADate
from datetime import datetime

st.title("API")

def restructureDate(date):
    date_str = str(date)
    return date_str[:4]+"-"+date_str[4:6]+"-"+date_str[6:]

def displayHistoricValues(data):
    df = pd.DataFrame(data)
    df['date'] = df['date'].apply(restructureDate)
    st.session_state["historicValues"]=df
    
def displayMetricOfADate(data):
    metricColumn1, metricColumn2 = st.columns(2)
    
    metricColumn1.metric("Hospitalized", 
                         data["hospitalizedCurrently"], 
                         data["hospitalizedIncrease"],
                         delta_color="inverse")
    metricColumn2.metric("Death",
                         data["death"], 
                         data["deathIncrease"], 
                         delta_color="inverse")
    
    metricColumn1.metric("Positive", 
                         data["positive"], 
                         data["positiveIncrease"], 
                         delta_color="inverse")
    metricColumn2.metric("Negative", 
                         data["negative"], 
                         data["negativeIncrease"])
    
def showErrorBanner(error):
    st.error(error)
    
def formatDate(d):
    return d.strftime("%Y%m%d")

if not 'historicValues' in st.session_state:
    getHistoricValues(displayHistoricValues, showErrorBanner)

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

getMetricOfADate(formatDate(date_picked), 
                 onSuccess=displayMetricOfADate, 
                 onError=showErrorBanner)