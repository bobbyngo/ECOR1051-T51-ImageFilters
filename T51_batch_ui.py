#Written by Alexander Szabo, 101151844, Group 51
# Milestone 3
# Submittion date April 2, 2020

from T51_image_filters import *

def batch_ui(filename: str) -> Image:
    infile = open(filename, 'r')
    for line in infile:
        commands = line.split()
        new_image = load_image(commands[0])
        for i in range(2, len(commands)):
            if commands[i] == '2':
                new_image = two_tone(new_image, "yellow", "cyan")
            elif commands[i] == 'X':
                new_image = extreme_contrast(new_image)
            elif commands[i] == 'P':
                new_image = posterize(new_image)
            elif commands[i] == 'V':
                new_image = vertical(new_image)
            elif commands[i] == 'H':
                new_image = horizontal(new_image)
            elif commands[i] == 'R':
                new_image = red_channel(new_image)
                red_image = new_image
            elif commands[i] == 'G':
                new_image = green_channel(new_image)
                green_image = new_image
            elif commands[i] == 'B':
                new_image = blue_channel(new_image)
                blue_image = new_image
            elif commands[i] == 'C':
                combined_image = combine(red_image, green_image, blue_image)
            elif commands[i] == '3':
                new_image = three_tone(new_image, "yellow", "magenta", "cyan")
            elif commands[i] == 'S':
                new_image = sepia(new_image)
            elif commands[i] == 'D':
                new_image = detect_edges(new_image, 10)
            elif commands[i] == 'DB':
                new_image = detect_edges_better(new_image, 10)
            
        save_as(new_image, commands[1])
        
    return None

print("Please enter a text file for image filtering")
batch_ui(input())
