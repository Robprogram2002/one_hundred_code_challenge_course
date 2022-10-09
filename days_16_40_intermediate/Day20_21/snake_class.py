from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_GRADE = 90
LEFT_GRADE = 180
RIGHT_GRADE = 0
DOWN_GRADE = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN_GRADE:
            self.head.setheading(90)

    def move_left(self):
        if self.head.heading() != RIGHT_GRADE:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != LEFT_GRADE:
            self.head.setheading(0)

    def move_down(self):
        if self.head.heading() != UP_GRADE:
            self.head.setheading(270)
