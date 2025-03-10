import random
import requests

# 3 lists of 4 playlists for each weather type
rainy_playlists = ["https://open.spotify.com/playlist/37i9dQZF1DXbcPC6Vvqudd?si=c5b4_M6GQ3qX33rf2xejpw","https://open.spotify.com/playlist/37i9dQZF1DX2mFmJUZg4Mp?si=sBYpgnLFQeaOxoZstxlpjw","https://open.spotify.com/playlist/37i9dQZF1DWY8U6Zq7nvbE?si=E_scZ2W2Tt-qMhU0w7CiHQ","https://open.spotify.com/playlist/5m8hWoxPvKRFRW2Oer7RGA?si=ncBHt6y1RG-TM2QGd34QZQ"]
sunny_playlists = ["https://open.spotify.com/playlist/1lKj46rZMLXZ1uU0rhSI1Z?si=l3lECD0oTS-36Z9UvGoRmQ","https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC?si=XbqukbqtQVeNbMOKLYuqpA","https://open.spotify.com/playlist/37i9dQZF1DWSf2RDTDayIx?si=P2okoyLYTpapsCFtnQFA_g","https://open.spotify.com/playlist/37i9dQZF1DX5YTAi6JhwZm?si=JpMp5CIHSn6v4IpknDwdjA"]
cold_playlists = ["https://open.spotify.com/playlist/37i9dQZF1DX5IDTimEWoTd?si=tPir2k1PTqeCP3sNlrnEbg","https://open.spotify.com/playlist/37i9dQZF1DXaImRpG7HXqp?si=BtXpO9UsRvKwRttyPQqH9w","https://open.spotify.com/playlist/37i9dQZF1DWSwxyU5zGZYe?si=_x6t7infQFaRKTIou16tOA","https://open.spotify.com/playlist/37i9dQZF1DWT3gM3xdPT0c?si=F4hddmXUTliAFLu5qNJZEg"]

# Get weather data
def get_weather_data(city):
    """
    This function takes the city name as a parameter and then outputs the weather category like Clear, Cloud or other weather types.
    :param city:
    :return:
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?q=" #Base url for the api call
    api_key = open("api_key",'r').read() #The API key from openweathermap.org. It is advised to get your own API key from openweathermap.org for running this program on your device.
    # Also if you want to run this program, you'll need to replace the path to the api_key with your api key's file path

    url = base_url + city + "&appid=" + api_key # Concatenate the url components to a url for api call

    response = requests.get(url).json() # This stores the api call response in the response variable

    weather_main = response['weather'][0]['main'] #extracting the broad weather category from the api response

    return weather_main #returning the weather category

def welcome():
    """
    This is the function where all the other functions are managed and coordinated to-
    1. Take the city name as input
    2. Choose the playlist by the weather type/category
    3. print out the final result
    :return:
    """
    print("Welcome to The Playlist By Weather application!")
    city = input("Enter your city name: ") # please enter the city name here
    weather = get_weather_data(city)  #This calls the function to get the weather category of the city that the user inputted from openweatherapi
    final_playlist = choose_playlist(weather) # This calls the function to choose the playlist given the weather category of the city
    print(f"The weather in {city} is {weather}.\nYour ideal playlist based on the {weather} weather in {city} is:\n{final_playlist}") # This prints the final result and the final playlist based on the weather

def choose_playlist(weather):
    """
    This function chooses among rainy, sunny and cold weather based on the weather category received from the openweatherapi
    :param weather:
    :return:
    """
    rainy_weathers = ['Thunderstorm','Drizzle','Rain','Haze','Squall','Tornado','Clouds'] # These broad categories are assumed to be rainy weathers
    sunny_weathers = ['Sand','Dust','Ash','	Clear'] # These broad categories are assumed to be sunny weathers
    cold_weathers = ['Fog','Snow','Mist','Smoke'] # These broad categories are assumed to be cold weathers

    #This if-elif-else block checks if the weather from the openweatherapi is in which weather among rainy, sunny and cold weathers.
    if weather in rainy_weathers:
        return random.choice(rainy_playlists) # randomly chooses from the rainy playlist link list
    elif weather in sunny_weathers:
        return random.choice(sunny_playlists) # randomly chooses from the sunny playlist link list
    elif weather in cold_weathers:
        return random.choice(cold_playlists) # randomly chooses from the cold playlist link list
    else:
        return random.choice(sunny_playlists) # randomly chooses from the sunny playlist link list because it doesn't fall into any of the pre-defined 3 weathers


if __name__=="__main__": # Execution of the code starts from here.
    welcome()