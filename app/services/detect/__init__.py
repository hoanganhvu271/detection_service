import pickle
import joblib

def load_mlb():
    mlb_permissions = joblib.load('services/models/mlb_permissions.pkl')
    mlb_service = joblib.load('services/models/mlb_services.pkl')
    mlb_broadcast = joblib.load('services/models/mlb_broadcast.pkl')
    mlb_hardware = joblib.load('services/models/mlb_hardware.pkl')

    return mlb_permissions, mlb_service, mlb_broadcast, mlb_hardware

def load_model():
    with open('services/models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model