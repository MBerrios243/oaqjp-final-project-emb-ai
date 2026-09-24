from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def call_emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    formatted_response = f"For the given statement, the system response is\
     'anger': {result['anger']}, 'disgust': {result['disgust']},\
      'fear': {result['fear']}, 'joy': {result['joy']} and\
       'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

    return formatted_response



if __name__ == "__main__":
      app.run(host="localhost", port=5000) # Port 5000 was in use

