import requests
import json

def emotion_detector(text_to_analyze):
    # Verificar si el texto a analizar está vacío
    if not text_to_analyze.strip():
        # Si el texto está vacío, devolver el diccionario con None para todas las emociones
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = Input_json, headers=Headers)
    
    # Verificar el código de estado de la respuesta
    if response.status_code == 400:
        # Si el código de estado es 400, devolver el diccionario con None para todas las emociones
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convertir la respuesta en un diccionario
    response_dict = response.json()
    
    # Extraer las emociones desde 'emotionPredictions'
    emotions = response_dict['emotionPredictions'][0]['emotion']
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Determinar la emoción dominante
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Formatear la salida en el formato requerido
    formatted_output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }    
    return formatted_output


