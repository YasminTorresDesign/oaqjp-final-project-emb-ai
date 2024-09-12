"""
Este módulo inicia un servidor Flask para analizar emociones a través de una API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Función que maneja la ruta '/emotionDetector'.
    Recibe un texto a través de los argumentos de la solicitud,
    lo analiza para detectar emociones, y devuelve la respuesta formateada.

    Retorna:
        str: Respuesta formateada que incluye las puntuaciones de las emociones 
        y la emoción dominante, o un mensaje de error si la entrada es inválida.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Extraer las puntuaciones de las emociones y la emoción dominante de la respuesta
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Verificar si la emoción dominante es None
    if dominant_emotion is None:
        return "¡Texto no válido! ¡Por favor, inténtalo de nuevo!"

    return (
        f"Para la afirmación dada, la respuesta del sistema es 'ira': {anger}, "
        f"'asco': {disgust}, 'miedo': {fear}, 'alegría': {joy}, y 'tristeza': {sadness}. "
        f"La emoción dominante es {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Función que maneja la ruta raíz '/'.
    Renderiza la página principal utilizando el archivo 'index.html'.
    
    Retorna:
        str: El contenido renderizado de 'index.html'.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
