
import requests
import json
import os, sys
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

"""city_name = 'São Paulo'
state_code = 'São Paulo'
country_code = 'BR'"""

if len(sys.argv) > 3:
    city_name = sys.argv[1]
    state_code = sys.argv[2]
    country_code = sys.argv[3]
else:
    print("Uso: python OpenWeather.py <cidade> <estado> <país>")
    sys.exit(1)

API_key = os.getenv('OPENWEATHER_API_KEY')

geo_response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')
print("Resposta da Geocodificação:")
print(f"Status Code: {geo_response.status_code}")

if geo_response.status_code == 200:
    geo_data = json.loads(geo_response.text)
    
    if geo_data and len(geo_data) > 0:
        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']
        name = geo_data[0]['name']
        
        print(f"\nLocalização encontrada: {name}")
        print(f"Latitude: {lat}, Longitude: {lon}")
        
        forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}&units=metric&lang=pt_br'
        forecast_response = requests.get(forecast_url)
        
        print(f"\nStatus da previsão: {forecast_response.status_code}")
        
        if forecast_response.status_code == 200:
            forecast_data = json.loads(forecast_response.text)
            
            print(f"\n=== PREVISÃO DO TEMPO PARA {name.upper()} ===")
            
            for i in range(min(7, len(forecast_data['list']))):
                item = forecast_data['list'][i]
                
                dt = datetime.fromtimestamp(item['dt'])
                temp = item['main']['temp']
                feels_like = item['main']['feels_like']
                humidity = item['main']['humidity']
                description = item['weather'][0]['description']
                
                print(f"\n📅 {dt.strftime('%d/%m/%Y %H:%M')}")
                print(f"🌡️  Temperatura: {temp}°C (sensação: {feels_like}°C)")
                print(f"💧 Umidade: {humidity}%")
                print(f"☁️  Condição: {description.title()}")
                print("-" * 40)
        else:
            print("Erro ao obter previsão do tempo")
            print(forecast_response.text)
    else:
        print("Cidade não encontrada")
else:
    print("Erro na geocodificação")
    print(geo_response.text)