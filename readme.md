# 🏏 IPL Score Predictor 

This is a machine learning project to predict the **final IPL score** ball-by-ball using match context features like overs, runs, wickets, etc. It uses **Lasso Regression** for prediction and is deployed with an interactive **Streamlit** web interface.

---

## 📊 Features Used

- Batting Team (one-hot encoded)
- Bowling Team (one-hot encoded)
- Venue (one-hot encoded)
- Overs Completed
- Runs Scored
- Wickets Fallen
- Runs in Last 5 Overs
- Wickets in Last 5 Overs

---

## 🔍 Model Used

- **Lasso Regression**
- Trained using scikit-learn's `GridSearchCV` to optimize the `alpha` hyperparameter.

---

## 🚀 Web App (Streamlit)

### Inputs:

- Dropdowns for **Batting Team**, **Bowling Team**, **Venue**
- Sliders and number inputs for:
  - Overs completed
  - Runs scored
  - Wickets fallen
  - Runs and wickets in the last 5 overs

### Output:

- Predicted Final Score
- Score range: _"Expected Score : **lower_limit** - **upper_limit** runs"_

---

