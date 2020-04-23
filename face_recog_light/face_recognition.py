"""
The facenet model was converted to a quantized tflite model using the guide here:
https://medium.com/@tomdeore/facenet-on-mobile-cb6aebe38505
"""
import base64
import os
import tensorflow as tf
from PIL import Image
import numpy as np
import json

MODEL_FILENAME = 'sandberg_model-20180402-114759.ckpt-275.tflite'
MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'models'))

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path=os.path.join(MODELS_DIR, MODEL_FILENAME))
interpreter.allocate_tensors()
# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()



def face_locations_from_image(raw_image, strategy='mtcnn'):
    """Run a face detector to get all faces in the image
       @param raw_image: PIL image
       @param strategy: 'mtcnn' or 'hog'
    """
    pass

def align_face(face_crop):
    """Do affne transformation to get eyes and mouth in the centre."""
    pass

def encoding_from_face(aligned_face):
    "Return the embedding as well as the model name used to generate it."

    img_160 = aligned_face.resize((160, 160), resample=Image.LANCZOS)
    img_160_arr = np.array(img_160)
    input_data = np.expand_dims(img_160_arr, axis=0)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return json.dumps(output_data.tolist()[0]), MODEL_FILENAME

def encodings_from_image(raw_image):
    "Implement this as a generator"
    face_locations = face_locations_from_image(raw_image)

    encodings = []
    for face_location in face_locations:
        # face_crop = crop(raw_image, face_location)  # crop on face location
        aligned_face = align_face(face_crop)
        encoding = encoding_from_face(aligned_face)

        # generate unique id for face
        # face_id = ...
        encodings.append = {
            'face_id': face_id,
            'encoding': encoding,
            'b64img': base64.encodebytes(face_crop)  # TODO: implement this properly
        }

    return encodings
