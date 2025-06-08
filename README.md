##  Weather Agent

A simple Python-based AI agent that fetches real-time weather data and generates personalized weather insights using OpenRouter's LLMs.


### Features

* Retrieves live weather data using OpenWeatherMap API
* Processes the data through an AI model on OpenRouter
* Returns a human-readable summary and actionable recommendations
* Fully modular: `perceive → process → act` agent architecture

---

### Tech Stack

* Python 3.10+
* [OpenWeatherMap API](https://openweathermap.org/api)
* [OpenRouter.ai](https://openrouter.ai)
* Dotenv for API key management

---

### Setup Instructions

#### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/Weather_Agent.git
cd Weather_Agent
```

#### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Add your API keys

Create a `.env` file in the root directory:

```env
WEATHER_API_KEY=your_openweathermap_key
OPENROUTER_API_KEY=your_openrouter_key
```

---

### Running the Agent

```bash
python main.py
```

You'll be prompted to enter a city. The agent will:

1. Fetch the weather
2. Ask the LLM to analyze it
3. Print weather insights and recommendations

---


### Sample Output
Enter a city name: lagos

🌍 Fetching weather for lagos...

📍 Weather in Lagos:
🌡️  Temp: 25.34°C
🌥️  Conditions: overcast clouds
💧  Humidity: 91%
🌬️  Wind: 1.96 m/s

🧠 Weather Recommendation:
Okay, here's a summary of the weather and some activity/outfit suggestions based on that data:

**Weather Summary:**

The weather in Lagos is cloudy (overcast). The temperature is pleasant but warm, hovering around **25°C**, which is comfortable for most outdoor activities without requiring heavy clothing. However, the high **humidity (91%)** is noticeable, making it feel a bit sticky and potentially warmer than the actual temperature might suggest. There's a very **light breeze (1.96 m/s)**, so it's not particularly cool or warm from the wind.

**Outfit & Activity Ideas:**

1.  **Outfit Idea 1: Casual Comfort**
    *   **Why:** High humidity calls for breathable fabrics (cotton, linen). Light layers allow adjustment if it were slightly warmer, but aren't too heavy for this temperature.
    *   **Suggestion:** Light-coloured, comfortable pants or shorts with a breathable, short-sleeved shirt or top. Perhaps bring a lightweight, packable rain jacket just in case the overcast sky brings any passing showers, even if unlikely.

2.  **Activity Idea 1: Gentle Exploration**
    *   **Why:** Comfortable temperature is ideal for walking or exploring around town. Low humidity means it won't be oppressive for extended periods. Overcast conditions are beautiful for photo opportunities without harsh sunlight.
    *   **Suggestion:** Take a walk through a neighborhood you haven't seen in a while or walk part of a popular beach area like Bar Beach in the evening for a gentler pace.

3.  **Activity Idea 2: Sustainable Staying Cool Indoors**
    *   **Why:** High humidity is challenging. The light wind means it won't help with cooling much. An air-conditioned indoor space offers a reliable escape.
    *   **Suggestion:** Visit a museum (like the Ibeju-Ijaiye Olugbenga-Olubuseun Museum), explore a specific area known for good food away from the heat, or spend time in an air-conditioned café with a light meal or drink.      

4.  **Activity Idea 3: Wind-Appropriate Exercise**
    *   **Why:** Very light wind isn't enough to be too hot during exercise but also won't provide significant cooling.
    *   **Suggestion:** A light workout like jogging or yoga indoors is comfortable. Alternatively, joining a windsurfing session (joule) on one of Lagos' beaches might be appealing despite the minimal wind, using motorised boards to get started. If the wind picks up unexpectedly while at the beach (though unlikely based on data), activities like paddleboarding or casual swimming become feasible. **(Note: The wind speed is too low for most watersports without motor assistance).**

---

###  Project Structure

```
Weather_Agent/
│
├── main.py              # Main agent logic
├── .env                 # API keys (not tracked by git)
├── .gitignore
└── README.md
```

---

### Contributing
PRs welcome! Feel free to add features like:
- Telegram/Discord bot integration
- Weather history logging
- Web frontend

---

### License

MIT License — free to use, modify, and distribute.

---

### 🤖 Credits

* Built by [Ese Monday](https://x.com/EseMonday1)
* Powered by [OpenWeatherMap](https://openweathermap.org/) and [OpenRouter](https://openrouter.ai/deepseek/deepseek-r1-0528-qwen3-8b:free/api)



