import streamlit as st
import requests
import os

# Streamlit Secrets se API key lo
API_KEY = st.secrets["OPENWEATHER_API_KEY"]


st.set_page_config(page_title="🌤️ Weather App", page_icon="🌤️")
st.title("🌤️ Weather App")
st.write("Apni city ka naam daalein aur weather ka pata lagayein!")

# User input
city = st.text_input("City Name", "Haroonabad")

if city:
    # Weather data fetch function
    def get_weather(city_name):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ur"
        response = requests.get(url)
        return response.json()
    
    data = get_weather(city)
    
    if data.get("cod") == 200:
        st.subheader(f"Weather in {data['name']}, {data['sys']['country']}")
        st.write(f"**Temperature:** {data['main']['temp']}°C")
        st.write(f"**Feels Like:** {data['main']['feels_like']}°C")
        st.write(f"**Humidity:** {data['main']['humidity']}%")
        st.write(f"**Weather:** {data['weather'][0]['description'].title()}")
        st.write(f"**Wind Speed:** {data['wind']['speed']} m/s")
    else:
        st.error("City not found. Please check the spelling and try again.")
