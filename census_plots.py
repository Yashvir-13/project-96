import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app(df):

    st.title("Visiualisation")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.subheader("Visualisation selector")
    graph=st.multiselect("Select the desired plot type",("pie-chart","countplot","box-plot","area chart","line-chart","correlation heatmap","histogram","bargraph"))
    if "pie-chart" in graph:
        st.subheader("Pie-chart")
        plt.pie(df["income"].value_counts(),labels=df["income"].value_counts().index,startangle=45,autopct="%1.2f%%")
        st.pyplot()
    if "countplot" in graph:
        st.subheader("countplot")
        col=st.selectbox("Select the catagory",df.columns)
        sns.countplot(df[col])
        st.pyplot()    
    if "box-plot" in graph:
        st.subheader("boxplot")
        col=st.selectbox("Select the catagory",('age','education-years','capital-gain','capital-loss','hours-per-week',))
        sns.boxplot(df[col])
        st.pyplot()     
    if "line-chart" in graph:
        st.subheader("line chart")
        col=st.selectbox("Select the column",df.columns)
        st.line_chart(df[col])
    if "correlation heatmap" in graph:
        st.subheader("correlation heatmap")
        sns.heatmap(df.corr(),annot=True)
        st.pyplot()
    if "bargraph" in graph:
        st.subheader("bargraph")
        col=st.selectbox("Select the category",df.columns)
        st.bar_chart(df[col])