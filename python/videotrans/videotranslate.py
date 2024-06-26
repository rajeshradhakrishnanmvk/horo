# Input : Video = (https://www.youtube.com/watch?v=zjkBMFhNj_g) and Source Language = English to Target Language = Malayalam
# 1. Split the video to one minute shorts - splitMainVideo.py
# 2. Loop and Extract Audio from one minute Videos - splitMainVideoAudio.py/audioExtract.py
# 3. Convert Speech to Text - speech2text.py
# 4. IndicTrans2 - Translate English Text to Malayalam, https://github.com/AI4Bharat/IndicTrans2
# 5. Convert Text to Speech - https://github.com/AI4Bharat/Indic-TTS
# 6. Generate Subtitles using Malayalam Text
# 7. Burn the Subtitles to the Malayalam Video - Subtitle_Add.ipynb
# 	a. Font: https://thottingal.in/blog/2022/10/05/nupuram/
# 8. Review Final Video 
# 9. End Loop
import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


GOOGLE_API_KEY=os.environ['GOOGLE_API_KEY']
genai.configure(api_key=GOOGLE_API_KEY)


# model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content("Give me python code to split a video with audio into one minute video")
# print(response.text)

# segment_1_file = genai.upload_file(path='.\\LLM-AndreiKarpathy\\audio\\segment_1.wav')


# prompt = "Listen carefully to the following audio file. create subtitles in srt format in Malayalam for the audio file"
# model = genai.GenerativeModel('models/gemini-1.5-flash')
# response = model.generate_content([prompt, segment_1_file])

# print(response)