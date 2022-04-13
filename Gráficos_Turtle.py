from turtle import *
setup(450, 550, 750, -150)
title("Fábrica de Polígonos")
#hideturtle()
#screensize(300, 150)
#goto(100, 0)
#exitonclick()
def poligono(lado,n):
    for i in range(n):
        forward(lado)
        right(360/n)

def poligonos():
    for i in range(3,10):
        poligono(100,i)

def espiral():
    for i in range(10,200,5):
        poligono(i,4)
        right(10)

penup()
goto(-50, 50)
pendown()
espiral()
poligonos()
onkeypress(bye, 'q')
listen()
done()
