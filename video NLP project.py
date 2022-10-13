#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install moviepy')


# In[2]:


get_ipython().system('pip install wordcloud')


# In[3]:


get_ipython().system('pip install mlxtend')


# In[4]:


get_ipython().system('pip install pydub')


# In[5]:


get_ipython().system('pip install speechrecognition')


# In[6]:


import numpy as np
import pandas as pd
import moviepy.editor as mp


# In[7]:


clip = mp.VideoFileClip(r"J:/roommates/TVF's Permanent Roommates _ S01E02 - 'The Father-In-Law'.mp4")


# In[8]:


audio_clip= clip.audio.write_audiofile(r"J:/roommates/Audio_file.wav")


# In[9]:


import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
r = sr.Recognizer()


# In[10]:


def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text


# In[14]:


text = get_large_audio_transcription("J:/roommates/Audio_file.wav")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




