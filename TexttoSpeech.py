#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from gtts import gTTS
from playsound import playsound


# In[2]:


root = Tk()
root.title("Chandan's Text to Speech Converter")
root.geometry("1000x580+200+80")
root.resizable(False,False)
root.configure(bg="#F7AC40")
#root.mainloop()


# In[3]:


tts = pyttsx3.init()
def speaknow():
    text= text_box.get(1.0, END)
    gender= gender_box.get()
    speed= speed_box.get()
    voices= tts.getProperty('voices')
    
    def setvoice():
        if(gender == 'Male'):
            tts.setProperty('voice', voices[0].id)
            tts.say(text)
            tts.runAndWait()
        
        else:
            tts.setProperty('voice', voices[1].id)
            tts.say(text)
            tts.runAndWait()
        
    if(text):
        if(speed == 'Fast'):
            tts.setProperty('rate',250)
            setvoice()
        elif(speed == 'Medium'):
            tts.setProperty('rate', 150)
            setvoice()
        else:
            tts.setProperty('rate', 60)
            setvoice()


# In[4]:


#simpli_logo = PhotoImage(file = "C:/Users/chandan/Desktop/Bits Python codes/Codes/Text to speech converter inPython/logo.png")
#Label(root, image= simpli_logo, bg="#F7AC40").place(x=800, y=530)
#root.mainloop()


# In[5]:


logo_image = PhotoImage(file = "C:/Users/chandan/Desktop/Bits Python codes/Codes/Text to speech converter inPython/logo.png")
root.iconphoto(False, logo_image)
#root.mainloop()


# In[6]:


upper_frame = Frame(root, bg ="#14A7DD", width =1200, height =130)
upper_frame.place(x=0, y=0)

picture = PhotoImage(file = "C:/Users/chandan/Desktop/Bits Python codes/Codes/Text to speech converter inPython/icon1.png")
Label(upper_frame, image= picture, bg="#14A7DD").place(x=130, y=10)
#root.mainloop()


# In[7]:


Label(upper_frame, text="Text to Speech Converter", font="TimeNewroman 40 bold", bg ="#14A7DD", fg='White').place(x=250, y=35)
#root.mainloop()


# In[8]:


text_box= Text(root, font="calibri 20", bg="white", relief=GROOVE, wrap=WORD, bd=1)
text_box.place(x=30, y=150, width=940, height=180)
#root.mainloop()


# In[9]:


gender_box = Combobox(root, values=['Male','Female'], font= "Robote 12" ,state='r', width=12)
gender_box.place(x=340, y=400)
gender_box.set('Male')
#root.mainloop()


# In[10]:


speed_box = Combobox(root, values=['Fast','Medium','Slow'], font= "Robote 12" ,state='r', width=12)
speed_box.place(x=540, y=400)
speed_box.set('Medium')
#root.mainloop()


# In[11]:


Label(root, text="Select Voice", font ='TimeNewroman 15 bold', bg="#F7AC40", fg="white").place(x=340,y=370)
Label(root, text="Select Speed", font ='TimeNewroman 15 bold', bg="#F7AC40", fg="white").place(x=540,y=370)
#root.mainloop()


# In[ ]:


play_button= PhotoImage(file= "C:/Users/chandan/Desktop/Bits Python codes/Codes/Text to speech converter inPython/play.png")
play_btn = Button(root, text="Play", compound = LEFT, image= play_button, bg='white', width = 140, font ="arial 14 bold",
                  borderwidth='0.1c', command= speaknow)
play_btn.place(x=435, y=450)
root.mainloop()

