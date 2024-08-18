import random
import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
from Gemini import Gemini
from threading import Thread

"""Speaks the given input text."""
speaker = win32com.client.Dispatch("SAPI.SpVoice")


def ai(prompt):
    """Takes Gemini API, processes it and gives response."""
    text = f"Gemini Response for Prompt: {prompt} \n********************\n"
    response = None

    try:
        gemini = Gemini()
        response = gemini.question(prompt)
        text += response
    except Exception as e:
        print("An Error occurred while processing the Prompt.")

    if not os.path.exists("Gemini Prompts"):
        os.mkdir("Gemini Prompts")

    # Folder/prompts/Gemini response
    with open(f"Gemini Prompts/prompt - {random.randint(1, 12384756)}", "w") as f:
        f.write(text)

    return response


def search_on_chrome(que_ry):
    """constructs url, opens chrome and searches for it."""
    search_url = f"https://www.google.com/search?q={que_ry}"
    webbrowser.open(search_url)


chatStr = ""


def chat(que_ry):
    """Initiates chat with user and stores it in variable chatStr"""
    global chatStr
    chatStr += f"User: {que_ry}\n "
    response1 = None

    try:
        gemini = Gemini()
        response1 = gemini.question(que_ry)
        chatStr += response1
    except Exception as e:
        print("An Error occurred while processing the Prompt.")

    chatStr += f"Cleo: {response1}\n\n"
    speaker.Speak(response1)


def take_command():
    """Takes in voice, processes it and gives a response """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8  # This is the default pause threshold
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Cleo."


if __name__ == "__main__":
    print("Welcome to Cleo AI")

    program_is_on = True

    while program_is_on:

        print("Listening...")
        text = take_command()

        """Searching sites using a loop"""
        sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
                 ["wikipedia", "https://www.wikipedia.com"], ["gmail", "https://www.gmail.com"],
                 ["amazon", "https://www.amazon.com"], ["flipkart", "https://www.flipkart.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
                print(f"Opening {site[0]} Sir.")
                speaker.Speak(f"Opening {site[0]} Sir.")
                # webbrowser.open(f"https://{site[0]}.com")
                webbrowser.open(f"{site[1]}")

        if "Shut".lower() in text.lower():
            print("Shutting down the program.")
            program_is_on = False
            speaker.Speak("Shutting down the program......Do come back again.")

        elif "the time".lower() in text.lower():
            """Tell date and time"""
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speaker.Speak(f"Sir, The Time is: {strfTime}")

        # Opening apps
        elif "open music".lower() in text.lower():
            """Open music directory"""
            os.startfile(r"C:\Users\dhing\Music")
        elif "open edge".lower() in text.lower():
            location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            speaker.Speak("Opening Edge Browser...")
            os.startfile(location)
        elif "open chrome".lower() in text.lower():
            chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            speaker.Speak("Opening Chrome Browser...")
            os.startfile(chrome)
        elif "open firefox".lower() in text.lower():
            firefox = r"C:\Program Files\Mozilla Firefox\firefox.exe"
            speaker.Speak("Opening Firefox Browser...")
            os.startfile(firefox)
        elif "open vscode".lower() in text.lower():
            vscode = r"C:\Users\dhing\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            speaker.Speak("Opening VSCode...")
            os.startfile(vscode)
        elif "open word".lower() in text.lower():
            word = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            speaker.Speak("Opening Word...")
            os.startfile(word)
        elif "open excel".lower() in text.lower():
            excel = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
            speaker.Speak("Opening Excel...")
            os.startfile(excel)
        elif "open powerpoint".lower() in text.lower():
            powerpoint = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
            speaker.Speak("Opening Powerpoint...")
            os.startfile(powerpoint)
        elif "open outlook".lower() in text.lower():
            outlook = r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"
            speaker.Speak("Opening Outlook...")
            os.startfile(outlook)
        elif "open pycharm".lower() in text.lower():
            pycharm = r"C:\Program Files\JetBrains\PyCharm Community Edition 2023.3.2\bin\pycharm64.exe"
            speaker.Speak("Opening PyCharm...")
            os.startfile(pycharm)
        elif "open vlc".lower() in text.lower():
            vlc = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
            speaker.Speak("Opening VLC...")
            os.startfile(vlc)
        elif "open store".lower() in text.lower():
            store = r"C:\Program Files (x86)\Windows Store\app"
            speaker.Speak("Opening Windows Store...")
            os.startfile(store)
        elif "open file explorer".lower() in text.lower():
            explorer = r"C:\Windows\explorer.exe"
            speaker.Speak("Opening File Explorer...")
            os.startfile(explorer)
        elif "open command prompt".lower() in text.lower():
            cmd = r"C:\Windows\System32\cmd.exe"
            speaker.Speak("Opening Command Prompt...")
            os.startfile(cmd)
        elif "open terminal".lower() in text.lower():
            terminal = r"C:\Windows\System32\cmd.exe"
            speaker.Speak("Opening Terminal...")
            os.startfile(terminal)
        elif "open notepad".lower() in text.lower():
            notepad = r"C:\Windows\System32\notepad.exe"
            speaker.Speak("Opening Notepad...")
            os.startfile(notepad)
        elif "open calculator".lower() in text.lower():
            calculator = r"C:\Windows\System32\calc.exe"
            speaker.Speak("Opening Calculator...")
            os.startfile(calculator)
        elif "open task manager".lower() in text.lower():
            task_manager = r"C:\Windows\System32\taskmgr.exe"
            speaker.Speak("Opening Task Manager...")
            os.startfile(task_manager)
        elif "open control panel".lower() in text.lower():
            control_panel = r"C:\Windows\System32\control.exe"
            speaker.Speak("Opening Control Panel...")
            os.startfile(control_panel)

        elif "reset".lower() in text.lower():
            """Deletes the AI based conversation in prompts section"""
            for file in os.listdir(r"C:\Users\dhing\Coding Playground\python\PycharmProjects\Jarvis_2\Gemini Prompts"):
                os.remove(rf"C:\Users\dhing\Coding Playground\python\PycharmProjects\Jarvis_2\Gemini Prompts\{file}")
            chatStr = ""    
            speaker.Speak("Reset Successful.")
        elif "search on internet".lower() in text.lower():
            """Searches on Google"""
            query = text.replace("search on net", "")
            search_on_chrome(query)

        elif "Using Artificial Intelligence".lower() in text.lower():
            print("Thinking....")
            answer = ai(text)
            speaker.Speak(answer)
        else:
            chat(text)
            print(chatStr)
