import speech_recognition as sr
from moviepy.editor import VideoFileClip
import os

def extract_from_audio(path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)

def extract_from_video(path):
    clip = VideoFileClip(path)
    audio_path = "temp.wav"
    clip.audio.write_audiofile(audio_path)
    text = extract_from_audio(audio_path)
    os.remove(audio_path)
    return text
