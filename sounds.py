import os
import playsound
import time
import winsound

# for playing drink sound
def no():
    winsound.PlaySound(os.path.join("sounds",'filename.wav'),winsound.SND_FILENAME)
def drink():
    winsound.PlaySound(os.path.join("sounds","drikke.mp3"), winsound.SND_FILENAME)
def intro():
    winsound.PlaySound(os.path.join("sounds","intro.wav"), winsound.SND_FILENAME)
def babydragon():
    winsound.PlaySound(os.path.join("sounds", 'dragon.wav'), winsound.SND_FILENAME)
def wolfpack():
    winsound.PlaySound(os.path.join("sounds" ,'WOLF.wav'), winsound.SND_FILENAME)
def petTiger():
    winsound.PlaySound(os.path.join("sounds", 'tiger.wav'), winsound.SND_FILENAME)
def Dragon():
    winsound.PlaySound(os.path.join("sounds", 'dragon.wav'), winsound.SND_FILENAME)
def Gaints():
    winsound.PlaySound(os.path.join("sounds", 'gaints.mp3'), winsound.SND_FILENAME)
def Privatearmy():
    winsound.PlaySound(os.path.join("sounds", 'privatearmy.mp3'), winsound.SND_FILENAME)
def dragger():
    winsound.PlaySound(os.path.join("sounds", 'fil.wav'), winsound.SND_FILENAME)

