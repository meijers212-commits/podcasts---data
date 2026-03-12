import speech_recognition as sr
from os import path
from ingestion_orchestrator import logger


def speech_to_text(file_path):
    # audio = sr.AudioData.from_file(file_path)
    
    r = sr.Recognizer()

    with sr.AudioFile(file_path) as f:
        audio = r.record(f)

    try:
        logger.info(f"Google Speech Recognition processing file: {file_path}")
        return  r.recognize_google(audio)
    except sr.UnknownValueError:
        logger.error("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        logger.error("Could not request results from Google Speech Recognition service; {0}".format(e))



