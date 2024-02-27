from tkinter import *
from tkinter import ttk
import requests 

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=be70f372605d1a717eee6af5269395a7").json()
    w_label1.config(text = data["weather"][0]["main"])
    wb_label1.config(text = data["weather"][0]["description"])
    temp_label1.config(text = str(int(data["main"]["temp"] -273.15)))
    per_label1.config(text = data["main"]["pressure"])
    
win = Tk()
win.title("Weather App")
win.config(bg="aqua")
win.geometry("500x500")

name_label = Label(win, text = "Nikon Weather App", font=("Time New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=40, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win, text = "Weather App", values = list_name,
                   font=("Time New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=40, width=450)

w_label = Label(win, text = "Weather Climate",
                font=("Time New Roman", 20))
w_label.place(x=25, y=260, height=30, width=220)
w_label1 = Label(win, text = "",
                font=("Time New Roman", 20))
w_label1.place(x=260, y=260, height=30, width=220)

wb_label = Label(win, text = "Weather Description",
                font=("Time New Roman", 18))
wb_label.place(x=25, y=310, height=30, width=220)
wb_label1 = Label(win, text = "",
                font=("Time New Roman", 18))
wb_label1.place(x=260, y=310, height=30, width=220)

temp_label = Label(win, text = "Temparature",
                font=("Time New Roman", 20))
temp_label.place(x=25, y=360, height=30, width=220)
temp_label1 = Label(win, text = "",
                font=("Time New Roman", 20))
temp_label1.place(x=260, y=360, height=30, width=220)

per_label = Label(win, text = "Pressure",
                font=("Time New Roman", 20))
per_label.place(x=25, y=410, height=30, width=220)
per_label1 = Label(win, text = "",
                font=("Time New Roman", 20))
per_label1.place(x=260, y=410, height=30, width=220)

done_button = Button(win, text = "Done",
                   font=("Time New Roman", 20, "bold"), command = data_get)
done_button.place(x = 200,y=190, height=40, width=100)

win.mainloop()