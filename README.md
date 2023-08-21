# ChatRooms 💬

Welcome to the **ChatRooms** application! This project allows users to join chat rooms and communicate with each other in real-time using **WebSocket** technology.

![image](https://github.com/AnshumanRoy/chatRoom/assets/56593553/e91787ca-b293-4e22-982f-0782217dadb5)


## Features

- User **authentication** and **registration**
- Real-time chat functionality using **WebSockets**
- Join/create chat rooms
- Send and receive messages within chat rooms
- User-friendly interface

## Technologies

- Django 4.2: Python web framework
- Django Channels: Asynchronous framework for handling WebSockets
- Redis: Message broker for Django Channels
- HTML, CSS, JavaScript: Frontend development

## Getting Started

### Prerequisites

- Python 3.8+
- Redis server (for WebSocket support)

### Installation

1. Clone the repository:
   
   ```sh
   git clone https://github.com/AnshumanRoy/chatRoom.git
   cd chatRoom/mysite

2. Create a virtual environment (optional but recommended):

   ```sh
   python -m venv env
   env\Scripts\activate.bat

3. Install dependencies:

   ```sh
   pip install -r requirements.txt

4. Configure the Application:
   Create a new config.ini file in the folder containing **manage.py**. Edit it appropriately to set the necessary configuration values, such as database settings and channel layers configuration.

   ```ini
   [django]
   SECRET_KEY = your-secret-key
   DEBUG = True
    
   [database]
   DB_NAME = your-dbname
   DB_USER = your-dbuser
   DB_PASSWORD = your-dbpass
   DB_HOST = your-dbhost
   DB_PORT = your-dbport
    
   [channels]
   CHANNEL_HOST = your-channel-host
   CHANNEL_PORT = your-channel-port

6. Set up the database:

   ```sh
   python manage.py migrate

7. Start the development server:

   ```sh
   python manage.py runserverr

8. Access the application at http://localhost:8000 in your web browser.

## Usage

The application can be hosted locally, over the system IP address or on a domain. To have other users access the application, send them a link to the application in the browser after running it.

1. Register an account or log in.

   ### Landing page
   ![image](https://github.com/AnshumanRoy/chatRoom/assets/56593553/25e8a7ac-3a58-475c-a03f-a01a44ca3e29)

   ### Login page
   ![image](https://github.com/AnshumanRoy/chatRoom/assets/56593553/36eb5c09-26d6-4fda-be12-a7b580fbea87)

   ### Register page
   ![image](https://github.com/AnshumanRoy/chatRoom/assets/56593553/546c4fda-b8d8-4e00-8b9d-f780f8938da4)


3. Choose a chat room or create your own by entering an existing room name or choosing a new name.

   ![image](https://github.com/AnshumanRoy/chatRoom/assets/56593553/5bf08921-75ef-4067-ab4f-6eccb273cfdb)

5. Start chatting with other users in real-time!
