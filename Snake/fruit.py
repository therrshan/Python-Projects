from constants import *
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
import random


class Fruit(object):

	create = lambda self: pg.draw.rect(screen, self.colour, [self.position[0], self.position[1], self.unit, self.unit])
	erase = lambda self: pg.draw.rect(screen, background_colour, [self.x_position, self.y_position, self.unit, self.unit])

	def __init__(self):

		self.colour = white
		self.unit = 10
		self.x_position = 0
		self.y_position = 0
		location = (self.x_position, self.y_position)
		self.position = location


	def update_position(self, snake):

		while (self.position in snake): 

			self.x_position = random.randrange(0, screen_width - self.unit, self.unit)
			self.y_position = random.randrange(0, screen_height - self.unit, self.unit)
			self.position = (self.x_position, self.y_position)


	def spawn(self):

		self.erase()
		self.update_position(self.position)
		self.create()