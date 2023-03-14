import json
import pandas as pd


#reading json file 
with open('response.json', 'r') as json_file:
	json_load = json.load(json_file)

# print(json_load)
# print(json_load['items'])



 
#extracting data from the data
data = json_load['items']
new_data = [] #creating empty list
for x in data:
	y = x['id'],x['name'],x['external_urls'],x['release_date'],x['type']
	new_data.append(y)
# print(new_data)



#converting into dataframe and creating csv file
spotify_data  = pd.DataFrame(new_data)
spotify_data.columns = ["Id", "Name", "Link", "Release_date", "Album"]
spotify_data.to_csv("/Users/mihirzala/myprojects/spotify.csv")
print(spotify_data)
