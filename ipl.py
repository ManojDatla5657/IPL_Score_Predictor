import streamlit as st
import numpy as np
import pickle

# Load trained model
with open('Batting-score-ElasticNet-model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define categorical features
teams = ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab',
         'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
         'Royal Challengers Bangalore', 'Sunrisers Hyderabad']

venues = ['Eden Gardens', 'Feroz Shah Kotla', 'M Chinnaswamy Stadium',
          'MA Chidambaram Stadium, Chepauk', 'Sawai Mansingh Stadium',
          'Punjab Cricket Association Stadium, Mohali',
          'Rajiv Gandhi International Stadium, Uppal', 'Wankhede Stadium']

# Streamlit UI
st.title("🏏 IPL Score Predictor")

batting_team = st.selectbox("Select Batting Team", teams)
bowling_team = st.selectbox("Select Bowling Team", [t for t in teams if t != batting_team])
venue = st.selectbox("Select Venue", venues)

overs = st.slider("Overs Completed", 0.1, 20.0, 5.0, step=0.1)
runs = st.number_input("Current Runs", min_value=0, value=50)
wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10, value=2)
runs_last_5 = st.number_input("Runs in Last 5 Overs", min_value=0, value=30)
wickets_last_5 = st.number_input("Wickets in Last 5 Overs", min_value=0, max_value=5, value=1)

# Prepare the input vector
def prepare_input():
    input_vector = []

    # One-hot encode batting team
    for team in teams:
        input_vector.append(1 if team == batting_team else 0)

    # One-hot encode bowling team
    for team in teams:
        input_vector.append(1 if team == bowling_team else 0)

    # One-hot encode venue
    for v in venues:
        input_vector.append(1 if v == venue else 0)

    # Append numeric inputs
    input_vector.extend([overs, runs, wickets, runs_last_5, wickets_last_5])

    return np.array(input_vector).reshape(1, -1)

# Prediction trigger
if st.button("Predict Final Score"):
    if runs_last_5 > runs:
        st.error(" Runs in last 5 overs cannot exceed total runs.")
    elif wickets_last_5 > wickets:
        st.error(" Wickets lost in last 5 overs cannot exceed total wickets.")
    else:
        input_data = prepare_input()
        prediction = model.predict(input_data)[0]

        lower_limit = int(prediction - 5)
        upper_limit = int(prediction + 10)
        st.info(f" Score Range: {lower_limit} to {upper_limit} runs")
