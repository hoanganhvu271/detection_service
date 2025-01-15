# from sklearn.svm import SVC
# from sklearn.metrics import classification_report, accuracy_score
import os

from .load import load_model
from .preprocess import preprocess, normalize
from app.services.dataset.insert_datasets import insert_new_dataset
from datetime import datetime

model = load_model()

def detect(data):
    result_list = []

    for item in data:
        preprocessed_data = preprocess(item)
        result = model.predict_proba(preprocessed_data)
        try:
            if result[0][1] > os.getenv('THRESHOLD', 0.65):
                item['prediction'] = result[0][1]
                item['time'] = datetime.now()
                insert_new_dataset(normalize(item))
        except Exception as e:
            print('Error inserting data:', str(e))
        finally:
            result_list.append(result[0].tolist())
    
    return result_list
        
    

