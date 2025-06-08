import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Check if the API keys are set
if not WEATHER_API_KEY or not OPENROUTER_API_KEY:
    raise ValueError("Please set the WEATHER_API_KEY and OPENROUTER_API_KEY in your .env file.")    
# Initialize OpenAI client

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

# Function to get weather data
class WeatherAgent:
    def __init__(self):
        self.weather_api_key = WEATHER_API_KEY
    
    def perceive(self, location):
        """Fetch weather data from OpenWeather"""
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.weather_api_key}&units=metric"
        response = requests.get(url)
        return response.json()
    
    def process(self, weather_data):
        """Use OpenRouter GPT to generate recommendations"""
        city = weather_data.get('name', 'Unknown City')
        temp = weather_data['main']['temp']
        desc = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind = weather_data['wind']['speed']

        # 📋 Log the raw details (you’ll see this in terminal)
        print(f"\n📍 Weather in {city}:")
        print(f"🌡️  Temp: {temp}°C")
        print(f"🌥️  Conditions: {desc}")
        print(f"💧  Humidity: {humidity}%")
        print(f"🌬️  Wind: {wind} m/s")

        
        
        prompt = f"""
        The weather in {city} is:
        - Temperature: {temp}°C
        - Conditions: {desc}
        - Humidity: {humidity}%
        - Wind Speed: {wind} m/s

        Based on this, summarize the weather and suggest 3 outfit or activity ideas.
        """
        completion = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528-qwen3-8b:free",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    def act(self, message):
        print("\n🧠 Weather Recommendation:")
        print(message)


    def run(self, location):
        print(f"\n🌍 Fetching weather for {location}...")
        weather_data = self.perceive(location)
        summary = self.process(weather_data)
        self.act(summary)   

    
if __name__ == "__main__":
    city = input("Enter a city name: ")
    agent = WeatherAgent()
    agent.run(city)