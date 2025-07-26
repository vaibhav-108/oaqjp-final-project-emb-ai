import requests
import json

def emotion_detector(text_to_analyze):
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json, headers=header)
    status_code = response.status_code
    return status_code
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # formated_response= json.loads(response.text)
    # emotions=formated_response["emotionPredictions"][0]["emotion"]
    # dominent_emotion= max(emotions.items(),key=lambda x: x[1])
    # emotions["dominent_emotion"]= dominent_emotion
    # return emotions 



    
