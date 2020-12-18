from random import randint
import numby as np
import plaque

class plateau(object):
	plat = ' '
	"""docstring for plateau"""
	def __init__(self, plaque1,plaque2,plaque3,plaque4):
		for i in range(randint(0,3)):
			plaque1.switch90()
		for j in range(randint(0,3)):
			plaque2.switch90()
		for t in range(randint(0,3)):
			plaque3.switch90()
		for k in range(randint(0,3)):
			plaque4.switch90()
		
		self.plat = plat
		