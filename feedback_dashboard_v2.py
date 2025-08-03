import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.colors import qualitative

# Load the Excel file
df = pd.read_excel("_survey_2025-07-30 18_57_31 (1).xlsx")

st.set_page_config(page_title="Employee Health Camp Feedback Dashboard", layout="wide")

st.markdown("<h1 style='color:#4A90E2;'>🏥 Health Camp Feedback Dashboard</h1>", unsafe_allow_html=True)
st.markdown("Explore employee feedback and suggestions from the recent health check-up camp.")

# Sidebar filters
with st.sidebar:
    st.header("🔍 Filters")
    respondents = st.multiselect("Filter by Respondents", options=df["Respondent"].unique(), default=df["Respondent"].unique())
    df = df[df["Respondent"].isin(respondents)]

# Feedback Ratings Section
st.markdown("## ⭐ Overall Ratings Summary")

col1, col2 = st.columns(2)

with col1:
    exp_chart = df["How would you rate your overall experience of the health camp? - Single Choices"].value_counts()
    fig = px.bar(exp_chart, title="Overall Experience", color=exp_chart.index, color_discrete_sequence=qualitative.Set2)
    st.plotly_chart(fig, use_container_width=True)

    staff_chart = df["How would you rate the quality & courteousness of the staff ? - Single Choices"].value_counts()
    fig2 = px.bar(staff_chart, title="Staff Courtesy", color=staff_chart.index, color_discrete_sequence=qualitative.Bold)
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    wait_chart = df["How would you rate the waiting time and overall flow of the event ? - Single Choices"].value_counts()
    fig3 = px.bar(wait_chart, title="Waiting Time & Flow", color=wait_chart.index, color_discrete_sequence=qualitative.Prism)
    st.plotly_chart(fig3, use_container_width=True)

    equip_chart = df["How would you rate the quality of the equipment used for the checkup ? - Single Choices"].value_counts()
    fig4 = px.bar(equip_chart, title="Equipment Quality", color=equip_chart.index, color_discrete_sequence=qualitative.Vivid)
    st.plotly_chart(fig4, use_container_width=True)

# Pie Charts Section
st.markdown("## 🩺 Doctor Consultation & Health Insight")

col3, col4 = st.columns(2)

with col3:
    consult_chart = df["Did you seek a free doctor consultation via Practo? - Single Choices"].value_counts()
    fig5 = px.pie(names=consult_chart.index, values=consult_chart.values, title="Consultation via Practo", color_discrete_sequence=qualitative.Pastel)
    st.plotly_chart(fig5, use_container_width=True)

with col4:
    help_chart = df["Did the check-up help you gauge your health better and plan accordingly? - Single Choices"].value_counts()
    fig6 = px.pie(names=help_chart.index, values=help_chart.values, title="Usefulness of the Check-up", color_discrete_sequence=qualitative.Set3)
    st.plotly_chart(fig6, use_container_width=True)

# Text Feedback Section
st.markdown("## 📝 Open-ended Feedback")

def render_feedback(title, column_name):
    st.markdown(f"### {title}")
    responses = df[["Respondent", column_name]].dropna()
    if responses.empty:
        st.info("No responses available.")
    else:
        for idx, row in responses.iterrows():
            with st.expander(f"{row['Respondent']}"):
                st.write(row[column_name])

render_feedback("What did you like the most about the Camp?", "What did you like the most about the Camp ? - Text Box")
render_feedback("What areas do you think need improvement?", "What areas do you think need improvement ? - Text Box")
render_feedback("Additional Comments or Suggestions", "Do you have any additional comments or suggestions ? - Text Box")
