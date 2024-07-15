import requests
from datetime import datetime, timedelta

def search_city(query):
    api_key = "c72b9093a1a50d253b1b1ce5130148c4"  # Replace with your OpenWeatherMap API key
    url = f'https://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if not data:
            return None
        
        if len(data) == 1:
            city_info = {
                'name': data[0]['name'],
                'country': data[0]['country'],
                'lat': data[0]['lat'],
                'lon': data[0]['lon']
            }
            return city_info
        else:
            print(f"Multiple matches found, which city did you mean?")
            for idx, city in enumerate(data, 1):
                print(f"{idx}. {city['name']},{city['country']}")
            
            selection = input("> ")
            try:
                index = int(selection) - 1
                if 0 <= index < len(data):
                    city_info = {
                        'name': data[index]['name'],
                        'country': data[index]['country'],
                        'lat': data[index]['lat'],
                        'lon': data[index]['lon']
                    }
                    return city_info
                else:
                    return None
            except ValueError:
                return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching city data: {e}")
        return None
    
def weather_forecast(lat, lon):
    api_key = "c72b9093a1a50d253b1b1ce5130148c4"  # Replace with your OpenWeatherMap API key
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            forecasts = data['list']
            forecast_info = {}
            
            for forecast in forecasts:
                timestamp = forecast['dt']
                date = datetime.utcfromtimestamp(timestamp)
                
                # Fetching weather details
                weather_description = forecast['weather'][0]['description']
                temp = forecast['main']['temp']
                
                # Formatting date to YYYY-MM-DD
                formatted_date = date.strftime('%Y-%m-%d')
                
                # Collecting forecast information
                if formatted_date not in forecast_info:
                    forecast_info[formatted_date] = f"{formatted_date}: {weather_description} {temp}°C"
            
            return list(forecast_info.values())
        
        else:
            print(f"Error fetching weather data: {data['message']}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def main():
    while True:
        print("City?")
        city = input("> ")
        
        if not city:
            break
        
        city_info = search_city(city)
        
        if not city_info:
            print("City not found. Please try again.")
            continue
        
        print(f"Here's the weather forecast in {city_info['name']}, {city_info['country']} for the next 5 days:")
        forecasts = weather_forecast(city_info['lat'], city_info['lon'])
        
        if forecasts:
            for forecast in forecasts:
                print(forecast)
        
        print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
