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

Input : Video = (https://www.youtube.com/watch?v=zjkBMFhNj_g) and Source Language = English to Target Language = Malayalam
1. Split the video to one minute shorts - splitMainVideo.py
2. Loop and Extract Audio from one minute Videos - splitMainVideoAudio.py/audioExtract.py
3. Convert Speech to Text - speech2text.py
4. IndicTrans2 - Translate English Text to Malayalam, https://github.com/AI4Bharat/IndicTrans2
5. Convert Text to Speech - https://github.com/AI4Bharat/Indic-TTS
6. Generate Subtitles using Malayalam Text - In Progress
7. Burn the Subtitles to the Malayalam Video - Subtitle_Add.ipynb
 	a. Font: https://thottingal.in/blog/2022/10/05/nupuram/
8. Review Final Video 
9. End Loop
