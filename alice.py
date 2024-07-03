import tkinter
import tkinter as tk
from tkinter import *
import ai_speak
import speech_recognition as sr
from knowledge_main import ALICE
from PIL import Image, ImageTk
import tkinter as tk
import threading
import time
import keyboard

root = tk.Tk()
root.title("ALICE")
root.config(bg='#b6d0e2')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 590
window_height = 700
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

chat_area_placeholder = "Type your message here..."


def start_alice():
    def activate_button():
        voice_input()

    # Function to check if spacebar is being held down for 2 seconds
    def check_spacebar():
        while True:
            if keyboard.is_pressed('space'):
                start_time = time.time()
                while keyboard.is_pressed('space'):
                    if time.time() - start_time >= 2:
                        activate_button()
                        break
                # Adjust sleep time to control the speed of checking
                time.sleep(0.1)
            else:
                time.sleep(0.1)

    spacebar_thread = threading.Thread(target=check_spacebar)
    spacebar_thread.start()

    def activate_f1():
        help_window = tk.Toplevel()
        help_window.geometry(f'750x650+{x-100}+{y}')
        help_window.title("Help")
        help_label = tk.Label(help_window, text="Commands", fg='red', font=("Arial", 18, "bold"))
        help_label.pack()
        lab1 = tk.Label(help_window, text='Functions', font=("Arial", 17, "underline"), underline=10)
        lab1.place(x=50 ,y=60)
        lab2 = tk.Label(help_window, text='Keywords', font=("Arial", 17,  "underline"), underline=10)
        lab2.place(x=520 ,y=60)
        col1_content = tk.Label(help_window,
                                text='''To find current Date\n\nTo find current Time\n\nTo find Weather\n\n\nTo open an application\n\nTo take a screenshot\n\nTo open camera\n\nTo calculate\n\n\nTo activate voice input\n\nTo open help section''',
                                font=("Arial", 12))
        col1_content.pack(side=tk.LEFT, padx=30, pady=20, anchor="w")

        col2_content = tk.Label(help_window,
                                text='''Date\n\nTime\n\nWeather or temperature\n or climate\n\nOpen + <Application name>\n\nScreenshot or screen\n\nCamera or Photo or Image\n\nCalculate or name of operation\nto be performed\n\nLong press Spacebar\n\nLong press f1''',
                                font=("Arial", 12), anchor='w')
        col2_content.pack(side=tk.RIGHT, padx=30, pady=20)


    # Function to check if f1 is being held down for 2 seconds
    def check_f1():
        while True:
            if keyboard.is_pressed('f1'):
                start_time = time.time()
                while keyboard.is_pressed('f1'):
                    if time.time() - start_time >= 2:
                        activate_f1()
                        break
                # Adjust sleep time to control the speed of checking
                time.sleep(0.1)
            else:
                time.sleep(0.1)

    f1_thread = threading.Thread(target=check_f1)
    f1_thread.start()

    def voice_input():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            ai_speak.speak("Listening... waiting for voice input")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

            try:
                print("Recognizing voice...")
                query = recognizer.recognize_google(audio)
                # print("User_Name: ", query)
                chat_area.delete(0, tk.END)
                chat_area.insert(tk.END, query)
            except Exception as e:
                print(e)
                ai_speak.speak("Sorry, I couldn't understand. Please try again.")

            message = chat_area.get().strip()
            if message and message != chat_area_placeholder:  # Check if message is not empty and not placeholder
                chat_area.delete(0, tk.END)
                message2 = ''
                for i in range(0, len(message), 40):
                    message2 += message[i:i + 40] + '\n'
                    message2 = ALICE(query=message)

                # Create a Label for user message with padding to the left
                user_message = Label(scrollable_frame, text=message, bg="#cce6ff", fg="black", anchor="w",
                                     wraplength=300, justify="left")
                user_message.grid(sticky="w", padx=1, pady=5)  # Add padding on the left

                # Create a Label for Alice's message
                alice_message = Label(scrollable_frame, text=message2, bg="#b3e0ff", fg="black", anchor="w",
                                      wraplength=300, justify="left")
                alice_message.grid(sticky="w", padx=1, pady=5)  # Add padding on the right

                canvas.update_idletasks()  # Update canvas to reflect changes
                canvas.yview_moveto(1.0)  # Scroll to the bottom

                ai_speak.speak(message2)

    def sending_message(event=None):
        message = chat_area.get().strip()
        if message and message != chat_area_placeholder:  # Check if message is not empty and not placeholder
            chat_area.delete(0, tk.END)
            message2 = ''
            # if message2 == 'quit' or message2 == 'bye':
            #     root.destroy()
            #     return
            for i in range(0, len(message), 40):
                message2 += message[i:i + 40] + '\n'
                message2 = ALICE(query=message)

            # Create a Label for user message with padding to the left
            user_message = Label(scrollable_frame, text=message, bg="#cce6ff", fg="black", anchor="w", wraplength=300,
                                 justify="left")
            user_message.grid(sticky="w", padx=1, pady=5)  # Add padding on the left

            # Create a Label for Alice's message
            alice_message = Label(scrollable_frame, text=message2, bg="#b3e0ff", fg="black", anchor="w", wraplength=300,
                                  justify="left")
            alice_message.grid(sticky="w", padx=1, pady=5)  # Add padding on the right

            canvas.update_idletasks()  # Update canvas to reflect changes
            canvas.yview_moveto(1.0)  # Scroll to the bottom

    root.bind("<Return>", sending_message)
    # root.bind("<space>", voice_input)

    message_frame = Frame(root, bg="#b6d0e2")
    message_frame.grid(row=0, column=0, columnspan=2, padx=8, pady=8, sticky="nsew")

    canvas = Canvas(message_frame, bg="#b6d0e2")
    scrollbar = Scrollbar(message_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="#b6d0e2")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    chat_area = Entry(root, width=50, bg='#6082b6', fg='white', insertbackground='green', font=(18))
    chat_area.insert(0, chat_area_placeholder)
    chat_area.bind("<FocusIn>",
                   lambda event: chat_area.delete(0, tk.END) if chat_area.get() == chat_area_placeholder else None)
    chat_area.bind("<FocusOut>",
                   lambda event: chat_area.insert(0, chat_area_placeholder) if chat_area.get() == '' else None)
    chat_area.grid(row=1, column=0, padx=50, pady=8, sticky="ew")

    send_icon = ImageTk.PhotoImage(Image.open('Images/send_icon.png'))
    voice_icon = ImageTk.PhotoImage(Image.open('Images/voice_icon.png'))

    button = Button(root, bg='#b6d0e2', image=send_icon, command=lambda: sending_message(None), border=0)
    button.grid(row=1, column=1, padx=(0, 5), pady=5, sticky="e")

    button2 = Button(root, bg='#b6d0e2', image=voice_icon, command=voice_input, border=0)
    button2.grid(row=1, column=0, padx=(5, 0), pady=5, sticky="w")

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=0)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=0)

    root.mainloop()


# if __name__ == '__main__':
start_alice()