# horo

## GRPC Experiment
```
pip install grpcio grpcio-tools
npm install -g grpc-tools @grpc/proto-loader

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto
node_modules/.bin/grpc_tools_node_protoc --js_out=import_style=commonjs,binary:. --grpc_out=grpc_js:. --proto_path=. service.proto

python server.py
node client.js
```

## Video Translation Experiment

Input : Video = (https://www.youtube.com/watch?v={input}) 
Source Language: English to Target Language: Malayalam
0. YT download (if required) - downloadvideo.py
1. Split the video to one minute shorts - splitMainVideo.py
2. Loop and Extract Audio from one minute Videos - splitMainVideoAudio.py/audioExtract.py
3. Convert Speech to Text - speech2text.py using google.generativeai>model gemini-1.5-flash
4. IndicTrans2 - Translate English Text to Malayalam, https://github.com/AI4Bharat/IndicTrans2
	a. server code : malaylamtranslator_server.py
	b. client code : malaylamtranslator_client.py
5. Indic-TTS Convert Text to Speech - https://github.com/AI4Bharat/Indic-TTS
	a. server code : malayalamTTS_server.py
	b. client code : malayalamTTS_client.py
6. Generate Subtitles using Malayalam Text - subtitle_gen.py
7. Burn the Subtitles to the Malayalam Video - Subtitle_Add.ipynb
 	a. Font: https://thottingal.in/blog/2022/10/05/nupuram/
8. Add Sign Language - IN PROGRESS
	a. Virtual Humans Research for Sign Language Animation
	b. https://vh.cmp.uea.ac.uk/index.php/Main_Page
8. Merge (using ClipChamp) + Review Final Video 
9. End Loop
