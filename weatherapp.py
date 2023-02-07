from tkinter import*
import requests
import json
from tkinter import messagebox
root = Tk()
root.title("Weather Application")
#root.geometry("200x200")
#root.configure(background = "Red")

'''
{'location': {'name': 'London', 'region': 'City of London, Greater London', 'country': 'United Kingdom', 'lat': 51.52, 'lon': -0.11, 'tz_id': 'Europe/London', 'localt
ime_epoch': 1630146223, 'localtime': '2021-08-28 11:23'}, 'current': {'last_updated_epoch': 1630145700, 'last_updated': '2021-08-28 11:15', 'temp_c': 18.0, 'temp_f':
64.4, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 5.6, 'wind_kph': 9.0, '
wind_degree': 20, 'wind_dir': 'NNE', 'pressure_mb': 1026.0, 'pressure_in': 30.3, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 68, 'cloud': 75, 'feelslike_c': 18.0,
 'feelslike_f': 64.4, 'vis_km': 10.0, 'vis_miles': 6.0, 'uv': 4.0, 'gust_mph': 12.8, 'gust_kph': 20.5}}

'''
def search_me():
    try:
        location = location_input.get()
        api_request = requests.get("https://api.weatherapi.com/v1/current.json?key=2f3518d651f54405a05101438212808&q="+str(location)+"&aqi=no")
        my_api = json.loads(api_request.content)
        city = my_api["location"]["name"]
        tempcelc = my_api["current"]["temp_c"]
        tempfah = my_api["current"]["temp_f"]
        condition = my_api["current"]["condition"]["text"]
        update = my_api["current"]["last_updated"]
        new = Toplevel()
        title = Label(new, text = "Weather report", font = ("Helvetica", 10))
        the_city = Label(new, text="city = "+ city, font=("Helvetica", 10))
        temperature = Label(new, text= "Temperature ="+str(tempcelc)+ " Celcius" + " or " + str(tempfah) +" Fahrenheit", font=("Helvetica", 10))
        thecondition = Label(new, text="Condition" + " = " + condition , font=("Helvetica", 10))
        updatetime = Label(new, text= "Last updated " +"= " + str(update), font=("Helvetica", 10))
        title.grid(row= 0, column =0, padx= 10, pady = 8 )
        the_city.grid(row=1, column=0, padx= 10, pady = 8)
        temperature.grid(row=2, column=0, padx= 10, pady = 8)
        thecondition.grid(row=3, column=0, padx= 10, pady = 8)
        updatetime.grid(row=4, column=0, padx= 10, pady = 8)
    except:
        error = messagebox.showerror("Error", "Please enter a valid location")
        errorlabel = Label(root, text=error)
        errorlabel.pack()



my_label = Label(root,text = "Please enter the location.", font = ("Helvetica", 13))
location_input = Entry(root, font = ("Helvetica", 13), border=7)
my_label.grid(row = 0,column =0, padx=8,pady=6)
location_input.grid(row=1,column=0,padx=8,pady=5)
search_button = Button(root, text = "Search", font = ("Helvetica", 9), border = 6, command = search_me)
search_button.grid(row=2,column=0,padx=8,pady=5)


root.mainloop()