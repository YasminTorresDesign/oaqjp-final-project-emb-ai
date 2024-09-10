from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Prueba de la emoción 'alegría'
        result = emotion_detector("I am extremely happy and overjoyed that this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

        # Prueba de la emoción 'enojo'
        result = emotion_detector("This makes me very angry")
        self.assertEqual(result['dominant_emotion'], 'anger')

        # Prueba de la emoción 'asco'
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

        # Prueba de la emoción 'tristeza'
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

        # Prueba de la emoción 'miedo'
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

unittest.main()