from flask import request, jsonify, Flask
from flask_restful import Resource, Api
import yolov5
import base64

app = Flask(__name__)
api = Api(app)

total_time = 0.0


def detect(source):
    return yolov5.detect.run(source=source,
                             imgsz=(640, 640),
                             conf_thres=0.58,
                             save_txt=False,
                             save_conf=False,
                             nosave=True,
                             line_thickness=1,
                             name='Results_Flask')


class Detect_EPIs(Resource):
    @staticmethod
    def post():
        global total_time

        some_json = request.get_json()

        base64_img_bytes = some_json['Key'].encode('utf-8')

        with open(r"C:\Users\estagio.sst17\OneDrive - SESIMS\Documentos\Banco\imageToSave.png", 'wb') as file_to_save:
            decoded_image_data = base64.decodebytes(base64_img_bytes)
            file_to_save.write(decoded_image_data)

        results = detect(r'C:\Users\estagio.sst17\OneDrive - SESIMS\Documentos\Banco\imageToSave.png')

        return jsonify({'Results': results})


api.add_resource(Detect_EPIs, '/detect/')


if __name__ == "__main__":
    app.run(debug=True)

