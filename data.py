import requests
import json
parameters = {
    "type": "boolean"
}
question_data = requests.get("https://opentdb.com/api.php?amount=20&category=31&type=boolean", params=parameters)
data = question_data.json()
quiz_questions = data['results']


