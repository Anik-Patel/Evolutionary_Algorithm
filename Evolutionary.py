import turtle
import math
import random
import time
import matplotlib.pyplot as plt
import cv2
import keyboard



global best_set
global old_fitness
global best_fit




best_fit = 100000

old_fitness = 10000000000000000
best_set = []
population = []
obstacles = []


placement = []
goal_pos = []


wn = turtle.Screen()

wn.tracer(0)
wn.title('Evolutionary Algorithm')

goal = turtle.Turtle()
goal.color('red')
goal.shape('circle')
goal.up()
wn.update()


canvas = wn.getcanvas()



draw = turtle.Turtle()
draw.color('blue')
draw.shape('circle')
draw.up()




while True:
	if keyboard.is_pressed('a'):
		x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
		
		placement.append([x-700, (y*-1)+500])
		draw.goto(x-700, (y*-1)+500)
		draw.stamp()
		wn.update()
		time.sleep(0.1)

	if keyboard.is_pressed('g'):
		x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
		
		
		goal.goto(x-700, (y*-1)+500)
		
		wn.update()
		time.sleep(0.1)
		
	if keyboard.is_pressed('q'):
		break


draw.clear()





for i in range(len(placement)):
	obstacles.append(turtle.Turtle())

lolol = 0
for bad in obstacles:
	bad.color('blue')
	bad.shape('circle')
	bad.up()
	bad.goto(placement[lolol])
	lolol += 1




dot = turtle.Turtle()
dot.speed(0)
dot.shape('circle')
dot.shapesize(0.4, 0.4)
dot.up()
dot.goto(0, -300)
wn.update()



def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False


def get_fitness():
	x1 = dot.xcor()
	y1 = dot.ycor()
	x2 = goal.xcor()
	y2 = goal.ycor()

	fitness = int(math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))
	for bad in obstacles:
		if isCollision(dot, bad):
			fitness += 100000
			
	return fitness


global fitness_list
fitness_list = []
def do_stuff():
	global best_set, old_fitness, best_fit, fitness_list

	fitness = 1000000000000000000000000
	
	move = 0
	
	move = random.randint(0, 360)
	dot.setheading(move)
	dot.forward(12)
	fitness = get_fitness()
	
	
	best_fit = old_fitness
	if fitness < old_fitness:
		old_fitness = fitness
		best_set.append(move)
	else:
		
		dot.goto(0, -300)
		move = 0
		for p in best_set:
			dot.setheading(p)
			dot.forward(12)
			
	wn.update()
	fitness_list.append(old_fitness)

	if generation % 50 == 0:
		#print(fitness_list)
		nTemp = fitness_list[0]
		bEqual = True
		 
		for item in fitness_list:
		  if nTemp != item:
		    bEqual = False
		    
		if bEqual:
			try:
				best_set.pop(len(best_set)-1)
				
			except:
				pass

		fitness_list = []
		dot.goto(0, -300)
		for p in best_set:
			dot.setheading(p)
			dot.forward(12)

		old_fitness = get_fitness()


	





plots_x = []
plot_y = []
generation = 0
count = 0
for i in range(1000000000):
	generation = count
	gen = "Evolutionary Algorithm  Generation: "+str(count)+"  "+"best fit: "+str(best_fit)
	wn.title(gen)
	do_stuff()
	plots_x.append(count)
	plot_y.append(best_fit)
	

	if isCollision(dot, goal):
		print('done')
		best_fit = 0
		gen = "Evolutionary Algorithm  Generation: "+str(count)+"  "+"best fit: "+str(best_fit)
		wn.title(gen)
		break
	count += 1


time.sleep(2)
dot.goto(0, -300)
wn.update()
print('the route is')
time.sleep(2)


plot_y.pop(0)
plots_x.pop(0)

dot.pendown()

for moves in best_set:
	dot.setheading(moves)
	dot.forward(12)
	

dot.up()

dot.goto(0, -300)

for moves in best_set:
	dot.setheading(moves)
	dot.forward(12)
	wn.update()
	time.sleep(0.05)


plt.xlabel('generation')
plt.ylabel('fitness')
plt.plot(plots_x, plot_y)
plt.show()


wn.mainloop()

