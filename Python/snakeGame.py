import turtle
import random
import time

delay=0.1
score=0
highestScore=0

bodies=[]

#creating game screen
s=turtle.screen
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600,height=600)

#Creating snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

#Snake Food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()

#Score Board
sb=turtle.Turtle
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.white("Score: 0 | highestScore:0")

 def moveup:
   if head.direction!="down":
   head.direction="up"
  
 def movedown():
  if head.direction!="up":
    head.direction="up"
    
  def moveleft():
    if head.direction!="right":
      head.direction="left"
      
  def moveright():
    if head.direction!="left":
      head.direction="right"
      
#To stop the snake
def movestop():
  head.direction="stop"
  
def move():
  if head.direction=="up"
    y=head.ycor()
    head.sety(y+20)
    
   if head.direction=="down"
      y=head.ycor()
      head.sety(y-20)
      
   if head.direction=="left":
       x=head.xcor()
       head.setx(x-20)
        
   if head.direction=="right":
       x=head.xcor()
       head.setx(x+20)
        
 # Event Handling
s.listen()
s.onkey(moveup,"up")
s.onkey(movedown,"down")
s.onkey(moveleft,"left")
s.onkey(moveright,"right")
s.onkey(movestop,"stop")

#Finalising the main loop
while True:
  s.update()
  if head.rcor()>290:
   head.set x(-290)
  if head.xcor()<-290:
   head.set x(290)
  if head.ycor()>290:
   head.set y(-290)
  if head.ycor()<-290:
   head.set y(290)
   
#Checking Collision with food
if head.distance(food)<20:
 #move food to random position
 x=random.randint(-290,290)
 y=random.randint(-290,290)
 food.goto(x,y)
 
 #increase length of snake
 body=turtle.Turtle()
 body.speed(0)
 body.penup()
 body.shape("square")
 body.color("red")
 body.fillcolor("black")
 bodies.append(body)
 
 score+=10
 #change in delay
 delay-=0.001
 
 #update highscore
 if score>highscore:
  highestScore=score
 sb.clear()
 sb.write("Score:(), highestScore().format(Score,highestScore))
          
#To move snake body
for index in range (len(bodies)-1,0,-1):
          x=bodies[index-1].xcor()
          y=bodies[index-1].ycor()
          bodies[index].goto(x,y)
if len(bodies)>0:
          x=head.xcor()
          y=head.ycor()
          bodies[0].goto(x,y)
move()
          
#Checking collision with snake body
for body in bodies:
          if body.distance(head)<20:
           time.sleep(1)
          head.goto(0,0)
          head.direction="Stop"
          
         #When game stops body should be clear
          for body in bodies:
           body.ht()  #hideturtle
          bodies.clear()
          Score=0
          Delay=0.1
         
         #Update Score Board
          sb.clear()
          sb.write("Score() HighestScore()"format(Score() highestScore())
          time.sleep(delay)
s.mainloop()
  
