import helper
from tqdm import tqdm
from  flask import Flask,request,render_template,redirect
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import plotly.graph_objects as go
from itertools import chain
import plotly.express as px
import plotly
import json
df=pd.read_pickle("df.csv" + '.pkl')
df=df[df.popularity>0.3]

def recomends(name,artist):
    name=name.casefold()
    artist=artist.casefold()
    dist=[]
    songs=df[df.track_name==name]
    songs=songs[songs.artist_name==artist].head(1).values[0]
    dropsong=df[df.track_name!=name]
    for r_song in tqdm(dropsong.values):
        distance = 0
        for i in np.arange(len(dropsong.columns)):
            if not i in[0,1,2,3,10,13,16]:
                distance = distance + np.absolute(float(songs[i]) - float(r_song[i]))
        dist.append(distance)
    dropsong['distance'] = dist
        #sorting our data to be ascending by 'distance' feature
    dropsong = dropsong.sort_values('distance')
    columns = ['artist_name', 'track_name']
    return dropsong[columns]
def result(name,artist):
    result=recomends(name,artist).reset_index()
    result=result.head(10)
    for i in range(len(result.track_name)):
       result.track_name[i]=str.title(result.track_name[i])
    for i in range(len(result.artist_name)):
       result.artist_name[i]=str.title(result.artist_name[i])
    result=result.drop('index',axis=1)
    result=result.drop_duplicates()
    return result
def result1(name,artist):
    result=recomends(name,artist).reset_index()
    result=result.head(10)
    for i in range(len(result.track_name)):
       result.track_name[i]=str.title(result.track_name[i])
    for i in range(len(result.artist_name)):
       result.artist_name[i]=str.title(result.artist_name[i])
    result=result.drop_duplicates()
    return result
def getlen(name,artist):
    name=name.casefold()
    artist=artist.casefold()
    songs=df[df.track_name==name]
    songs=songs[songs.artist_name==artist]
    length=len(songs)
    return length
def chartshow(name,artist):
    name=name.casefold()
    artist=artist.casefold()   
    chartdf=df[df.track_name==name]
    chartdf=chartdf[chartdf.artist_name==artist].head(1)
    num_types = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    numdf2= chartdf.select_dtypes(include=num_types)
    data=numdf2.head(1).values
    data=data.tolist()
    label = numdf2.columns
    label=label.tolist()
    data= list(chain.from_iterable(data))
# Use `hole` to create a donut-like pie chart
    figpi = go.Figure(data=[go.Pie(labels=label, values=data, hole=.6,title=f"{str.title(name)} Stats",)])
    graph=json.dumps(figpi,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def chartshow2(result):
    name=result.head(1)
    name=name['track_name']
    name=name[0]
    ind=result.head(1)
    ind=ind['index'].values
    ind=ind[0]  
    resultin=df[df.index==ind]
    num_types = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    numdf= resultin.select_dtypes(include=num_types)
    data=numdf.head(1).values
    data=data.tolist()
    label = numdf.columns
    label=label.tolist()
    data= list(chain.from_iterable(data))
    figpi = go.Figure(data=[go.Pie(labels=label, values=data, hole=.6,title=f"{name} Stats",)])
    graph=json.dumps(figpi,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
