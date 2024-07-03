# A.L.I.C.E. (Automated Listening and Interactive Chat Engine)

## Overview

A.L.I.C.E. (Automated Listening and Interactive Chat Engine) is a versatile Python-based application designed to offer a comprehensive suite of interactive features. The program allows users to interact with a variety of services including  displays real date and time, chatting, logging in, signing up, performing calculations, capturing screenshots, webcam capture, conducting internet speed tests, accessing a knowledge base, opening applications, translation, and weather updates.


## Features

- User-friendly console interface.
- Display real date and time.
- Real-time chatting and interaction.
- User authentication using database connections for secure access.
- Integrated calculator for quick computations.
- Screen capture and webcam capture functionalities.
- Internet speed test.
- Knowledge base integration trained in Java.
- Application launching capabilities.
- Translation services.
- Weather updates.


## Prerequisites

- Python 3.7.9
- MySQL Database
- Basic understanding of Python programming, socket programming, and MySQL.


## Usage


### Setup MySQL Database

1. Run file conn_database.py
2. Run file conn_tables.py
   - Note: Edit the data entry present in conn_table as required.


### Install Dependencies

Make sure you have the required Python packages by installing them with:
Installations to be done for ALICE

Note: If you install or use any other libraries regarding the project please add it below following the convention as provided below.

Python version 3.7.9
IDE: Pycharm

For Chatterbot
	pip install "chatterbot==1.0.0"
	pip install pytz
	pip install pyyaml
	
For pyttsx3
	pip install pyttsx3

For Speech Recognition
	pip install "SpeechRecognition==3.8.1"
	pip install pipwin
	pipwin install pyaudio
	
For database
	pip install mysql-connector-python
	
For temperature
	pip install requests
	
For opening/closing app
	pip install pyautogui
	
For calculator
	pip install wolframaplha
	
For internet speed
	pip install speedtest-cli
	
For translator
	pip install googletrans==4.0.0-rc1
	
For splash screen
	pip install pillow
	pip install opencv-python
	pip install pygame

For .py to .exe
	pip install pyinstaller==3.5
	pyinstaller --onefile main.py


### Run the project
  - Run main.py


## Error Handling

The application handles common errors such as invalid input, connection issues, etc. Provides appropriate messages for errors and guides users to enter valid information.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Limitations

The application assumes a local MySQL setup for user authentication.
The chat application focuses on simplicity and real-time messaging without advanced features such as file sharing or multimedia.
Feel free to contribute and enhance the functionality of A.L.I.C.E.!


## Project Credits

Mehul S. Katwe: https://www.linkedin.com/in/mehul-katwe-746439285
Rafan R. Nadiadwala: https://www.linkedin.com/in/rafan-nadiadwala-062b70262
