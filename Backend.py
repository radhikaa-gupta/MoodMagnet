#!/usr/bin/env python
# coding: utf-8

# In[23]:


from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# In[14]:


file_path = 'path_to_your_file.txt'
with open('1.txt', 'r') as file:
    text = file.read()


# In[25]:


text = open("1.txt", encoding="utf-8").read()


# In[26]:


lower_case=text.lower()


# In[27]:


clean_text=lower_case.translate(str.maketrans('','',string.punctuation))


# In[28]:


tokenized_words= word_tokenize(clean_text,'english')


# In[29]:


final_words=[]


# In[30]:


for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


# In[31]:


emotion_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("/n",'').replace(",",'').replace("'",'').strip()
        word,emotion= clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w=Counter(emotion_list)
print(w)


# In[32]:


def sentiment_analyse(sentiment_text):
    score=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=score['neg']
    pos= score['pos']
    if neg>pos:
        print("Negative Sentiment")
    elif pos>neg:
        print("Positive Sentiment")
    else:
        print("Neutral")   


# In[33]:


sentiment_analyse(clean_text)


# In[11]:


fig, ax1= plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




