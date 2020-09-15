#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

new_path = r"C:\\Users\UserK\Desktop\py\jupyter\covid19\Korea\new.csv"
new=pd.read_csv(new_path, encoding='CP949')

new=new[:10]

new.shape
# In[2]:


# 주소를 좌표로 변환하는 API
import requests
import json

def xy(address) :

    KEY='AC7ABDBD-9A01-313D-AC9A-314F57E73E42'
    a=address.split()
    b=' '.join(a[:3])
    r=requests.get('http://api.vworld.kr/req/address?service=address&request=getcoord&version=2.0&crs=epsg:4326&address='+b+'&refine=false&simple=true&format=json&type=road&key='+KEY)
    R=r.json()

    if R['response']['status']=='OK' :
        return R['response']['result']['point']
    else :
        return {'x': '128.873523365', 'y': '37.786069974'}


# In[3]:


lat=[]
lng=[]

for i in range(len(new.주소)) :

    d=xy(new.주소[i])
    #print(d)
    lat.append(float(d['y']))
    lng.append(float(d['x']))


new['lat']=lat
new['lng']=lng


new.shape


# In[12]:


import folium
from folium.plugins import MarkerCluster

mc = MarkerCluster()
map2=folium.Map(location=[new.lat.mean(),new.lng.mean()],zoom_start=8)

for work, BP, la, ln in zip(new.작업내용, new.BP사, new.lat, new.lng) :
    mc.add_child(folium.Marker(location=[la,ln], popup=( work, BP)))
    map2.add_child(mc)

map2


# In[6]:


map2.save('C:/Users/UserK/Desktop/map2.html')


# In[ ]:
