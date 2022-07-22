# region Imports
import time
from flask import request, jsonify, Flask
from flask_restful import Resource, Api
from static.Model import load_model
from static.Detect import detect
from Helpers.Save_image import save_image


# endregion
# region Global_Variables
app = Flask(__name__)
api = Api(app)
model = load_model()
total_time = 0.0
path_image = r"C:\Users\estagio.sst17\OneDrive - SESIMS\Documentos\Banco\imageToSave.png"


# endregion


class Detect_EPIs(Resource):
    @staticmethod
    def post():
        global total_time

        some_json = request.get_json()

        try:
            base64_img_bytes = some_json['ImageData'].encode('utf-8')
            save_image(base64_img_bytes)
        except Exception as error:
            return jsonify({'Error': repr(error)})

        try:
            start = time.time()

            results = detect(path_image, model=model)

            end = time.time()
            results.append("Time: " + str(end - start))
        except Exception as error:
            return jsonify({'Error': repr(error)})

        return jsonify({'Results': str(results)})


api.add_resource(Detect_EPIs, '/detect/')


if __name__ == "__main__":
    app.run()
