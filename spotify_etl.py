from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET_KEY")

# print(client_id,client_secret)


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    data = {"grant_type":"client_credentials"}
    result = post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token  = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer" + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/artists{}"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)
    print(json_result)


token = get_token()
search_for_artist(token, "4YRxDV8wJFPHPTeXepOstw")
# print(token)

# BQDECClrRzxZP6MH6HyBlQPr6vDv8QVE4Mc9Cds1rqaLMl3BuvHWJr7cUAn3rDRHe2Vk_CLbizY4G5xVz5vOnjiBEVCZ_9B-uVHu4yPGNxdL3fV-nGDJ