



class World:
	def __init__(self):
		self.Height = 20
		self.Width = 20
		self.Barr = []

	def say_init(self):
		print("World is ready!")

	def tell_barr(self):
		print(self.Barr)
	
	def add_barr(self,posx,posy):
		self.Barr.append((posx,posy))


class Snake:
	def __init__(self,world):
		self.length = 1
		self.posx = 0
		self.posy = 0
		self.canMove = [ 0, 1, 1, 0 ]

	def check_canMove(self,world):
		

	def AI_move(self,world):
		if self.posx < 19:
			self.posx = self.posx + 1
	
	def say_pos(self):
		print(self.posx,"  ",self.posy)




wo = World()
wo.say_init()
wo.add_barr(3,3)

sn = Snake(wo)
sn.AI_move(wo)
sn.AI_move(wo)
sn.say_pos()


wo.tell_barr()



