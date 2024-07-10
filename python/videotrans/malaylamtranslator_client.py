import requests
import json

url = 'http://127.0.0.1:5069/api/mal-trans'
headers = {
    'Content-Type': 'application/json',
    'charset': 'utf-8'
}
data = {
    'text': 'Elon Musk has shown again he can influence the digital currency market with just his tweets. After saying that electric vehicle-making company Tesla will not accept payments in Bitcoin because of environmental concerns, he tweeted that he was working with developers of Dogecoin to improve system transaction efficiency.',
    'min_length': 15,
    'max_length': 75
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())

# തന്റെ ട്വീറ്റുകളിലൂടെ ഡിജിറ്റൽ കറൻസി വിപണിയെ സ്വാധീനിക്കാൻ കഴിയുമെന്ന് എലോൺ മസ്ക് വീണ്ടും തെളിയിച്ചു. പാരിസ്ഥിതിക ആ
# ശങ്കകൾ കാരണം ഇലക്ട്രിക് വാഹന നിർമ്മാണ കമ്പനിയായ ടെസ്ല ബിറ്റ്കോയിനിൽ പേയ്മെന്റുകൾ സ്വീകരിക്കില്ലെന്ന് പറഞ്ഞ ശേഷം, സിസ്റ്റം ഇടപാടിന്
# റെ കാര്യക്ഷമത മെച്ചപ്പെടുത്തുന്നതിനായി ഡോഗ്കോയിൻ ഡവലപ്പർമാരുമായി പ്രവർത്തിക്കുന്നുണ്ടെന്ന് അദ്ദേഹം ട്വീറ്റ് ചെയ്തു.