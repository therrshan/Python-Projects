from constants import *
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
import random


class Snake(object):

	def __init__(self, fruit):

		self.unit = 10
		self.reset(fruit)
		self.body_colour = body_colour
		self.head_colour = head_colour


	def update_position(self):

		self.event_handler()
		self.spawn()


	def event_handler(self):

		for event in pg.event.get():

			if (event.type == pg.QUIT):

				pg.quit()
				quit()

			if (event.type == pg.KEYDOWN):
				
				if (event.key == pg.K_UP):
					
					self.x_velocity = 0
					self.y_velocity = -self.unit
					
				elif (event.key == pg.K_DOWN):
					
					self.x_velocity = 0
					self.y_velocity = self.unit
					
				elif (event.key == pg.K_LEFT):
					
					self.y_velocity = 0
					self.x_velocity = -self.unit
					
				elif (event.key == pg.K_RIGHT):
					
					self.y_velocity = 0
					self.x_velocity = self.unit


	def create(self):

		counter = 0
		depth = len(self.position)

		for location in self.position:

			if (counter == depth - 1): colour = self.head_colour
			else: colour = self.body_colour
			square = [location[0], location[1], self.unit, self.unit]
			pg.draw.rect(screen, colour, square)
			counter += 1


	def erase(self):

		for location in self.position:

			square = [location[0], location[1], self.unit, self.unit]
			pg.draw.rect(screen, background_colour, square)
	

	def spawn(self):

		self.erase()
		self.x_position = (self.x_position + self.x_velocity)%screen_width
		self.y_position = (self.y_position + self.y_velocity)%screen_height
		location = (self.x_position, self.y_position)
		self.position.append(location)
		self.position.pop(0)
		self.create()


	def check_body_collision(self, fruit):

		body = self.position[:-1]
		head = self.position[-1]
		for point in body: self.reset(fruit) if (point == head) else None


	def eat(self, fruit):

		head = self.position[-1]
		x = abs(head[0] - fruit.x_position)
		y = abs(head[1] - fruit.y_position)

		if ((x < self.unit) & (y < self.unit)):

			location = (self.x_position, self.y_position)
			self.position.insert(0, location)
			self.length = len(self.position)
			fruit.spawn()
			if (self.length == 15): self.speed += 2
			elif (self.length == 25): self.speed += 2
			elif (self.length == 35): self.speed += 2
			elif (self.length == 45): self.speed += 2
			elif (self.length == 55): self.speed += 2


	def reset(self, fruit):

		screen.fill(background_colour)
		self.speed = framerate
		self.x_position = random.randrange(0, screen_width - self.unit, self.unit)
		self.y_position = random.randrange(0, screen_height - self.unit, self.unit)
		direction = random.choice(["up", "down", "left", "right"])

		if (direction == "up"):
			
			self.x_velocity = 0
			self.y_velocity = -self.unit
			head = (self.x_position, self.y_position)
			body = (self.x_position, self.y_position + self.unit)
			tail = (self.x_position, self.y_position + 2*self.unit)
			
		elif (direction == "down"):
			
			self.x_velocity = 0
			self.y_velocity = self.unit
			head = (self.x_position, self.y_position)
			body = (self.x_position, self.y_position - self.unit)
			tail = (self.x_position, self.y_position - 2*self.unit)
			
		elif (direction == "left"):
			
			self.y_velocity = 0
			self.x_velocity = -self.unit
			head = (self.x_position, self.y_position)
			body = (self.x_position + self.unit, self.y_position)
			tail = (self.x_position + 2*self.unit, self.y_position)
			
		elif (direction == "right"):
			
			self.y_velocity = 0
			self.x_velocity = self.unit
			head = (self.x_position, self.y_position)
			body = (self.x_position - self.unit, self.y_position)
			tail = (self.x_position - 2*self.unit, self.y_position)

		self.position = [tail, body, head]
		self.length = len(self.position)
		fruit.spawn()