# Imports
import requests
import subprocess
from tkinter import *
from tkinter import messagebox

# Functions
def get_weather():
    try:
        api_key = '30d4741c779ba94c470ca1f63045390a'

        user_input = enter_city_entry.get()

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            messagebox.showerror("Error: No city found!")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])

            message = f"The weather in {user_input} is: {weather}\nThe temperature in {user_input} is: {temp}ºF"
            messagebox.showinfo("Weather Info", message)
    except:
        messagebox.showerror("Error!", "Cannot get Weather Info!")

def get_weather_in_c():
    try:
        api_key = '30d4741c779ba94c470ca1f63045390a'

        user_input = enter_city_entry.get()

        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            messagebox.showerror("Error: No city found!")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            converted_temp = round((temp - 32) * 5 / 9)

            message = f"The weather in {user_input} is: {weather}\nThe temperature in {user_input} is: {converted_temp}ºC"
            messagebox.showinfo("Weather Info", message)
    except:
        messagebox.showerror("Error!", "Cannot get Weather Info!")

def get_full_data(weather_data_2):
    try:
        file = open("weather_data.txt", "a")
        file.write(weather_data_2.json())
        file.close()

        file = open("weather_data", "r")
        subprocess.open("weather_data.txt")

    except:
        messagebox.showerror("Error!", "Error: Cannot get Full Weather Data!")

# GUI Setup
window = Tk()
window.title("PyWeather")
window.config(padx=25, pady=25)

# Labels
weather_label = Label(text="PyWeather", font=('Areal', 25))
weather_label.grid(row=0, column=0, sticky='w')

placeholder_label = Label(text="")
placeholder_label.grid(row=1, column=0)

enter_city_label = Label(text="Enter city:")
enter_city_label.grid(row=2, column=0, sticky='w')

placeholder_label_2 = Label(text="")
placeholder_label_2.grid(row=3, column=0)

# Entries
enter_city_entry = Entry(width=35)
enter_city_entry.grid(row=2, column=1, sticky=W)

# Buttons
find_weather_button = Button(text="Find Weather in °F", command=get_weather)
find_weather_button.grid(row=4, column=0, sticky='w')

find_weather_in_f_button = Button(text="Find Weather in °C", command=get_weather_in_c)
find_weather_in_f_button.grid(row=5, column=0, sticky='w')

get_full_weather_data = Button(text="Get Full Weather Date", command=get_full_data)
# get_full_weather_data.grid(row=3, column=2)

# GUI Loop
window.mainloop()
