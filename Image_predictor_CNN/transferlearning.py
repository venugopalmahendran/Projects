import joblib
from pipeline_compontents import Imagepreprocess
from pipeline_compontents import kerasmodelwrapper

model=joblib.load("models/image_model.joblib")
