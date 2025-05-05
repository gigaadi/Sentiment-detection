import streamlit as st
import textblob

def analyze_single_comment(comment):
    analysis = textblob.TextBlob(comment)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        st.success("Review: Positive")
        print("Review: Positive")
    elif polarity == 0:
        st.success("Review: Neutral")
        print("Review: Neutral")
    else:
        st.success("Review: Negative")
        print("Review: Negative")

st.title("Sentiment Analysis")
comment=st.text_input("Enter any comment")
b=st.button("Analyze")
if "select" not in st.session_state:
    st.session_state["select"] = False
if not st.session_state["select"]:
    if b:
        analyze_single_comment(comment)
        
else:
    st.error("Please enter a valid video URL")