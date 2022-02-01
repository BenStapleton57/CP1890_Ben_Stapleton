import tkinter as tk
from tkinter import ttk
import requests

# creating function to use button and access data

def get_weather_data():
    """
    Gets the weather data from the api key and sets the values for corresponding item
    """

    # construct URL to get weather info
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city = string_city_name.get()
    api_key = "f55f38dacebd7f35aee3e7d77d0c195a" # https://home.openweathermap.org/api_keys
    url = f'{base_url}q={city}&appid={api_key}'
    resp = requests.get(url)
    data = resp.json()


    if data["cod"] != "200":
        # making a dict for each piece of data
        data_dict = data["main"]
        data_dict_2 = data["wind"]
        data_dict_3 = data["weather"]

        # getting values
        current_temperature = data_dict["temp"]
        current_temperature -= 274.04
        current_temperature = round(current_temperature,2)

        feels_like = data_dict["feels_like"]
        feels_like -= 274.04
        feels_like = round(feels_like,2)


        wind_speed_mps = data_dict_2["speed"]
        wind_speed_mps *= 3.6
        wind_speed_mps = round(wind_speed_mps,2)

        wind_gust_mps = data_dict_2["gust"]
        wind_gust_mps *= 3.6
        wind_gust_mps = round(wind_gust_mps,2)

        weather_description = data_dict_3[0]["description"]

        # setting text box values
        city_temp.set(current_temperature)
        feels_like_temp.set(feels_like)
        wind_speed.set(wind_speed_mps)
        wind_gust.set(wind_gust_mps)
        summary.set(weather_description)

# create root
root =tk.Tk()
root.title('Weather App')
root.geometry('600x300')

# create main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand =True)

# add labels
ttk.Label(frame_home, text="Enter City Name: ").grid(column=0, row =0)
ttk.Label(frame_home, text="Current Temp(Cel): ").grid(column=0, row =2)
ttk.Label(frame_home, text="Feels Like Temp(Cel): ").grid(column=0, row =3)
ttk.Label(frame_home, text="Summary: ").grid(column=0, row =4)
ttk.Label(frame_home, text="Wind Speed(KM/H): ").grid(column=0, row =5)
ttk.Label(frame_home, text="Wind GustKMH/H: ").grid(column=0, row =6)

# text boxes for city and data
string_city_name = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_city_name).grid(column=2, row=0)

city_temp = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=city_temp).grid(column=2, row=2)

feels_like_temp = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=feels_like_temp).grid(column=2, row=3)

summary = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=summary).grid(column=2, row=4)

wind_speed = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=wind_speed).grid(column=2, row=5)

wind_gust = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=wind_gust).grid(column=2, row=6)

# create get data button
ttk.Button(frame_home, width=30, text='Get Weather Data', command=get_weather_data).grid(column=1, row=1, columnspan=4)

root.mainloop()
