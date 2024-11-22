from customtkinter import *
from PIL import Image
from CTkListbox import *
import requests
import json


app = CTk()
app.geometry("900x400")
app.resizable(0,0)
app.title("Weather App")

def get_weather(city):
    API="9cf0321ea1ac572c76261a9a79ac0865"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        #print(f"Error: {response.status_code}")
        return None
    

def update_weather_info(city):
    
    weather_data = get_weather(city)
    if weather_data:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        pressure = weather_data["main"]["pressure"]
        max_temp = weather_data["main"]["temp_max"]
        min_temp = weather_data["main"]["temp_min"]
        coordinates = f"Lat: {weather_data['coord']['lat']}, Lon: {weather_data['coord']['lon']}"

        temperature_label.configure(text=f"Temperature: {temperature}°F")
        humidity_label.configure(text=f"Humidity: {humidity}%")
        description_label.configure(text=f"Description: {description}")
        pressure_label.configure(text=f"Pressure: {pressure} hPa")
        max_temp_label.configure(text=f"Max Temp: {max_temp}°F")
        min_temp_label.configure(text=f"Min Temp: {min_temp}°F")
        coordinates_label.configure(text=f"Coordinates: {coordinates}")
        error_label.configure(text="")

    else:
        error_label.configure(text="Invalid location! Please enter a valid city name.", text_color="red")


def direct():
    
    city = enter_city.get()
    update_weather_info(city)


side_img_data = Image.open("Image.jpg")
side_image = CTkImage(dark_image=side_img_data, 
                      light_image=side_img_data, 
                      size=(450, 400))

CTkLabel(master=app, text="", image=side_image).pack(expand=True, side="left")

frame = CTkFrame(master=app, 
                 width= 530, 
                 height= 400, 
                 fg_color="#8D6DF1")

frame.pack_propagate(0)

frame.pack(expand=True, side="right")


label1 = CTkLabel(master=frame, 
                  text="Search Bar", 
                  text_color="#FCFCFC", 
                  anchor="w", 
                  justify="left", 
                  font=("Arial Bold", 24))

label1.pack(anchor="w", pady=(50, 5), padx=(25, 0))

label1.place(relx=0.3, rely=0.05)

enter_city = CTkEntry(frame,fg_color="white",text_color="blue",width=200,height=10)

enter_city.pack(anchor="w", pady=10, padx=10)

enter_city.place(relx=0.10, rely=0.26)


button1 = CTkButton(master=frame, 
                    text="Get Weather", 
                    fg_color="blue", 
                    hover_color="red", 
                    font=("Arial Bold", 12), 
                    text_color="#ffffff", 
                    width=150,command=direct 
                    )

button1.pack(anchor="w",pady=10, padx=10)

button1.place(relx=0.45, rely=0.26)

temperature_label =CTkLabel(master=frame,text="", text_color="#FCFCFC", anchor="w", 
                  justify="left")
humidity_label = CTkLabel(master=frame,text="",text_color="#FCFCFC", anchor="w", 
                  justify="left")
description_label = CTkLabel(frame,text="",text_color="#FCFCFC", anchor="w", 
                  justify="left")
pressure_label = CTkLabel(frame,text="", text_color="#FCFCFC", anchor="w", 
                  justify="left")
max_temp_label = CTkLabel(frame,text="",text_color="#FCFCFC", anchor="w", 
                  justify="left")
min_temp_label = CTkLabel(frame,text="",text_color="#FCFCFC", anchor="w", 
                  justify="left")
coordinates_label = CTkLabel(frame,text="",text_color="#FCFCFC", anchor="w", 
                  justify="left")
response=CTkLabel(frame,text="",text_color="#FCFCFC", anchor="w", 
                  justify="left")  

temperature_label.pack()
temperature_label.place(x=100,y=175)
humidity_label.pack()
humidity_label.place(x=100,y=200)
description_label.pack()
description_label.place(x=100,y=225)
pressure_label.pack()
pressure_label.place(x=100,y=250)
max_temp_label.pack()
max_temp_label.place(x=100,y=275)
min_temp_label.pack()
min_temp_label.place(x=100,y=300)
coordinates_label.pack()
coordinates_label.place(x=100,y=325)

error_label = CTkLabel(master=frame, text="", text_color="red",height=5)
error_label.pack(pady=5)
error_label.place(x=75,y=175)


app.mainloop()



