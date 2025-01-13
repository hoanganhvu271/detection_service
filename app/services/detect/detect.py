from sklearn.svm import SVC
# from sklearn.metrics import classification_report, accuracy_score
import os

from .load import load_model
from .preprocess import preprocess, normalize
from app.services.dataset.insert_datasets import insert_new_dataset

model = load_model()

def detect(data):
    preprocessed_data = preprocess(data)
    result = model.predict_proba(preprocessed_data)
    try:
        if result[0][1] > os.getenv('THRESHOLD', 0.65):
            insert_new_dataset(normalize(data))
    except Exception as e:
        print('Error inserting data:', str(e))
    finally:
        return result

