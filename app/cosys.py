import math
import pyproj
import numpy as np
import pandas as pd

ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')

def geo_to_ecef(lat, lon, h, feet = True):
    '''
    feet: If True converts altitude from feet to meters
          If False altitude is assumed to be passed in meters

    lat: In Degrees

    lon: In Degrees

    https://gist.github.com/sbarratt/a72bede917b482826192bf34f9ff5d0b
    (lat, lon) in WSG-84 degrees
    '''

    if feet == True:
        h = h*0.3048

    a = 6378137
    b = 6356752.3142
    f = (a - b) / a
    e_sq = f * (2-f)

    lamb = math.radians(lat)
    phi = math.radians(lon)
    s = math.sin(lamb)
    N = a / math.sqrt(1 - e_sq * s * s)

    sin_lambda = math.sin(lamb)
    cos_lambda = math.cos(lamb)
    sin_phi = math.sin(phi)
    cos_phi = math.cos(phi)

    x = (h + N) * cos_lambda * cos_phi
    y = (h + N) * cos_lambda * sin_phi
    z = (h + (1 - e_sq) * N) * sin_lambda

    return x, y, z

def ecef_to_geo(x, y, z, get_in_feet=True):
    '''
    get_in_feet: If True Returns Altitude in feet
                 else in meters
    '''
    lon, lat, alt = pyproj.transform(ecef, lla, x, y, z, radians=False)

    if get_in_feet == True:
        alt = alt/0.3048

    return lat, log, alt

def df_geo_to_ecef(df, feet = True):
    '''
    feet: If True converts altitude from feet to meters
          If False altitude is assumed to be passed in meters

    lat: In Degrees

    lon: In Degrees

    https://gist.github.com/sbarratt/a72bede917b482826192bf34f9ff5d0b
    (lat, lon) in WSG-84 degrees
    '''

    lat, lon, h = df[['Lat']].values, df[['Long']].values, df[['Alt']].values

    if feet == True:
        h = h*0.3048

    a = 6378137
    b = 6356752.3142
    f = (a - b) / a
    e_sq = f * (2-f)

    lamb = np.deg2rad(lat)
    phi = np.deg2rad(lon)
    s = np.sin(lamb)
    N = a / np.sqrt(1 - e_sq * s * s)

    sin_lambda = np.sin(lamb)
    cos_lambda = np.cos(lamb)
    sin_phi = np.sin(phi)
    cos_phi = np.cos(phi)

    x = (h + N) * cos_lambda * cos_phi
    y = (h + N) * cos_lambda * sin_phi
    z = (h + (1 - e_sq) * N) * sin_lambda

    df_result = np.hstack((x, y, z))

    df_result = pd.DataFrame(df_result, columns=['x', 'y', 'z'])

    return df_result

def df_ecef_to_geo(df, get_in_feet=True):
    '''
    get_in_feet: If True Returns Altitude in feet
                 else in meters
    '''
    
    x, y, z = df[['x']].values, df[['y']].values, df[['z']].values
    log, lat, alt = pyproj.transform(ecef, lla, x, y, z, radians=False)

    if get_in_feet == True:
        alt = alt/0.3048

    df_result = np.hstack((lat, log, alt))
    df_result = pd.DataFrame(df_result, columns=['Lat', 'Long', 'Alt'])

    return df_result
