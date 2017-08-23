import Tkinter
import swampy
from swampy.TurtleWorld import * 
world = TurtleWorld()
bob = Turtle()
print bob

for i in range(4):
	fd(bob , 100)
	lt(bob)

wait_for_user()

def square(t):
	for i in range(4):
		fd(t, 100)
		lt(t)

square(bob)