# Written by Ahmed Moussa, 101142994, Group 51 
# Milestone 3
# Submittion date April 2, 2020

from Cimpl import *
from time import sleep

def image_load():
    print("Select an Image to Load:")
    try:
        return load_image(choose_file())
    except:
        print("Failed to Load Image!")
        sleep(2)
        return False


def image_save(image):
    save_as(image)
    return True


def quit_program():
    print("Any existing changes are not saved automatically.\nAre you sure you would like to quit? (Y/N)")
    while True:
        quitInput = input().upper()
        if quitInput == "Y" or quitInput == "YES":
            return True
        elif quitInput == "N" or quitInput == "NO":
            return False


