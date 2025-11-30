from config import Config # w przypadku pobierania fukncji czy czegokolwiek innego musimy wykonać from xxx import xxx
import pandas as pd
import services.openweather # w przypadku pobierania pilku z innego folderu uzywamy ściezki, przy czym / zamieniamy na .
# from services.openweather import fetchdata #w tej sytuacji moemy pobrać tylko jedną dokłądną funkcję z konkretnego pliku i potem 
# services.openweather.fetchdata2() #zeby pobrać funkcję, clasę, itp nalezy wykonać odwołanie po ściezce

weather=services.openweather.fetchweather()
# print(weather)

def save_to_excel(data):
    df=pd.DataFrame([data])
    df.to_excel("Weather_info.xlsx") #trzeba dodać rozszerzenie aby plik się utworzył
    return df
    
save_to_excel(weather)
    
