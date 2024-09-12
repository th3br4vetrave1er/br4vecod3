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


# def polygon(n, length):
#     angle = 360 / n
#     for i in range(n):
#         turtle.forward(length)
#         turtle.left(angle)
        
# polygon(n=17, length=120)


# def circle(radius):
#     circumference = 2 * 3.14 * radius
#     n = 30
#     length = circumference / n
#     polygon(n, length)
    
# circle(30)


def polyline(n, length, angle):
    """
    Draws line segments with the given length and angle between them.
    n: integer number of line segments
    length: length of the line segments
    angle: angle between segments (in degrees)
    """ 
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)
        
def polygon(n, length):
    angle = 360.0 / n
    polyline(n, length, angle)
    
def arc(radius, angle):
    arc_length = 2 * 3.14 * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)
    
def circle(radius):
    arc(radius, 360)
    
polygon(n=20, length=9)
arc(radius=70, angle=70)
circle(radius=10)