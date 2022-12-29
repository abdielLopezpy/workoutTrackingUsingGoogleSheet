# Code to get information about exercises and send it to the Sheety app

This code does the following:

1. Imports the necessary libraries, `requests` and `datetime`.
2. Defines some variables necessary to make a request to the Nutritionix API: `GENDER`, `WEIGHT_KG`, `HEIGHT_CM`, and `AGE`. These variables must be replaced with the appropriate values.
3. Defines two other variables necessary to make a request to the Nutritionix API: `APP_ID` and `API_KEY`. These variables must be replaced with the appropriate values obtained when registering on the Nutritionix platform.
4. Defines the variable `exercise_endpoint` with the URL of the Nutritionix API that will be used to get information about exercises. The variable `sheet_endpoint` is also defined with the URL of the Sheety app endpoint.
5. Asks the user to enter a description of the exercises they did.
6. Defines the headers for the request to the Nutritionix API.
7. Defines the parameters for the request to the Nutritionix API.
8. Makes a request to the Nutritionix API using the `requests.post()` function and saves the response in the `response` variable.
9. Processes the response from the Nutritionix API using the `response.json()` function and saves the result in the `result` variable.
10. Gets the current date and time with the `datetime.now()` function and formats them to be saved in the variables `today_date` and `now_time`, respectively.
11. Iterates over each exercise in the result obtained from the Nutritionix API. For each exercise, a dictionary is constructed with the information necessary to make a request to the Sheety app.
12. Makes a request to the Sheety app using the `requests.post()` function and saves the response in the `sheet_response` variable.
13. Prints the response from the Sheety app using the `sheet_response.text` function.
