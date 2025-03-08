import datetime as dt
import requests

# 3 lists of 4 playlists for each weather type
rainy_playlists = ["https://open.spotify.com/playlist/37i9dQZF1DXbcPC6Vvqudd?si=c5b4_M6GQ3qX33rf2xejpw","https://open.spotify.com/playlist/37i9dQZF1DX2mFmJUZg4Mp?si=sBYpgnLFQeaOxoZstxlpjw","https://open.spotify.com/playlist/37i9dQZF1DWY8U6Zq7nvbE?si=E_scZ2W2Tt-qMhU0w7CiHQ","https://open.spotify.com/playlist/5m8hWoxPvKRFRW2Oer7RGA?si=ncBHt6y1RG-TM2QGd34QZQ"]
sunny_playlists = ["https://open.spotify.com/playlist/1lKj46rZMLXZ1uU0rhSI1Z?si=l3lECD0oTS-36Z9UvGoRmQ","https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC?si=XbqukbqtQVeNbMOKLYuqpA","https://open.spotify.com/playlist/37i9dQZF1DWSf2RDTDayIx?si=P2okoyLYTpapsCFtnQFA_g","https://open.spotify.com/playlist/37i9dQZF1DX5YTAi6JhwZm?si=JpMp5CIHSn6v4IpknDwdjA"]
cold_playlists = ["https://open.spotify.com/playlist/37i9dQZF1DX5IDTimEWoTd?si=tPir2k1PTqeCP3sNlrnEbg","https://open.spotify.com/playlist/37i9dQZF1DXaImRpG7HXqp?si=BtXpO9UsRvKwRttyPQqH9w","https://open.spotify.com/playlist/37i9dQZF1DWSwxyU5zGZYe?si=_x6t7infQFaRKTIou16tOA","https://open.spotify.com/playlist/37i9dQZF1DWT3gM3xdPT0c?si=F4hddmXUTliAFLu5qNJZEg"]

# Get weather data
def get_weather_data():
    base_url = "http://api.openweathermap.org/data/2.5/weather?id=" #Base url for the api call
    api_key = open("api_key",'r').read() #The API key from openweathermap.org. It is advised to get your own API key from openweathermap.org for running this program on your device.
    # Also if you want to run this program, you'll need to replace the path to the api_key with your api key's file path

    city_code = "1275004" # City Code For Kolkata, India 

    url = base_url + city_code + "&appid=" + api_key # Concatenate the url components to a url for api call

    print(url)
    #response = requests.get(url).json()

    #print(response)

if __name__=="__main__":
    get_weather_data()