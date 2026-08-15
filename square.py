import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Dharani's Beautiful Square Design")

t = turtle.Turtle()
t.pensize(5)
t.color("darkblue")
t.speed(3)

for _ in range(4):
    t.forward(150)
    t.right(90)

t.hideturtle()
screen.mainloop()