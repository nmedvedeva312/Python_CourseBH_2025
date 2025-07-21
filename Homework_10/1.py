'''
Добавить несколько черепах 
    - или сразу 
    * или в течении игры по одной через определенное количество кликов
    - на каждой забиндить клик через одну и туже функцию cath

'''


"""
УПРАВЛЕНИЕ:
Клик - Остановка / запуск черепахи
space - Добавить черепаху
s - Остановить всех
c - Очистить маршруты (оставить черепах)
r - Полный сброс и перезапуск

"""

from turtle import *
from random import randint

ts = []  # список черепах
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'black']
angles = [0, 60, 120, 180, 240, 300]
color_index = 0
angle_index = 0
turtle_count = 0

screen = Screen()
screen.setup(800, 600)
width, height = 800, 600

# границы
xmin = -width // 2 + 10
xmax = width // 2 - 10
ymin = -height // 2 + 10
ymax = height // 2 - 10

# замыкание для клика
def make_catch_and_toggle(t, name):
    moving = True
    click_count = 0

    def catch(x, y):
        nonlocal moving, click_count
        click_count += 1
        t.goto(0, 0)
        t.setheading(randint(0, 360))
        moving = not moving
        t.moving = moving

    return catch

# создать черепаху
def create_turtle():
    global color_index, angle_index, turtle_count
    t = Turtle('turtle')
    t.penup()
    color = colors[color_index % len(colors)]
    t.color(color)
    t.pencolor(color)
    t.speed(0)
    t.goto(randint(xmin + 50, xmax - 50), randint(ymin + 50, ymax - 50))
    t.setheading(angles[angle_index % len(angles)])
    t.pendown()
    t.moving = True
    turtle_count += 1
    name = f"Turtle {turtle_count}"
    t.onclick(make_catch_and_toggle(t, name))
    ts.append(t)
    color_index += 1
    angle_index += 1

# добавление
def add_turtle():
    create_turtle()

# остановка всех
def stop_all():
    for t in ts:
        t.moving = False

# очистка маршрута
def clear_paths():
    for t in ts:
        t.clear()

# сброс всех
def reset_all():
    global ts, color_index, angle_index, turtle_count
    for t in ts:
        t.hideturtle()
    ts = []
    color_index = angle_index = turtle_count = 0
    clearscreen()
    setup_controls()
    for _ in range(3):
        create_turtle()

# отскок от стен
def bounce(t):
    x, y = t.xcor(), t.ycor()
    if not xmin < x < xmax:
        t.setheading(180 - t.heading())
    if not ymin < y < ymax:
        t.setheading(-t.heading())

# движение
def move():
    for t in ts:
        if getattr(t, 'moving', True):
            t.forward(3)
            bounce(t)
    ontimer(move, 30)

# управление
def setup_controls():
    listen()
    onkey(add_turtle, "space")
    onkey(stop_all, "s")
    onkey(clear_paths, "c")
    onkey(reset_all, "r")

# запуск
setup_controls()
for _ in range(3):
    create_turtle()
move()
mainloop()
