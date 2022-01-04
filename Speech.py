# ------------------------------------------------------------------------------------------------------------------
# ---Text to Speech program---
#
# Author: Sadhbh
# Date: october 2021
# Description: program to covert text into speech
#              options to change speaking rate, volume and gender
#              options to change languages
#              display voices on device
#              save text to speech as mp3 files
#
# references:
# https://www.geeksforgeeks.org/text-to-speech-changing-voice-in-python/
# https://betterprogramming.pub/an-introduction-to-pyttsx3-a-text-to-speech-converter-for-python-4a7e1ce825c3
# https://pyttsx3.readthedocs.io/en/latest/engine.html#pyttsx3.voice.Voice
#
# Updates:
# 1) it'll keep prompting the user dor more text to speech input until it's exited as opposed to entering option
# one each time
# ------------------------------------------------------------------------------------------------------------------

import collections
import pyttsx3
# from pyttsx3 import Engine


class VoiceEngine:

    voices: collections 

    def __init__(self, rate, vol, voice):
        # Initialize the converter
        self.engine = pyttsx3.init()  # object creation
        self.voices: collections = self.engine.getProperty('voices')
        self.rate = rate
        self.volume = vol
        self.voice = voice

    def voice_info(self):
        # to get the info about various voices in our PC
        for self.voice in self.voices:
            self.voices = self.engine.getProperty("voices")
            print("Voice:")
            print("ID: %s" % self.voice.id)
            print("Name: %s" % self.voice.name)
            print("Age: %s" % self.voice.age)
            print("Gender: %s" % self.voice.gender)
            print("Languages Known: %s" % self.voice.languages)
            print("\n")
        return

    def speech(self):
        text = '1'
        print("press '0' (zero) to exit\n")
        while text != '0':
            text = input("Enter text to be spoken: ")
            self.engine.say(text)
            self.engine.runAndWait()
            self.engine.stop()
        else:
            return

    def language(self):
        print(f"current language set to: English\n")
        print("\n"
              "            ---- Language Menu ----\n"
              "            1.English\n"
              "            2.French\n"
              "            3.Korean\n"
              "            4.Return to Main Menu\n"
              "            ")
        option: int = int(input("Choose a language option: "))
        if 0 > option > 4:
            print("Excuse me, was that an option?")
        elif option == 4:
            return
        elif option == 1:
            self.engine.setProperty('voice', self.voices[1].id)
            print(f"current language set to: English\n")
        elif option == 2:
            self.engine.setProperty('voice', self.voices[2].id)
            print(f"current language set to: French\n")
        elif option == 3:
            self.engine.setProperty('voice', self.voices[3].id)
            print(f"current language set to: Korean\n")
        else:
            print("bro,make up your mind")
            print(option)

        return

    def speaking_rate(self):
        # getting details of current speaking rate
        rate = self.engine.getProperty('rate')
        # printing current voice rate
        # self.engine.say('My current speaking rate is ' + str(rate))
        print(rate)
        choice: int = int(input("Would you like to change the voice rate?: \n1 = yes\n2 = no\n"))
        if choice != 1:
            print("Sure no problem")
        else:
            rate: int = int(input("What would you like the new voice rate to be?: "))
            self.engine.setProperty('rate', rate)  # setting up new voice rate
            print(f'print rate is: {rate}')
        return

    def volume_funct(self):
        # getting to know current volume level (min=0 and max=1)
        volume: int = self.engine.getProperty('volume')
        # printing current volume level
        print(volume)
        choice: int = int(input("Would you like to change the volume?: \n1 = yes\n2 = no\n"))
        if choice != 1:
            print("Sure no problem")
        else:
            volume: float = float(input("What would you like the new volume to be?: "))
            # setting up volume level  between 0 and 1
            self.engine.setProperty('volume', volume)
            print(f'print rate is: {volume}')
        return

    def gender(self):
        gender: int = self.engine.getProperty('voice')
        print(gender)
        choice: int = int(input("Would you like to change the gender?: \n1 = yes\n2 = no\n"))
        if choice != 1:
            print("Sure no problem")
        else:
            gender: int = int(input("Which gender do you want the voice to sound like?: \n1) Female\n2) Male\n"))
            # changing index changes voices. 1 for female. 0 for male
            for self.voice in self.voices:
                if gender == 2:
                    self.engine.setProperty('voice', self.voices[0].id)
                else:
                    self.engine.setProperty('voice', self.voices[1].id)
        print(f'print gender is: {gender}')
        return

    def save_voice(self):
        # Saving Voice to a file
        save_text = input("Input text to be saved: \n")
        file_name: str = input("What would you like to save yer file as? ")
        self.engine.save_to_file(save_text, file_name)
        self.engine.runAndWait()
        return


def main():
    voice_engine = VoiceEngine(rate=200, vol=1, voice=1)

    while True:
        print("\n"
              "            ---- Main Menu ----\n"
              "            1.Text to Speech\n"
              "            2.Set Voice properties\n"
              "            3.language option\n"
              "            4.Voice Info\n"
              "            5.Save to file\n"
              "            6.exit\n"
              "            ")
        selection: int = int(input("Please Select:"))
        if selection == 1:
            print("Text to speech")
            voice_engine.speech()
        elif selection == 2:
            print("Set Voice properties")
            voice_properties(voice_engine)
        elif selection == 3:
            print("Language")
            voice_engine.language()
        elif selection == 4:
            print("Voice Info")
            voice_engine.voice_info()
        elif selection == 5:
            print("Save voice to file")
            voice_engine.save_voice()
        elif selection == 6:
            print("Exit")
            break
        else:
            print("Unknown Option Selected!")


def voice_properties(voice_engine):
    print("\n"
          "            ---- voice properties Menu ----\n"
          "            1.Speaking rate\n"
          "            2.Volume\n"
          "            3.Gender\n"
          "            4.Return to Main Menu\n"
          "            ")
    selection: int = int(input("Please Select:"))
    if selection == 1:
        print("Speaking rate")
        voice_engine.speaking_rate()
    elif selection == 2:
        print("Volume")
        voice_engine.volume_funct()
    elif selection == 3:
        print("Gender")
        voice_engine.gender()
    else:
        return


def key_words():
    pass 

if __name__ == "__main__":
    main()


