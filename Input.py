import pygame
from pygame.locals import *

class Input():
    def __init__(self):
        self.keys = None
        self.mouseButtons = None
        self.mousePosition = None
    def update(self):
        self.keys = pygame.key.get_pressed()
        self.mouseButtons = pygame.mouse.get_pressed()
        self.mousePosition = pygame.mouse.get_pos()
    def getKeys(self):
        return self.keys
    def getMouseButtons(self):
        return mouseButtons
    def getMousePosition(self):
        return mousePosition
