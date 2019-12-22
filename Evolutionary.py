import turtle
import math
import random
import time
import matplotlib.pyplot as plt


global best_set
global old_fitness
global best_fit




best_fit = 100000

old_fitness = 10000000000000000
best_set = []
population = []



#Make screen-----------------------------------------------------
wn = turtle.Screen()
wn.tracer(0)
wn.title('Evolutionary Algorithm')


#Make Goal--------------------------------------------------
goal = turtle.Turtle()
goal.color('red')
goal.shape('circle')
goal.up()
goal.goto(0, 300)


#Make dot-----------------------------------------------------

dot = turtle.Turtle()
dot.speed(0)
dot.shape('circle')
dot.shapesize(0.4, 0.4)
dot.up()
dot.goto(0, -300)
wn.update()

#---------------------------------------------------------------

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False


def get_fitness():
	x1 = dot.xcor()
	y1 = dot.ycor()
	x2 = 0
	y2 = 300

	fitness = int(math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))

	return fitness


def do_stuff():
	global best_set, old_fitness, best_fit

	fitness = 1000000000000000000000000
	
	move = 0
	
	move = random.randint(0, 360)
	dot.setheading(move)
	dot.forward(12)
	fitness = get_fitness()
	#print(fitness)
	
	best_fit = old_fitness
	if fitness < old_fitness:
		old_fitness = fitness
		best_set.append(move)
	else:
		#print('ur bad')
		dot.goto(0, -300)
		move = 0
		for p in best_set:
			dot.setheading(p)
			dot.forward(12)
			#time.sleep(0.005)
			wn.update()
	wn.update()

	#print(old_fitness)





plots_x = []
plot_y = []
count = 0
for i in range(2000):
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
#print(best_set)



#mainloop--------------------------------

wn.mainloop()

