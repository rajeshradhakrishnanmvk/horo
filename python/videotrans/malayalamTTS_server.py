from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/synthesize', methods=['POST'])
def synthesize():
    # Extract parameters from POST request
    data = request.json
    text = data.get('text')
    model_path = data.get('model_path', "./rajeshExp/malTTS/fastpitch/best_model.pth")
    config_path = data.get('config_path', "./rajeshExp/malTTS/fastpitch/config.json")
    vocoder_path = data.get('vocoder_path', "./rajeshExp/malTTS/hifigan/best_model.pth")
    vocoder_config_path = data.get('vocoder_config_path', "./rajeshExp/malTTS/hifigan/config.json")
    out_path = data.get('out_path', "./rajeshExp/malTTS/out-4.wav")
    speaker_idx = data.get('speaker_idx', "female")

    # Construct command
    command = f"python3 -m TTS.bin.synthesize --text \"{text}\" --model_path \"{model_path}\" --config_path \"{config_path}\" --vocoder_path \"{vocoder_path}\" --vocoder_config_path \"{vocoder_config_path}\" --out_path \"{out_path}\" --speaker_idx=\"{speaker_idx}\""

    # Execute command
    try:
        subprocess.run(command, check=True, shell=True)
        return jsonify({"message": "Synthesis completed", "output_path": out_path}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Failed to synthesize", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

#curl -X POST http://localhost:5000/synthesize -H "Content-Type: application/json" -d "{\"text\":\"Your text here\", \"model_path\":\"./rajeshExp/malTTS/fastpitch/best_model.pth\", \"config_path\":\"./rajeshExp/malTTS/fastpitch/config.json\", \"vocoder_path\":\"./rajeshExp/malTTS/hifigan/best_model.pth\", \"vocoder_config_path\":\"./rajeshExp/malTTS/hifigan/config.json\", \"out_path\":\"./rajeshExp/malTTS/out-4.wav\", \"speaker_idx\":\"female\"}"