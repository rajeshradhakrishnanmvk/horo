# ref https://github.com/ThomasVuNguyen/chatGPT-Voice-Assistant/tree/main
# ref https://www.youtube.com/watch?v=lHxFFn04L10

import os
import openai
from dotenv import load_dotenv, find_dotenv
import time
import speech_recognition as sr
import pyttsx3
import numpy as np
from gtts import gTTS
import pyaudio
import wave
import io

# Configuration
mytext = 'Welcome to me'
language = 'en'
load_dotenv(find_dotenv())
model = 'gpt-4'

# Speech recognition and text-to-speech setup
r = sr.Recognizer()
engine = pyttsx3.init("dummy")
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
name = "RAJESH"
greetings = [
    f"whats up buddy {name}",
    "yeah?",
    "Well, hello there, buddy of Puns and Jokes - how's it going today?",
    f"Ahoy there, Captain {name}! How's the ship sailing?",
    f"നമസ്തേ, സുഖമാണോ {name}! നീ എന്ത് ചെയ്യുന്നു? Wait, why the hell am I speaking Malayalam?"
]

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  
CHUNK = 4096  # Adjusted chunk size

def get_audio_stream(chunk=CHUNK, rate=RATE, channels=CHANNELS, format=FORMAT, device_index=1):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=format, channels=channels,
                        rate=rate, input=True,
                        input_device_index=device_index,
                        frames_per_buffer=chunk)
    return stream, audio

def write_wav(data, channels, width, rate):
    buffer = io.BytesIO()
    with wave.open(buffer, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)
    buffer.seek(0)
    return buffer

def listen_for_wake_word(stream, chunk=CHUNK, rate=RATE, channels=CHANNELS, width=2):
    print("Listening for 'bujji'...")
    audio_buffer = io.BytesIO()

    try:
        while True:
            try:
                data = stream.read(chunk, exception_on_overflow=False)
            except IOError as e:
                print(f"Error reading audio stream: {e}")
                continue
            
            audio_buffer.write(data)
            audio_buffer.seek(0)
            wav_buffer = write_wav(audio_buffer.getvalue(), channels, width, rate)
            with sr.AudioFile(wav_buffer) as source:
                try:
                    audio = r.record(source)
                    text = r.recognize_google(audio)  
                    print("You said " + text)
                    if "bujji" in text.lower():
                        print("Wake word detected: " + text.lower())
                        engine.say(np.random.choice(greetings))
                        engine.runAndWait()
                        return True  # Signal to proceed to respond mode
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                    pass
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                    break
                audio_buffer.seek(0)
                audio_buffer.truncate(0)
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
        return False
    finally:
        audio_buffer.close()

def listen_and_respond(stream, chunk=CHUNK, rate=RATE, channels=CHANNELS, width=2):
    print("OpenAI Listening...")
    audio_buffer = io.BytesIO()

    try:
        while True:
            try:
                data = stream.read(chunk, exception_on_overflow=False)
            except IOError as e:
                print(f"Error reading audio stream: {e}")
                continue
            
            audio_buffer.write(data)
            audio_buffer.seek(0)
            wav_buffer = write_wav(audio_buffer.getvalue(), channels, width, rate)
            with sr.AudioFile(wav_buffer) as source:
                try:
                    audio = r.record(source)
                    text = r.recognize_google(audio)
                    print(f"You said: {text}")
                    if not text:
                        continue
                    # Send input to OpenAI API
                    response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": f"{text}"}])
                    response_text = response.choices[0].message.content
                    print(response_text)
                    print("Generating audio response...")
                    myobj = gTTS(text=response_text, lang=language, slow=False)
                    myobj.save("response.mp3")
                    print("Speaking...")
                    os.system("vlc response.mp3")
                    # Speak the response
                    print("Speaking...")
                    engine.say(response_text)
                    engine.runAndWait()
                except sr.UnknownValueError:
                    time.sleep(2)
                    print("Silence found, shutting up, listening...")
                    break
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                    engine.say(f"Could not request results; {e}")
                    engine.runAndWait()
                    break
                audio_buffer.seek(0)
                audio_buffer.truncate(0)
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")

# Main execution
stream, audio = get_audio_stream()

try:
    if listen_for_wake_word(stream):
        listen_and_respond(stream)
finally:
    # Close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()
