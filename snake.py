from turtle import Turtle

START_POS=[(0,0),(-20,0),(-40,0)]
MOV_DIST=15
UP=90
RIGHT=0
LEFT=180
DOWN=270
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)

    def add_segment(self, position):
        a = Turtle("square")
        a.color("white")
        a.penup()
        a.goto(position)
        self.segments.append(a)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOV_DIST)

    def up(self):
        if self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading()!=UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading()!=RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading()!=LEFT:
            self.segments[0].setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()






