import app
import base64


def save_image(base64_img_bytes):
    with open(app.path_image, 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)