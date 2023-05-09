#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from gtts import gTTS
import os
import playsound


# In[2]:


root = Tk()
root.title("Text To Speech")
root.geometry("1000x500+200+90")
root.resizable(False, False)
root.configure(bg="#808080")


# In[3]:


#language_box = Combobox(root, values=["en", "es", "fr", "it", "ja", "ko", "zh-cn"], font="Roboto 12", state='readonly', width=12)
#language_box.place(x=150, y=400)
#language_box.set("en")


# In[4]:


def speaknow():
    text = text_box.get(1.0, END)
    language = "en"
    rate = speed_box.get()

    if rate == 'Slow':
        rate = 0.5
    elif rate == 'Medium':
        rate = 1.0
    else:
        rate = 1.5

    tts = gTTS(text=text, lang=language, slow=(rate == 0.5), tld='com', lang_check=True, pre_processor_funcs=[], use_prosody=True, key=None, timeout=4)
    tts.save("speech.mp3")
    playsound.playsound("speech.mp3", True)
    os.remove("speech.mp3")


# In[5]:


jj_logo = PhotoImage(file= "")
Label(root, image= jj_logo, bg="#808080").place(x=1000, y=739)


# In[6]:


upper_frame = Frame(root, bg = "#D3D3D3", width = 1200, height = 100)
upper_frame.place(x=0, y=0)


# In[7]:


Label(upper_frame, text="Text To Speech", font="Eurostile 60 bold", fg= "#84a9ac",bg= "#D3D3D3").place(x=330, y=30)


# In[8]:


text_box = Text(root, font= "Roboto 20", bg= "white", relief= GROOVE, wrap= WORD, bd=0)
text_box.place(x=50, y=150, width=900, height= 180)


# In[9]:


gender_box= Combobox(root, values=["Male", "Female"], font= "Roboto 12", state='r', width= 12)
gender_box.place(x=350, y=400)
gender_box.set("Male")


# In[10]:


speed_box= Combobox(root, values=["Fast", "Medium", "Slow"], font= "Roboto 12", state='r', width= 12)
speed_box.place(x=550, y=400)
speed_box.set("Medium")


# In[11]:


Label(root, text="Select Voice", font= "Roboto 15 bold", bg= "#808080", fg= "white").place(x=350, y=370)
Label(root, text="Select Speed", font= "Roboto 15 bold", bg= "#808080", fg= "white").place(x=550, y=370)


# In[ ]:


play_button = PhotoImage(file="/Users/user/Downloads/pngwing.com.png").subsample(2, 3)
play_btn = Button(root, text="Play", compound=LEFT, image=play_button, bg="#808080", width=130, font="arial 14 bold", borderwidth='0.1c', command=speaknow)
play_btn.place(x=435, y=450)
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




