import requests
from copy import deepcopy
import argparse
import json

URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
HEADERS = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
INPUT_JSON = { "raw_document": { "text": "placeholder" } }

def sentiment_analyzer(text_to_analyze):
    request_obj = deepcopy(INPUT_JSON)
    request_obj["raw_document"]["text"] = text_to_analyze
    response = requests.post(url = URL, json = request_obj, headers=HEADERS)
    formatted_response = json.loads(response.text)
    return {
        "label": formatted_response['documentSentiment']['label'] if response.status_code==200 else None,
        "score": formatted_response['documentSentiment']['score'] if response.status_code==200 else None
        }    

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-t", "--text")
    args = argument_parser.parse_args()
    print(sentiment_analyzer(args.text))