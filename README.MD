# 💬 Chatappify

## 📝 Description

Chatappify is a chat application that allows users to chat with each other in real-time. It is built with React, vite, Python, Flask, vanilla css and Socket.io. Its a good app to understand how the websockets work and how to implement them in your application.

## 🚀 Usage

To start using the app clone the repository and run the following commands:

```bash
cd chatappify - react
npm install
```

Then open another terminal and run the following commands:

```bash
cd chatappify - flask
pip install -r requirements.txt
```

One feature of the app is that this has the ability to crate dummy data with some flask commands that makes easy to test the app. To create dummy data run the following commands inside the flask folder:

```bash
flask init-db
flask test-data
flask fake-data
```

To start the app run the following commands:

```bash
cd chatappify - react
npm run dev
```

Then open another terminal and run the following commands:

```bash
cd chatappify - flask
flask run
```

## 📚 Requirements

- Python 3.9.5
- Node 14.17.0
- npm 6.14.13

## 📝 Diagrams

### Chatappify

![Alt text](<chatappify - assets/diagram-chatappify.png>)

### End to end encryption

![Alt text](<chatappify - assets/diagram-end-to-end-encryption.png>)

### Web socket

![Alt text](<chatappify - assets/diagram-web-socket.png>)

## ✔ Pending Tasks

- [ ] Solve repository contact problem
- [ ] Solve view of messages
- [ ] add E2E Encryption
