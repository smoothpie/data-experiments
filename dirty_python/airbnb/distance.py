#%%
import numpy as np
import math

lon1 = -103.548851
lat1 = 32.0004311
lon2 = -103.6041946
lat2 = 33.374939


def haversine(lat1, lon1, lat2, lon2):
  R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km

  dLat = np.radians(lat2 - lat1)
  dLon = np.radians(lon2 - lon1)
  lat1 = np.radians(lat1)
  lat2 = np.radians(lat2)

  a = math.sin(dLat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dLon/2)**2
  c = 2*math.asin(math.sqrt(a))

  return R * c

print(haversine(lat1, lon1, lat2, lon2))