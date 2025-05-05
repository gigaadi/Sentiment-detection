import streamlit as st
from googleapiclient.discovery import build
from langdetect import detect
import textblob
import re

api_key = 'your_api_key'


def analyze_sentiment(comments):
    sentiments = []
    for comment in comments:
        analysis = textblob.TextBlob(comment)
        sentiments.append(analysis.sentiment.polarity)
    return sentiments

def extract_youtube_video_comments(video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    video_response = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id
    ).execute()
    comments = []
    while len(comments) <= 100:
        for item in video_response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            try:
                if detect(comment) == 'en':
                    comments.append(comment)
            except:
                pass

        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                part='snippet,replies',
                videoId=video_id,
                pageToken=video_response['nextPageToken']
            ).execute()
        else:
            break
    return comments

def analyze_yt_comments(video_id):
    # Enter the video ID
    #'PCfiqY05BpA'
    comments = extract_youtube_video_comments(video_id)

    sentiment = analyze_sentiment(comments)
    print("Sentiment Analysis of the video comments:")
    avg_sentiment = sum(sentiment) / len(sentiment)

    # Print overall review
    if avg_sentiment > 0:
        st.success("Review: Positive")
    elif avg_sentiment == 0:
        st.success("Review: Neutral")
    else:
        st.success("Review: Negative")
    # for c in comments:
    #     print(c)
    # print(len(comments))
def extract_video_id(youtube_link):
    # Regular expression pattern to match YouTube video IDs
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, youtube_link)
    if match:
        return match.group(1)  # Extract the video ID from the matched pattern
    else:
        return None

st.title("Sentiment Analysis")
url=st.text_input("Enter YouTube course video URL")
b=st.button("Analyze")
if "select" not in st.session_state:
    st.session_state["select"] = False
if not st.session_state["select"]:
    if b:
        id = extract_video_id(url)
        analyze_yt_comments(id)
        
else:
    st.error("Please enter a valid video URL")

#'AIzaSyDNTCgfGuxyLe8daGykkNtIiwQXkXsRY-I'