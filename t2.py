# from playsound import playsound
# from multiprocessing import Process


# def sound():
#     playsound("C:\\Users\\Acer\\Downloads\\futuristic-beat-146661.mp3")

# if __name__ == "__main__":
#     p = Process(target=sound)
#     p.start()
#     e=input("e=")
#     p.terminate()
    
from pygame import mixer

import time
mixer.init() #Initialzing pyamge mixer

mixer.music.load('C:\\Users\\Acer\\Downloads\\futuristic-beat-146661.mp3') #Loading Music File

mixer.music.play() #Playing Music with Pygame

e=input('e=')

mixer.music.stop()
