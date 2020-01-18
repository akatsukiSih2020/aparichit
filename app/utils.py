import pandas as pd
from sklearn.ensemble.forest import RandomForestClassifier
from math import cos, asin, sqrt

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))*1000 #2*R*asin...(meterss)

def preprocess(fpath):
    df = pd.read_csv(fpath,index_col = 0)
    if 'ime' not in df.index.name:        
        for col in df.columns:
            if 'ime' in col:
                df.index = df[col]
                df.drop(columns=[col],inplace=True)
                break
        else:
            return {'failed' : 'configure csv with datetime columns'}

    if df.shape[0] < 100:
        return {"failed" : 'Need atleast 100 datapoints to classify object'}

    for param in ['Lat', 'Long', 'Alt']:
        df['v_' + param ] = 0
        df['v_' + param][1:] = df[param][1:].values - df[param][:-1].values

    df['v_Alt'] /= 60
    for param in ['Alt']:
        df['a_'  + param ] = 0
        df['a_'  + param][1:] = df['v_' + param][1:].values - df['v_' + param][:-1].values
    df = df.iloc[1:,:]
    df['a_Alt'] /= 60
    row = []

    for cols in df.columns:   
        row.extend(df[cols].values[:100])

    row = pd.Series(row)
    row = row.values.reshape((1,-1))
    return row

def intersect(df, lat_pad, long_pad):
    df = list(df.values)
    df.sort(key = lambda x : ((x[0]-lat_pad)**2 + (x[1]-long_pad)**2 - x[2]))
    return df[0][1], df[0][2], df[0][0]
