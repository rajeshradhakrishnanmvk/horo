import pyaudio
import wave
import threading
from picamera2 import Picamera2

# Parameters for audio
chunk = 4096
sample_format = pyaudio.paInt16
channels = 1
rate = 44100
audio_filename = "audio.wav"

# Function to record audio
def record_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
    frames = []

    try:
        while recording:
            data = stream.read(chunk)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio
    wf = wave.open(audio_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# Function to record video
def record_video():
    picam2 = Picamera2()
    picam2.start_and_record_video("video.mp4", duration=duration)

# Record duration (in seconds)
duration = 10

# Start recording audio and video in separate threads
recording = True
audio_thread = threading.Thread(target=record_audio)
video_thread = threading.Thread(target=record_video)

audio_thread.start()
video_thread.start()

# Wait for the duration of the recording
try:
    audio_thread.join(duration)
    video_thread.join()
finally:
    recording = False
    audio_thread.join()


# If you need to combine the audio and video files into a single file, you can use a tool like ffmpeg. 
# Install ffmpeg and use the following command:
#ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
