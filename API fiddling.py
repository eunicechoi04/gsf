import requests
import json

##GET requesting the API
response = requests.get('http://test.gsfmission.org/api/chat/')
print(response.text)


##POSTing the API
post_url = 'http://test.gsfmission.org/api/chat/'
data = {
  "patient_id": 2980,
  "fever": 1,
  "bleeding": 1,
  "appetite": 1,
  "breath": 1,
  "pus": 1,
  "vomit": 0,
  "diarrhea": 0,
  "urine": 0,
  "text": "Response to this question",
  "question_id": 5,
  "session": 15
}

response = requests.post(post_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
print(response.text)
