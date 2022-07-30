import streamlit as st
import pandas as pd
import numpy as np
import census_home,census_plots
st.set_page_config(page_title="Census visualisation app",page_icon=":money:",layout="centered",initial_sidebar_state="auto")
@st.cache()
def load_dataset():
    df=pd.read_csv("adult.csv")
    df.columns=['age','workclass','fnlwgt','education','education-years','marital-status','occupation','relationship','race','gender','capital-gain','capital-loss','hours-per-week','native-country','income']
    df['native-country'] = df['native-country'].replace(' ?',np.nan)
    df['workclass'] = df['workclass'].replace(' ?',np.nan)
    df['occupation'] = df['occupation'].replace(' ?',np.nan)
    df.dropna(inplace=True)
    df.drop(columns='fnlwgt',axis=1,inplace=True)
    return df
df=load_dataset()
pages_dict = {"Home":census_home,"Visualise Data": census_plots }
st.title("Census visualisation app")
st.subheader("This app allows the user to explore and visualise census data.")
user_selection=st.sidebar.radio("Explore",tuple(pages_dict.keys()))
if user_selection=="Home":
    census_home.app(df)
else:
    census_plots.app(df)  
