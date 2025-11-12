# Text to Speech Converter

A simple GUI application for converting text to speech using Python's `pyttsx3` library.

## Features

- Convert any text to speech
- Choose between Male or Female voice
- Adjust speech speed (Fast, Normal, Slow)
- User-friendly graphical interface

## Requirements

- Python 3.x
- pyttsx3 library
- tkinter (usually comes with Python)

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python text_to_speech.py
```

1. Enter your text in the text box
2. Select your preferred voice (Male or Female)
3. Choose the speech speed (Fast, Normal, or Slow)
4. Click the "Play" button to hear the text

## Notes

- The application uses Windows SAPI5 voices by default
- If image files (logo3.png, logo4.png, play1.png) are missing, the application will still work but without the images
- The application will automatically find the correct voice based on your gender selection

