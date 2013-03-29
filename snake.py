pos = [ (0,1,0), (1,0,1), (0,-1,2), (-1,0,3) ]



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
		if self.Barr:
			for i in self.Barr:
				if (posx,posy) != i:
					self.Barr.append((posx,posy))
		else:
			self.Barr.append((posx,posy))


class Snake:
	def __init__(self,world):
		self.length = 1
		self.posx = 0
		self.posy = 0
		self.canMove = [ 0, 0, 0, 0 ]
		self.check_canMove()
		world.add_barr(self.posx,self.posy)

	def check_canMove(self):
		for i in pos:
			if self.posx+i[0]>=0 and self.posx+i[0]<=19 and self.posy+i[1]>=0 and self.posy+i[1]<=19:
				self.canMove[i[2]] = 1
			else:
				self.canMove[i[2]] = 0
	
	def say_canmove(self):
		print(self.canMove)

	def AI_move(self,world):
		if self.posx < 19:
			self.posx = self.posx + 1
	
	def say_pos(self):
		print(self.posx,"  ",self.posy)




wo = World()
wo.say_init()
wo.add_barr(3,3)
wo.add_barr(3,3)

sn = Snake(wo)

sn.say_pos()


wo.tell_barr()
sn.check_canMove()
sn.say_canmove()


