
# Spotify-Song-Recommender

A flask app  which recommends songs similar to the one provided by the user.(Content Based Recommender System)

- The app uses K-means clustering algorithm  with 11 clusters for recommending songs. 

- User will provide the track name and the artist name based on which the app would generate the output.

- Searches are not case sensitive, app is optimised so that the user can enter in any case. 

- Note:-The dataset contains the record of  232,725 tracks only, So it may happen that some song entered by the user may not be present in the dataset so recommendation may not be generated instead the exception will be handled by the message "No match found!".  
  Some recommended searches to try:--   
  Dive --  Ed Sheeran             
  Rap God -- Eminem          
  Starboy -- The Weeknd         
  Water Fountain -- Alec Benjamin                             
  Gansta's Paradise -- Coolio      
  Instant Crush -- Daft Punk     
  or any popular song present in the dataset.

  


## Badges

[![Generic badge](https://img.shields.io/badge/build_with-python-yellow.svg)](https://en.wikipedia.org/wiki/Python_(programming_language))
[![Generic badge](https://img.shields.io/badge/-HTML-orange.svg)](https://en.wikipedia.org/wiki/HTML)
[![Generic badge](https://img.shields.io/badge/-CSS-blue.svg)](https://en.wikipedia.org/wiki/CSS)
[![Generic badge](https://img.shields.io/badge/using-flask-green.svg)](https://en.wikipedia.org/wiki/Flask_(web_framework))
[![Generic badge](https://img.shields.io/badge/deployed_in-heroku-7f03fc.svg)](https://en.wikipedia.org/wiki/Heroku)

## Datasource
Dataset used:--https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db




## Data Preprocessing
Data Preprocessing is done using python on jupyter notebook.  
ipynb file:- https://github.com/prakhar-198/notebook-Spotify-Song-Recommender

## Deployment

Web Development & Deployment: HTML,CSS and Python flask framework has been used for web development and the site is hosted on render as well.
Visit the app:--https://spotify-song-recommender-app.onrender.com
https://spotify-song-recommender-app.herokuapp.com/
