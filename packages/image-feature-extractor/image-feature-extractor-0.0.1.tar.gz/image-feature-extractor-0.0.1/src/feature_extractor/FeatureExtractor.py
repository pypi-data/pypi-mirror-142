import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
import numpy as np


class ExtractFeatureVectors(object):

    def __init__(self):
        # initializing the model
        self.model = None
        self._model()

    def _model(self):
        img_size = 224
        base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(img_size, img_size, 3), pooling='max')
        # Customize the model to return features from fully-connected layer
        self.model = base_model

    def extract(self, input_image):
        if self.model is not None:
            # Resize the image
            img = input_image.resize((224, 224))
            # Convert the image color space
            img = img.convert('RGB')
            # Reformat the image
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            # Extract Features
            feature = self.model.predict(x)[0]
            return feature / np.linalg.norm(feature)

