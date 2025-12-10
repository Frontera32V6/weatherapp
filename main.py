# from config import Config # w przypadku pobierania fukncji czy czegokolwiek innego musimy wykonać from xxx import xxx
# import pandas as pd
# import services.openweather # w przypadku pobierania pilku z innego folderu uzywamy ściezki, przy czym / zamieniamy na .
# # from services.openweather import fetchdata #w tej sytuacji moemy pobrać tylko jedną dokłądną funkcję z konkretnego pliku i potem 
# # services.openweather.fetchdata2() #zeby pobrać funkcję, clasę, itp nalezy wykonać odwołanie po ściezce
# import services.dashboard
# import time

from services.openweather_api import fetch_weather
from services.excel_files import save_to_excel, read_excel_file
from services.dashboard import create_plots
from services.mysql_db import create_record
from config import Config

weather=services.openweather.fetchweather()
# print(weather)

def save_to_excel(data):
    df=pd.DataFrame([data])
    df.to_excel("Weather_info.xlsx") #trzeba dodać rozszerzenie aby plik się utworzył
    return df
    
save_to_excel(weather)
services.dashboard.create_plots(weather)#oczekuje excela, którego mam zrobić 
print('Pobrałem dane!')
time.sleep(15)
    
