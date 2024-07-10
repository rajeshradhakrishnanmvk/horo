from inference.engine import Model
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class IndicTrans2():

    def __init__(self, data):

        self.model = Model("./en-indic/fairseq_model", model_type="fairseq")

        self.data = data

    def translate2mal(self):
        output = self.model.translate_paragraph(self.data, "eng_Latn", "mal_Mlym")
        return {'malayalam': output}


class MalayalamTranslator(Resource):
    def post(self):
        try:
            # Decode json object from the request
            json_object = request.get_json()
            data = json_object["text"]
            obj = IndicTrans2(data)
        except Exception as e:
            return {"Message": "Error in creating Classifier object" + str(e)}
        status = obj.translate2mal()
        status = status
        return status


api.add_resource(MalayalamTranslator, '/api/mal-trans')

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5069))
    # app.run(host='0.0.0.0', port=port)
    app.run(host='127.0.0.1', port=5069, debug=False)

# def translate_paragraph(src_lang, tgt_lang, text):
#     model = Model("./rajeshExp/en-indic/fairseq_model", model_type="fairseq")
#     translated_paragraph = model.translate_paragraph(text, src_lang, tgt_lang)
#     return translated_paragraph

# trans_text=translate_paragraph("eng_Latn", "mal_Mlym","Now, how do we actually use these neural networks? Well, once we've ")
# print(trans_text)

# curl -H "Content-Type: application/json" -H "charset: utf-8" -X POST -d '{"text":"Elon Musk has shown again he can influence the digital currency market with just his tweets. After saying that electric vehicle-making company Tesla will not accept payments in Bitcoin because of environmental concerns, he tweeted that he was working with developers of Dogecoin to improve system transaction efficiency.", "min_length": 15, "max_length": 75}' http://127.0.0.1:5069/api/mal-trans