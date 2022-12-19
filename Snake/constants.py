import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg

screen_width = 1200
screen_height = 600
size = [screen_width, screen_height]
white = (255, 255, 255)
grey = (50, 50, 50)
forest_green = pg.Color("#086623")
lime_green = pg.Color("#4CBB17")
background_colour = grey
body_colour = forest_green
head_colour = lime_green
framerate = 15
screen = pg.display.set_mode(size)
screen.fill(background_colour)