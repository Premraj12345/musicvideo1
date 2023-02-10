import streamlit as st
import os
from download import download
from time import sleep

st.header('App') 
VBR="1500k"
FPS="24"
QUAL="superfast"

YOUTUBE_URL="rtmp://a.rtmp.youtube.com/live2"
KEY="a2c2-ww7x-cv80-f6b1-fzb6"
VIDEO_SOURCE="video.mp4"

url = 'https://checker.in/go/4642329'
youtube_ffmpeg_command = f'ffmpeg -stream_loop -1 -re -i {VIDEO_SOURCE} -c:v libx264 -pix_fmt yuv420p -preset {QUAL} -r {FPS} -g 48 -b:v {VBR} -c:a aac -f flv {YOUTUBE_URL}/{KEY}'

status = download(url,'video.mp4')
st.markdown(status)

sleep(100)

text = os.popen(youtube_ffmpeg_command).read()
st.markdown(text)

st.text("Working")
