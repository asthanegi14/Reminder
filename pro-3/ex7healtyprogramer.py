#reminder
from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def log(msg):
    with open("healthyprogramer.txt","a") as d:
        d.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_workout = time()
    init_study = time()
    init_wakeup = time()
    wakeup = 2
    water = 5
    workout = 10
    study = 15
    while True:
        if time() - init_wakeup > wakeup:
            print("Time to wake up. Enter ok after you wake up to stop alarm.")
            musiconloop("wakeup.mp3", "drank")
            init_wakeup = time()
            log("wake up at == ")
        if time() - init_water > water:
            print("Time to drink water. Enter drank after drink to stop alarm.")
            musiconloop("drinkwater.mp3","drank")
            init_water = time()
            log("drank water at == ")
        if time() - init_workout > workout:
            print("Time to do workout. Enter 'done' after done your exercise to stop alarm.")
            musiconloop("workouttime.mp3","done")
            init_workout = time()
            log("exercise done at == ")
        if time() - init_study > study:
            print("Time to do physical exercise. enter 'done' after done your exercise to stop alarm.")
            musiconloop("physic.mp3","done")
            init_exerphy = time()
            log("study time is == ")