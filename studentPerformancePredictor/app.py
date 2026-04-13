import streamlit as st
from model import predict_score

# Page config
st.set_page_config(page_title="AI Student Predictor", layout="wide")

# Title
st.markdown("<h1 style='text-align:center; color:#00C9A7;'>🎓 AI Student Performance Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Predict student performance using Machine Learning</p>", unsafe_allow_html=True)

st.write("---")

# Card-like container using columns
with st.container():
    st.subheader("📋 Enter Student Details")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["male", "female"])
        race = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
        parental = st.selectbox("Parental Education",
                                ["some high school", "high school", "associate's degree",
                                 "bachelor's degree", "master's degree"])

    with col2:
        lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
        prep = st.selectbox("Test Preparation", ["none", "completed"])
        reading = st.slider("Reading Score", 0, 100, 50)
        writing = st.slider("Writing Score", 0, 100, 50)

    st.write("")
    predict_btn = st.button("🔮 Predict Performance")

# Prediction Section
if predict_btn:

    input_data = {
        "gender": gender,
        "race/ethnicity": race,
        "parental level of education": parental,
        "lunch": lunch,
        "test preparation course": prep,
        "reading score": reading,
        "writing score": writing
    }

    result = predict_score(input_data)

    st.write("---")
    st.subheader("📊 Prediction Result")

    st.metric(label="Predicted Math Score", value=result)

    if result >= 80:
        st.success("🟢 Excellent Performance")
    elif result >= 60:
        st.info("🔵 Good Performance")
    elif result >= 40:
        st.warning("🟡 Average Performance")
    else:
        st.error("🔴 Poor Performance")

# Footer
st.write("---")
st.markdown("<p style='text-align:center;'>🚀 Developed by Satyam Jha</p>", unsafe_allow_html=True)