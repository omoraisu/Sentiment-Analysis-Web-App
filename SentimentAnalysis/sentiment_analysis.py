"""
This module uses Watson's NLP library to analyze the provided text 
through the function sentiment_analyzer(). It returns its label and score. 
It also takes into account the status code received and does the correct
error-handling. 
"""

import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    Creates a sentiment analysis function using Watson NLP library 
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    response = requests.post(url, json = myobj, headers=header, timeout=60)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None

    return {'label': label, 'score': score}
