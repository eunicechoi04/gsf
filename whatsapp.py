from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# TODO: put into env file later
account_sid = 'AC6d19c6813aeec23e8fa4b8b3f508c58d'
auth_token = 'd0aa8702b3607893cce4e67d3ccffc7e'

client = Client(account_sid, auth_token)
whatsapp_number = '14155238886'


app = Flask(__name__)
@app.route("/", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body('Hello! This is the Global Smile Foundation post-operative chat. What can I help you with today?')
    print(incoming_msg)
    return str(resp)

if __name__ == "__main__":
    app.run(port=5002)