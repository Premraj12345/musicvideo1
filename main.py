import streamlit as st
import os
from download import download
from time import sleep

st.header('App') 

url = 'https://file-to-link-09.herokuapp.com/WhitE_DeviL09/736685/foetoall-A-lofi-boy-sitting-on-a.mp4'
youtube_ffmpeg_command = f'ffmpeg -re  -stream_loop -1 -i video.mp4 -c copy output.mp4 -c:v libx264 -c:a aac -f flv -b:v 750k -g 48 -keyint_min 48 -sc_threshold 0 rtmp://a.rtmp.youtube.com/live2/a2c2-ww7x-cv80-f6b1-fzb6'

status = download(url,'video.mp4')
st.markdown(status)

sleep(100)

text = os.popen(youtube_ffmpeg_command).read()
st.markdown(text)

st.text("Working")
