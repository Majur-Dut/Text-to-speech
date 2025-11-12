import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import os
import pyttsx3


root = Tk()
root.title("Text to Speech Converter")
root.geometry("1000x580+200+80")
root.resizable(False, False)
root.configure(bg="#F7AC40")


def speak_now():
    text = text_box.get(1.0, END).strip()
    gender = gender_box.get()
    speed = speed_box.get()

    if not text:
        return

    try:
        # Initialize TTS engine
        try:
            tts = pyttsx3.init(driverName='sapi5')
        except:
            tts = pyttsx3.init()

        voices = tts.getProperty('voices')

        # Select voice based on gender preference
        if gender == 'Male':
            # Try to find a male voice (usually contains 'David' or 'Male')
            for voice in voices:
                if 'david' in voice.name.lower() or 'male' in voice.name.lower():
                    tts.setProperty('voice', voice.id)
                    break
            else:
                # Fallback to first voice if no male voice found
                if len(voices) > 0:
                    tts.setProperty('voice', voices[0].id)
        else:
            # Try to find a female voice (usually contains 'Zira' or 'Female')
            for voice in voices:
                if 'zira' in voice.name.lower() or 'female' in voice.name.lower():
                    tts.setProperty('voice', voice.id)
                    break
            else:
                # Fallback to second voice if available, otherwise first
                if len(voices) > 1:
                    tts.setProperty('voice', voices[1].id)
                elif len(voices) > 0:
                    tts.setProperty('voice', voices[0].id)

        # Adjust speaking rate
        if speed == 'Fast':
            tts.setProperty('rate', 250)
        elif speed == 'Normal':
            tts.setProperty('rate', 150)
        else:
            tts.setProperty('rate', 60)

        # Speak and shut down engine
        tts.say(text)
        tts.runAndWait()
        tts.stop()
    except Exception as e:
        print(f"Error during speech: {e}")
        # Show error message to user
        import tkinter.messagebox as messagebox
        messagebox.showerror("Error", f"Failed to speak text: {e}")


# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Try to load logo image for window icon
try:
    logo_path = os.path.join(script_dir, "logo3.png")
    if os.path.exists(logo_path):
        logo_image = PhotoImage(file=logo_path)
        root.iconphoto(False, logo_image)
except Exception as e:
    print(f"Warning: Could not load logo3.png: {e}")

upper_frame = Frame(root, bg="#14A7DD", width=1200, height=190)
upper_frame.place(x=0, y=0)

# Try to load logo4.png for the header
try:
    picture_path = os.path.join(script_dir, "logo4.png")
    if os.path.exists(picture_path):
        picture = PhotoImage(file=picture_path)
        Label(upper_frame, image=picture, bg="#14A7DD").place(x=150, y=5)
except Exception as e:
    print(f"Warning: Could not load logo4.png: {e}")
# root.mainloop()

Label(upper_frame, text="Text to Speech Converter",
      font="TimesNewroman 40 bold", bg="#14A7DD", fg='white').place(x=340, y=60)
# root.mainloop()

text_box = Text(root, font="Arial 20", bg="white",
                relief=GROOVE, fg="black", wrap=WORD, bd=0)
text_box.place(x=10, y=200, width=980, height=180)
# root.mainloop()

gender_box = Combobox(
    root, values=['Male', 'Female'], font="Arial 14", state='r', width=10)
gender_box.place(x=250, y=400)
gender_box.set('Male')
# root.mainloop()

speed_box = Combobox(
    root, values=['Fast', 'Normal', 'Slow'], font="Arial 14", state='r', width=10)
speed_box.place(x=650, y=400)
speed_box.set('Normal')
# root.mainloop()

Label(root, text="Select Voice", font="Arial 14",
      bg="#F7AC40", fg="black").place(x=100, y=400)
Label(root, text="Select Speed", font="Arial 14",
      bg="#F7AC40", fg="black").place(x=500, y=400)
# root.mainloop()

# Try to load play button image
play_button = None
try:
    play_button_path = os.path.join(script_dir, "play1 (1).jpeg")
    if os.path.exists(play_button_path):
        play_button = PhotoImage(file=play_button_path)
except Exception as e:
    print(f"Warning: Could not load play1.png: {e}")

# Create play button with or without image
if play_button:
    play_butt = Button(
        root,
        text='Play',
        image=play_button,
        compound='bottom',  # Show text over image
        bg="#F7AC40",
        font='arial 14 bold',
        borderwidth='0.1c',
        activebackground="#F7AC40",
        bd=0,
        cursor="hand2",
        command=speak_now
    )
else:
    # Fallback button without image
    play_butt = Button(
        root,
        text='Play',
        bg="#F7AC40",
        font='arial 14 bold',
        borderwidth='0.1c',
        activebackground="#F7AC40",
        bd=0,
        cursor="hand2",
        command=speak_now,
        width=15,
        height=2
    )
play_butt.place(x=420, y=450)
root.mainloop()
