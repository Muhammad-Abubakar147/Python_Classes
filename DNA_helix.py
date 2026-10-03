import turtle
import math

# -------------------------------
# Screen Setup
# -------------------------------
screen = turtle.Screen()
screen.setup(900, 800)
screen.bgcolor("#080b18")
screen.title("Magical DNA Helix 🧬")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.tracer(0, 0)

# -------------------------------
# Settings
# -------------------------------
angle = 0
height = 260
points = 45
radius = 190

colors = [
    "#00FFFF",
    "#7A5CFF",
    "#FF4FD8",
    "#00FF99"
]

# -------------------------------
# Draw a glowing geometric shape
# -------------------------------
def polygon(turtle_obj, x, y, size, sides, color, rotation):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.setheading(rotation)
    turtle_obj.pendown()

    turtle_obj.color(color)
    turtle_obj.fillcolor(color)

    turtle_obj.begin_fill()

    for _ in range(sides):
        turtle_obj.forward(size)
        turtle_obj.left(360 / sides)

    turtle_obj.end_fill()


# -------------------------------
# Draw DNA
# -------------------------------
def draw_dna(rotation):
    t.clear()

    for i in range(points):

        # Vertical position
        y = -height + (i * (height * 2 / (points - 1)))

        # Helix angle
        theta = math.radians(i * 16 + rotation)

        # Two DNA strands
        x1 = math.sin(theta) * radius
        x2 = math.sin(theta + math.pi) * radius

        # Geometric shapes
        color1 = colors[i % len(colors)]
        color2 = colors[(i + 1) % len(colors)]

        polygon(
            t,
            x1,
            y,
            9,
            6,
            color1,
            i * 12 + rotation
        )

        polygon(
            t,
            x2,
            y,
            9,
            6,
            color2,
            -i * 12 - rotation
        )

        # DNA base pair
        t.penup()
        t.goto(x1, y)
        t.pendown()

        t.color("#4DFFFF")
        t.width(2)

        t.goto(x2, y)

    # Center spine effect
    for i in range(points - 1):
        y1 = -height + (i * (height * 2 / (points - 1)))
        y2 = -height + ((i + 1) * (height * 2 / (points - 1)))

        theta1 = math.radians(i * 16 + rotation)
        theta2 = math.radians((i + 1) * 16 + rotation)

        x1 = math.sin(theta1) * radius
        x2 = math.sin(theta2) * radius

        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.color("#2CFFE8")
        t.width(2)
        t.goto(x2, y2)

        theta1 = math.radians(i * 16 + rotation + 180)
        theta2 = math.radians((i + 1) * 16 + rotation + 180)

        x1 = math.sin(theta1) * radius
        x2 = math.sin(theta2) * radius

        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.color("#A66CFF")
        t.goto(x2, y2)


# -------------------------------
# Animation
# -------------------------------
def animate():
    global angle

    draw_dna(angle)

    angle += 4

    turtle.update()

    screen.ontimer(animate, 40)


animate()

screen.mainloop()