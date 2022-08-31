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
  
