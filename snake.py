from turtle import Turtle
starting_positions = [(0,0),(-20,0),(-40,0)]
UP =90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self):
        self.segaments = []
        self.creat_snake()
        self.head = self.segaments[0]

    def creat_snake(self):
        for positions in starting_positions:
            sam = Turtle(shape="square")
            sam.color("white")
            sam.penup()
            sam.goto(positions)
            self.segaments.append(sam)


    def move(self):
        for seg_num in range(len(self.segaments) -1 ,0,-1):
            new_x = self.segaments[seg_num - 1].xcor()
            new_y = self.segaments[seg_num - 1].ycor()
            self.segaments[seg_num].goto(new_x,new_y)
        self.head.forward(20)

    def up (self):
        if self.head.heading() != DOWN:
          self.head.setheading(UP)
    def down (self):
         if self.head.heading() != UP:
          self.head.setheading(DOWN)
    def right (self):
        if self.head.heading() != LEFT:
          self.head.setheading(RIGHT)
    def left (self):
        if self.head.heading() != RIGHT:
          self.head.setheading(LEFT)