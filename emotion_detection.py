'''Function to call the Emotion Detection function and return a response with the 
detected emotion'''

import requests

def emotion_detector(text_to_analyze):
    '''Input: text to be analyzed
    Output: emotion detected'''

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, headers = Headers, json = Input_json)

    return response.text
