import turtle

# Discord: Wasp #1000
# Discord: https://discord.gg/KD2cSKpyWU
# Instagram: @ege.pekkolay
# Github: github.com/waspdev


t = turtle.Turtle()

turtle.bgcolor("black")
t.color("orange")

def rect():
    t.pensize(9)
    t.forward(170)
    t.left(45)
    t.forward(6)
    t.left(45)
    t.forward(170)
    t.left(45)
    t.forward(6)
    t.left(45)
    t.forward(330)
    t.left(45)
    t.forward(6)
    t.left(45)
    t.forward(170)
    t.left(45)
    t.forward(6)
    t.left(45)
    t.forward(170)

def four_corner_lines():
    t.pensize(12)
    t.penup()
    t.forward(180)
    t.left(90)
    t.forward(35)
    t.left(90)
    t.pendown()
    t.forward(12)
    t.penup()
    t.forward(344)
    t.pendown()
    t.forward(17)
    t.penup()
    t.right(90)
    t.forward(105)
    t.right(90)
    t.pendown()
    t.forward(17)
    t.penup()
    t.forward(344)
    t.pendown()
    t.forward(12)

def p():
    t.penup()
    t.left(180)
    t.forward(280)
    t.pendown()
    t.forward(40)
    t.left(90)
    t.forward(100)
    t.left(180)
    t.forward(52)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(47)

def u():
    t.penup()
    t.right(90)
    t.forward(32)
    t.right(90)
    t.pendown()
    t.forward(98)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(98)

def b():
    t.penup()
    t.right(90)
    t.forward(35)
    t.pendown()
    t.forward(45)
    t.right(90)
    t.forward(43)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(40)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(40)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(40)
    t.right(90)
    t.forward(45)
    t.right(90)
    t.forward(96)

def g():
    t.penup()
    t.right(180)
    t.forward(53)
    t.left(90)
    t.forward(98)
    t.pendown()
    t.forward(25)
    t.right(90)
    t.forward(45)
    t.right(90)
    t.forward(45)
    t.right(90)
    t.forward(95)
    t.right(90)
    t.forward(40)

rect()
four_corner_lines()
p()
u()
b()
g()

turtle.done()

# Discord: Wasp #1000
# Discord: https://discord.gg/KD2cSKpyWU
# Instagram: @ege.pekkolay
# Github: github.com/waspdev