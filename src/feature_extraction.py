import numpy
import numpy as np
from PIL import Image
import pickle

DATA = {}


def get_prediction(img, model):
    img = Image.open(img)
    img = img.resize((244, 244))
    img = np.array(img)

    reshaped_img = img.reshape(1, 244, 244, 3)
    features = model.predict(reshaped_img, use_multiprocessing=True)

    return features


def extract_features(images, model, path):
    for image in images:
        try:
            feature = get_prediction(image, model)
            DATA[image] = feature
        except:
            with open(path, "wb") as file:
                pickle.dump(DATA, file)
    return DATA
