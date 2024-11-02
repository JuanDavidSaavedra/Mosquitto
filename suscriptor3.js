// suscriptor3.js
const mqtt = require('mqtt');
const client = mqtt.connect('mqtt://localhost:1883');

client.on('connect', () => {
  client.subscribe('topic/test', (err) => {
    if (!err) {
      console.log('suscriptor 3 conectado al topic');
    }
  });
});

client.on('message', (topic, message) => {
  console.log('suscriptor 3 recibió:', message.toString());
});