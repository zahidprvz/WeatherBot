import requests
import spacy

nlp = spacy.load("en_core_web_md")

api_key = "35e041b8938a60daf2bad6e6275e626a"

def get_weather(city_name):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)

    response = requests.get(api_url)
    response_dict = response.json()

    if response.status_code == 200:
        weather = response_dict["weather"][0]["description"]
        return weather
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None


def chatbot(statement):
    weather = nlp("Current weather in a city")
    statement = nlp(statement)
    min_similarity = 0.60

    if weather.similarity(statement) >= min_similarity:
        for ent in statement.ents:
            if ent.label_ == "GPE":  # GeoPolitical Entity
                city = ent.text
                break
            else:
                return "You need to tell me a city to check."

        city_weather = get_weather(city)
        if city_weather is not None:
            return "In " + city + ", the current weather is: " + city_weather
        else:
            return "Something went wrong."
    else:
        return "Sorry, I don't understand that. Please rephrase your statement."


user_input = input("Please enter your statement: ")
response = chatbot(user_input)
print(response)
