# Weather Chatbot

This is a simple chatbot that can provide the current weather of a city. It uses the OpenWeatherMap API to retrieve weather information and spaCy library for natural language processing.

## Requirements
- Python 3.7 or above
- requests library
- spaCy library with the `en_core_web_md` model

## Installation
1. Clone the repository or download the code files.
2. Install the required libraries using pip:

3. Download the spaCy model:


## Usage
1. Run the script:
2. Enter your statement when prompted. For example:

3. The chatbot will analyze your statement and provide the current weather for the specified city, if available.

## Notes
- The chatbot uses spaCy's natural language processing capabilities to understand the user's statement. It looks for the pattern 'Current weather in a city' and extracts the city name from the statement.
- The OpenWeatherMap API is used to retrieve weather information based on the city name.
- The minimum similarity threshold for understanding the statement is set to 0.60. If the similarity between the statement and the weather pattern is below this threshold, the chatbot will ask the user to rephrase the statement.
- If there are any issues with the API or retrieving the weather information, an appropriate error message will be displayed.

Feel free to modify the code and experiment with different statements and functionalities of the chatbot.
