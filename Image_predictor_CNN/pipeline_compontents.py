from sklearn.base import BaseEstimator,TransformerMixin
from keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions
from sklearn.pipeline import Pipeline
from keras.preprocessing import image
import numpy as np
import joblib

class Imagepreprocess(BaseEstimator,TransformerMixin):
  def fit(self,X,y=None):
    return self

  def transform(self,X):
    images = []
    for path in X:
        img = image.load_img(path, target_size=(224, 224))
        img = np.array(img)
        img = img / 255.0
        images.append(img)
    return np.array(images)
 

class kerasmodelwrapper(BaseEstimator,TransformerMixin):
  def __init__(self):
    self.model=MobileNetV2(weights=None)
    self.model.load_weights("models/mobilenetv2_clean.weights.h5")

  def fit(self,X,y=None):
    return self

  def transform(self,X):
    preds = self.model.predict(X)
    decoded_preds = decode_predictions(preds, top=1)[0][0][1]
    return decoded_preds



image_model=Pipeline([
    ("imgpre",Imagepreprocess()),
    ("model",kerasmodelwrapper())
])

joblib.dump(image_model,"image_model.joblib")