import turtle

# def square():
#     for i in range(4):
#         turtle.forward(50)
#         turtle.left(90)
        
# square()


# def square(length):
#     for i in range(4):
#         turtle.forward(length)
#         turtle.left(90)
        
# square(30)
# square(60)


def polygon(n, length):
    angle = 360 / n
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)
        
polygon(7, 30)