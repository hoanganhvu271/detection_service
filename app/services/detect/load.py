import pickle
import os
from sklearn.preprocessing import MultiLabelBinarizer
import joblib

def load_file(filename):

    base_path = os.path.dirname(__file__)
    model_path = os.path.join(base_path, 'models', filename)
    model = joblib.load(model_path)

    return model

def load_mlb():
    mlb_permissions = load_file('mlb_permissions.pkl')
    mlb_service = load_file('mlb_services.pkl')
    mlb_broadcast = load_file('mlb_broadcast.pkl')
    mlb_hardware = load_file('mlb_hardware.pkl')

    return mlb_permissions, mlb_service, mlb_broadcast, mlb_hardware


def load_model():
   return load_file('model.pkl')