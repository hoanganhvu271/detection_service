from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from detect import load_model

model = load_model()

def detect(data):
    return model.predict_proba(data)

