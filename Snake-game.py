import turtle
import time
import random
#set up the screen
wn=turtle.Screen()
wn.title("Snake_Game")
wn.bgcolor("yellow")
wn.setup(width=600,height=600)
wn.tracer(0)
delay=0.1

score=0
high_score=0

#make the snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="right"

#make food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
segment=[]

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("Score:0 High Score:0",align="center",font=("Courier",24,"normal"))


#define functions
def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
wn.listen()
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_up,"Up")

while True:
    wn.update()
    if head.ycor()>290 or head.ycor()<-290 or head.xcor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for s in segment:
            s.goto(1000,1000)
        segment.clear()

        score=0
        delay=0.1
        pen.clear()
        pen.write("Score:{} High-Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
        
    if head.distance(food)<20:
        y=random.randint(-290,290)
        x=random.randint(-290,290)
        food.goto(x,y)
    #Add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segment.append(new_segment)
        
        #Shorten the delay
        delay-=0.001
        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score:{} High-Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    
    #MOve the segments first in reverse order
    for i in range(len(segment)-1,0,-1):
        x=segment[i-1].xcor()
        y=segment[i-1].ycor()
        segment[i].goto(x,y)
    #Move segment 0 to where the head is
    if len(segment)>0:
        x=head.xcor()
        y=head.ycor()
        segment[0].goto(x,y)
        
    move()
    
    for s in segment:
        if s.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for s in segment:
                s.goto(1000,1000)
            segment.clear()

            score=0
            delay=0.1
            pen.clear()
            pen.write("Score:{} High-Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
        
        
            
    time.sleep(delay)

wn.mainloop()