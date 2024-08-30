import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url):
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if video_id_match:
        return video_id_match.group(1)
    return None


def get_captions(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        return "Invalid YouTube URL"

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        captions = " ".join([entry['text'] for entry in transcript])
        return captions
    except Exception as e:
        return f"Error: {str(e)}"


# Streamlit app
st.title("Get YouTube Video Captions")
st.write("Upload the URL of the video")

video_url = st.text_input("Enter YouTube video URL")

if st.button("Get Captions"):
    if video_url:
        captions = get_captions(video_url)
        st.text_area("Captions:", value=captions, height=300)
    else:
        st.warning("Please enter a YouTube video URL")
