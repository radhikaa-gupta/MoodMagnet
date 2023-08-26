# Import necessary libraries
import string

from flask import Flask, request, jsonify
from flask_cors import CORS
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Create a Flask app
app = Flask(__name__)
CORS(app)

# Define a route to handle sentiment analysis
@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    # Get the text data from the request
    data = request.get_json()

    # Perform sentiment analysis (replace with your sentiment analysis code)
    text = data.get('text')
    sentiment = perform_sentiment_analysis(text)

    # Return the sentiment result as JSON
    return jsonify({'sentiment': sentiment})

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral")

        # In[145]:

# Define a function to perform sentiment analysis (replace with your code)
def perform_sentiment_analysis(text):
    # Your sentiment analysis code here
    # Return 'positive', 'negative', or 'neutral' based on the analysis
    ch = -1
    ch2 = -1
    if "AC" in text:
        ch = 1
        if "LLoyd" in text:
            ch2 = 1

    lower_case = text.lower()
    clean_text = lower_case.translate(str.maketrans('', '', string.punctuation))
    tokenized_words = word_tokenize(clean_text, 'english')
    final_words = []
    for word in tokenized_words:
        if word not in stopwords.words('english'):
            final_words.append(word)
    emotion_list = []
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("/n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')
            if word in final_words:
                emotion_list.append(emotion)

    print(emotion_list)
    w = Counter(emotion_list)
    print(w)

    sentiment_analyse(clean_text)

    # In[146]:

    return w



if __name__ == '__main__':
    app.run()
