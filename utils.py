from random import randint

pixels = [[0,0],[0,0]]

last_pos = {}

def add(position = 0):
    length = 0
    for n in pixels:
        last_pos[length] = [0,0]
        length+=1

def show(position = (0,0)):
    return {}

def new_apple(screen = [0,0]):
    position = (round(randint(0,screen[0]) / 20) * 20,round(randint(0,screen[1]) / 20) * 20)
    return position

print(new_apple())
