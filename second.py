import Tkinter
import swampy
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

def square(t , length):
	for i in range(4):
		fd(t,length)
		lt(t)

square(bob, 100)
wait_for_user()