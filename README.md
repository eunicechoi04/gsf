all of this is in your terminal

# Creating a Virtual Environment (Optional)

\*\*replace YOUR-VENV-NAME with whatever name you want lol\*\*

## On Windows

`python -m venv YOUR-VENV-NAME`
`YOUR-VENV-NAME\Scripts\activate`

## On macOS/Linux

`python3 -m venv YOUR-VENV-NAME`
`source YOUR-VENV-NAME/bin/activate`

# Downloading Dependencies

\*\*You can do this on your local device or in your virtual environment\*\*
`pip install -r requirements.txt`

# For Testing

Make a ngrok account and find your authtoken
`ngrok config add-authtoken YOUR-AUTHTOKEN`
Open a split terminal. Run the whatsapp.py file and in the other terminal type:
`ngrok http 5002`

Go to Twilio's Sandbox and text their number "join actual-triangle". In the Settings, copy and paste the ngrok fowarding URL into the HTTP post box.
