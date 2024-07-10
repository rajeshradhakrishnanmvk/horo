import requests

#curl -X POST http://localhost:5000/synthesize -H "Content-Type: application/json" -d "{\"text\":\"Your text here\", \"model_path\":\"./rajeshExp/malTTS/fastpitch/best_model.pth\", \"config_path\":\"./rajeshExp/malTTS/fastpitch/config.json\", \"vocoder_path\":\"./rajeshExp/malTTS/hifigan/best_model.pth\", \"vocoder_config_path\":\"./rajeshExp/malTTS/hifigan/config.json\", \"out_path\":\"./rajeshExp/malTTS/out-4.wav\", \"speaker_idx\":\"female\"}

url = "http://localhost:5000/synthesize"
headers = {
    "Content-Type": "application/json"
}
data = {
    "text": "തന്റെ ട്വീറ്റുകളിലൂടെ ഡിജിറ്റൽ കറൻസി വിപണിയെ സ്വാധീനിക്കാൻ കഴിയുമെന്ന് എലോൺ മസ്ക് വീണ്ടും തെളിയിച്ചു. പാരിസ്ഥിതിക ആശങ്കകൾ കാരണം ഇലക്ട്രിക് വാഹന നിർമ്മാണ കമ്പനിയായ ടെസ്ല ബിറ്റ്കോയിനിൽ പേയ്മെന്റുകൾ സ്വീകരിക്കില്ലെന്ന് പറഞ്ഞ ശേഷം, സിസ്റ്റം ഇടപാടിന്റെ കാര്യക്ഷമത മെച്ചപ്പെടുത്തുന്നതിനായി ഡോഗ്കോയിൻ ഡവലപ്പർമാരുമായി പ്രവർത്തിക്കുന്നുണ്ടെന്ന് അദ്ദേഹം ട്വീറ്റ് ചെയ്തു.",
    "model_path": "./rajeshExp/malTTS/fastpitch/best_model.pth",
    "config_path": "./rajeshExp/malTTS/fastpitch/config.json",
    "vocoder_path": "./rajeshExp/malTTS/hifigan/best_model.pth",
    "vocoder_config_path": "./rajeshExp/malTTS/hifigan/config.json",
    "out_path": "./rajeshExp/malTTS/out-4.wav",
    "speaker_idx": "female"
}

response = requests.post(url, headers=headers, json=data)