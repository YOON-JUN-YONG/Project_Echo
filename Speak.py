import speech_recognition as sr
import json

from ibm_watson import SpeechToTextV1

r = sr.Recognizer()
speech = sr.Microphone()
speech_to_text = SpeechToTextV1(
    iam_apikey="cTiQBu_VQd5SIoKyMPKsDAqCcFmEh2O9-4RE0FD34YWs",
    url="https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/c437b593-8ca8-4052-ba4a-5d56528c5d78"
)
