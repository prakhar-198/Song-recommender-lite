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
def getlen(name,artist):
    name=name.casefold()
    artist=artist.casefold()
    songs=df[df.track_name==name]
    songs=songs[songs.artist_name==artist]
    length=len(songs)
    return length
