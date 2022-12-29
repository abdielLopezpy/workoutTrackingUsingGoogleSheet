import requests
from datetime import datetime

# Replace these variables with your own values
GENDER = YOUR GENDER
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE

# Replace these variables with your own values obtained from the Nutritionix platform
APP_ID = YOUR NUTRITIONIX APP ID
API_KEY = YOUR NUTRITIONIX API KEY

# URL of the Nutritionix API endpoint to get information about exercises
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# URL of the Sheety app endpoint
sheet_endpoint = YOUR SHEETY ENDPOINT

# Ask the user to enter a description of the exercises they did
exercise_text = input("Tell me which exercises you did: ")

# Headers for the request to the Nutritionix API
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Parameters for the request to the Nutritionix API
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Make a request to the Nutritionix API and get the response
response = requests.post(exercise_endpoint, json=parameters, headers=headers)

# Process the response from the Nutritionix API
result = response.json()

# Get the current date and time and format them
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Iterate over each exercise in the result from the Nutritionix API
for exercise in result["exercises"]:
    # Construct a dictionary with the information needed to make a request to the Sheety app
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Make a request to the Sheety app and get the response
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # Print the response from the Sheety app
    print(sheet_response.text)
