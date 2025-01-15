import pandas as pd
from .load import load_mlb

mlb_permissions, mlb_service, mlb_broadcast, mlb_hardware = load_mlb()

title = ['permissions', 'service_permissions', 'broadcast_receivers', 'uses_features']
mlb_title = [mlb_permissions, mlb_service, mlb_broadcast, mlb_hardware]

def preprocess(features):
    features = normalize(features)
    df = []
    for i in range(len(title)):
       df.append(remove_missing(features, title[i], mlb_title[i]))
    data = pd.concat(df, axis=1)
    return data


def normalize(features):
    for i in range(len(title)):
        a = features[title[i]]
        b = []
        for x in a:
            if x.lower().startswith('android'):
                b.append(x.lower())
        
        features[title[i]] = b
    return features
  


def remove_missing(df_new, title, mlb):
  classes = mlb.classes_
  df_classes = pd.DataFrame([ [0] * len(mlb.classes_)], columns=mlb.classes_)
  for clas in classes:
    if clas in df_new[title]:
        df_classes.loc[0, clas] = 1
        print(clas)
    else:
        df_classes.loc[0, clas] = 0

  return df_classes


