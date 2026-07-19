import streamlit as st
import pickle
import re


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text


with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


st.title("📰 Fake News Detection System")

st.write("Enter a news article below to check whether it is Fake or Real.")

news = st.text_area(
    "Paste your news article here:",
    height=250
)

if st.button("Predict News"):

    if news.strip() == "":
        st.warning("Please enter a news article.")

    else:
        cleaned_news = clean_text(news)
        news_vector = vectorizer.transform([cleaned_news])
        prediction = model.predict(news_vector)

        if prediction[0] == 0:
            st.error("❌ Fake News")
        else:
            st.success("✅ Real News")