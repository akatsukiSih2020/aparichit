import json
import os
import glob
import math
import time
import pandas as pd
import numpy as np
from datetime import datetime
from pprint import pprint as pp
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from . import cosys
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

def get_data(df, L, forecast=3):

    for i in range(1, L+1):
        for col in ['x', 'y', 'z']:
            df[col + '_' + str(i)]= df[col].shift(-i)
    df.dropna(inplace=True)

    # 3 is number of feature
    X = np.array(df.to_numpy(copy=True))[:-forecast].reshape((-1, 1, 3*(L+1)))
    y = np.array(df.to_numpy(copy=True))[forecast:].reshape((-1, 3*(L+1)))

    return X, y

def get_result(result,scaler):
    if result.shape != (3,3):
        result = result.reshape((-1, 3))

    result = scaler.inverse_transform(result)
    result = pd.DataFrame(result, columns=['x','y','z'])
    result = cosys.df_ecef_to_geo(result)

    return result

def process(df_path):
    df = pd.read_csv(df_path, index_col=0)
    data = cosys.df_geo_to_ecef(df)
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler = scaler.fit(data)
    data = scaler.transform(data)
    data = pd.DataFrame(data, columns=['x', 'y', 'z'])

    X, y = get_data(data, 2)
    model = Sequential()
    model.add(LSTM(units=30, input_shape=(1,9)))
    model.add(Dense(9))
    model.compile(loss='mae', optimizer='adam')

    # fit network
    history = model.fit(X, y, epochs=100, batch_size=1, verbose=2, shuffle=False)

    future_3 = get_result(model.predict([[y[-1:]]]).reshape((-1, 3)), scaler)
    latest_true = get_result(y[-1:].reshape((-1,3)), scaler)
    return future_3, latest_true

