'''Function to call the Emotion Detection function and return a response with the 
detected emotion'''

import requests
import json

def emotion_detector(text_to_analyze):
    '''Input: text to be analyzed
    Output: emotion detected'''

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, headers = Headers, json = Input_json)

    if (text_to_analyze == ""):
        print('hi')
        print(response.text)
        return {'anger': None, 'disgust': None,
    'fear': None, 'joy':None, 'sadness': None,
    'dominant_emotion': None}

    formatted_response = json.loads(response.text)['emotionPredictions'][0]['emotion']

    anger_score = formatted_response['anger']
    disgust_score = formatted_response['disgust']
    fear_score = formatted_response['fear']
    joy_score = formatted_response['joy']
    sadness_score = formatted_response['sadness']

    list_emotions = {'anger': anger_score, 'disgust': disgust_score,
    'fear': fear_score, 'joy':joy_score, 'sadness': sadness_score}

    dominant_emotion = max(list_emotions, key=list_emotions.get)

    return {'anger': anger_score, 'disgust': disgust_score,
    'fear': fear_score, 'joy':joy_score, 'sadness': sadness_score,
    'dominant_emotion': dominant_emotion}

