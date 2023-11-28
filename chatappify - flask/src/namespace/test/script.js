const chatForm = document.getElementById('websocket-form');
const textarea = document.getElementById('websocket-messages');
const chatInput = document.getElementById('websocket-input');

const socket = io("http://127.0.0.1:5000/chat");

// Emit events

socket.on('connect', () => {
  socket.emit('join', {
    "username": 'test',
    "room": 'test'
  })
});

chatForm.addEventListener('submit', (e) => {
  e.preventDefault();
  console.log('submit');
  socket.emit('send_message', {
    "username": 'test',
    "room": 'test',
    "message": chatInput.value
  });
});

chatInput.addEventListener('input', (e) => {
  console.log('input');
  socket.emit('typing', {
    "username": 'test',
    "room": 'test'
  });
});

// Listen Events

socket.on('send_message', (data) => {
  const { username, room, message } = data;
  console.log('send_message', data);
  textarea.value += `${username}: ${message}\n`
});

socket.on('typing', (data) => {
  const { username, room } = data;
  console.log('typing', data);
  textarea.value += `${username} is typing...\n`
});