import pandas as pd
from app.services.detect import load_mlb

mlb_permissions, mlb_service, mlb_broadcast, mlb_hardware = load_mlb()

def preprocess(features):
    features = normalize(features)
    df_permissions = remove_missing(features, 'permissions', mlb_permissions)
    df_service_permissions = remove_missing(features, 'service_permissions', mlb_service)
    df_broadcast_receivers = remove_missing(features, 'broadcast_receivers', mlb_broadcast)
    df_hardware_features = remove_missing(features, 'uses_features', mlb_hardware)
    data = pd.concat([df_permissions, df_service_permissions, df_broadcast_receivers, df_hardware_features], axis=1)
    return data

def normalize(a):
  b = []
  for x in a:
    if x.lower().startswith('android'):
      b.append(x.lower())
  return b


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


