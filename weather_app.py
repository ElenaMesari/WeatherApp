import streamlit as st
import requests
 
st.markdown("<h1 class='big-font'>⛅ Weather App</h1>", unsafe_allow_html=True)
 
city = st.text_input("Enter a city name", "New York")

st.markdown("---")

 
if st.button("Get Weather 🌦️"):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&format=json"
    response = requests.get(geo_url)

    if response.status_code == 200 and response.json().get("results"):
        location_data = response.json()["results"][0]
        latitude = location_data["latitude"]
        longitude = location_data["longitude"]

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            temp = weather_data["current_weather"]["temperature"]
            weather_condition = weather_data["current_weather"]["weathercode"]

            # Display weather data with enhanced styling
            st.markdown(f"<h2 class='weather-header'>🌡️ Temperature in {city}: {temp}°C</h2>", unsafe_allow_html=True)

            # Display additional information on weather condition
            if weather_condition == 0:
                st.success("☀️ Clear skies!")
            elif weather_condition == 1:
                st.warning("🌤️ Partly cloudy")
            elif weather_condition == 2:
                st.info("☁️ Cloudy")
            else:
                st.error("🌧️ Rainy!")
        else:
            st.error("❌ Failed to fetch weather data. Please try again later.")
    else:
        st.error("❌ City not found. Please check the name and try again.")
    
    
 
