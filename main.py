import pygame
import requests
from pynput.keyboard import Key, Controller

IP = ""
PORT = ""

keyboard = Controller()
pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init() 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 1:
                    requests.get(f"http://{IP}:{PORT}/koreader/event/GotoViewRel/-1")
                elif event.button == 2:
                    requests.get(f"http://{IP}:{PORT}/koreader/event/GotoViewRel/1")
else:
    print("No joystick connected.")
