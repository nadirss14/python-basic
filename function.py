# -*- coding: utf-8 _*_
import turtle

def main():
    window = turtle.Screen()
    a_turtle = turtle.Turtle()
    make_square(a_turtle)
    turtle.mainloop()

def make_square(a_turtle):
    try:
        pass
        length = int(input('Tamaño del cuadrado: '))
        for i in range(4):
            make_line_and_turn(a_turtle,length)
    except:
        pass   
        print('El tamaño debe se numerico')

def make_line_and_turn(a_turtle,length):
    a_turtle.forward(length)
    a_turtle.left(90)

if __name__ == '__main__':
    main()