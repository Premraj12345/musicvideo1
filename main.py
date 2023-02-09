import streamlit as st
import os
from download import download

st.header('App')
button_click2 = st.button('Download the video File') 

cmd_input = st.text_input('Enter video url')
password = st.text_input('Enter password')
key = st.text_input('Enter key')
youtube_ffmpeg_command = f'ffmpeg -re  -stream_loop -1 -i video.mp4 -c copy output.mp4 -c:v libx264 -c:a aac -f flv -b:v 750k -g 48 -keyint_min 48 -sc_threshold 0 rtmp://a.rtmp.youtube.com/live2/{key}'

button_click3 = st.button('Download')

button_click = st.button('START')



if button_click == True:
    with st.container():
      if password == "PREMrajpaul1@123":
        text = os.popen(youtube_ffmpeg_command).read()
        st.markdown(text)
      else:
        st.markdown("Failed")
        
if button_click3 == True:
    with st.container():
      if password == "PREMrajpaul1@123":
        status = download(cmd_input,'video.mp4')
        st.markdown(status)
      else:
        st.markdown("Failed")
