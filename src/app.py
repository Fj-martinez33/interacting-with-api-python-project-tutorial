import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")

# Conect to Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

#Request to Spotify
# 6mdiAmATAx73kdxrNrnlao <-Iron Maiden

response = sp.artist_top_tracks(artist_id="6mdiAmATAx73kdxrNrnlao")

names = [response["tracks"][i]["name"] for i in range(9)]
duration = [response["tracks"][i]["duration_ms"] for i in range(9)]
duration = [i / 60000 for i in duration] #convertimos los milisegundos a minutos 1000 mseg = 1 seg, 60 seg = 1 min
popularity = [response["tracks"][i]["popularity"] for i in range(9)]
artists = [response["tracks"][i]["artists"][0]["name"] for i in range(9)]

tracks_dict = {"name" : names, "duration" : duration, "popularity" : popularity, "artist" : artists}

#Convert Dict to Dataframe

tracks = pd.DataFrame(tracks_dict).sort_values("popularity", ascending = False)

#Analize Data

graf = sns.scatterplot(data = tracks, x = "popularity", y = "duration").set_title("Relation Pop/Min")
figure = graf.get_figure()

print (tracks)
print(figure)
