import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
GOOGLE_API_KEY=os.environ['GOOGLE_API_KEY']
genai.configure(api_key=GOOGLE_API_KEY)
segment_files = os.listdir('.\\LLM-AndreiKarpathy\\audio\\')
output_folder = '.\\LLM-AndreiKarpathy\\closecaptions'

for segment_file in segment_files:
    segment_file_path = os.path.join('.\\LLM-AndreiKarpathy\\audio\\', segment_file)
    segment_1_file = genai.upload_file(path=segment_file_path)

    prompt = "Listen carefully to the following audio file. Extract the text from the audio file and write it down."
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content([prompt, segment_1_file])

    output_file_path = os.path.join(output_folder, f'{segment_file}.txt')
    with open(output_file_path, 'w') as output_file:
        output_file.write(response.text)