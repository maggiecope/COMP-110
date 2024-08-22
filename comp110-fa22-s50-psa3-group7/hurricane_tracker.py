"""
Module: hurricane_tracker

Program to visualize the path of a Hurrican in the North Atlantic Basin.

Authors:
1) Sophia Zaboukos - szaboukos@sandiego.edu
2) Maggie Cope - mcope@sandiego.edu
"""
from tkinter import W
import turtle


def screen_setup():
    """
    Creates the Turtle and the Screen with the map background
    and coordinate system set to match latitude and longitude.

    Returns:
    A list containing the turtle, the screen, and the background image.

    DO NOT MODIFY THIS FUNCTION IN ANY WAY!!!
    """

    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Tracker")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()

    # set the coordinate system to match lat/long
    turtle.setworldcoordinates(-90, 0, -17.66, 45)

    map_bg_img = tkinter.PhotoImage(file="atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("hurricane.gif")
    t.shape("hurricane.gif")

    return [t, wn, map_bg_img]


# Define the get_category function here
def get_category(wind_speed) :
    """
    Returns the hurricane category (integer) based on the given wind speed 
    """

    cg = 0
    if 74 <= int(wind_speed) <= 95 :
        cg = 1
    elif 96 <= int(wind_speed) <= 110 :
        cg = 2
    elif 111 <= int(wind_speed) <= 129 :
        cg = 3
    elif 130 <= int(wind_speed) <= 156 :
        cg = 4
    elif int(wind_speed) > 156 :
        cg = 5
    return cg

def animate(csv_filename):
    """
    Animates the path of a hurricane.

    Parameters:
    csv_filename (string): Name of file containing hurricane data (CSV format).
    """

    # screen_setup returns a list of three items: the turtle to draw with, the
    # screen object for the window, and the background image of the window.
    # We only care about the turtle though.
    setup_data = screen_setup()

    # Give a name to the turtle that we were given back.
    hurricane_turtle = setup_data[0]


    # Your code to perform the animation will go after this line.
    f = open(csv_filename,'r')
    hurricane_turtle.hideturtle()
    hurricane_turtle.penup()
    
    for line in f:
   
        vals = line.split(",")
        long = float(vals[3])
        lat = float(vals[2])
        ws = float(vals[4])
        wind = get_category(ws)
        if wind == 1 :
            hurricane_turtle.color("blue")
            hurricane_turtle.pensize(2)
        elif wind == 2 :
            hurricane_turtle.color("green")
            hurricane_turtle.pensize(3)
        elif wind == 3 :
            hurricane_turtle.color("yellow")
            hurricane_turtle.pensize(4)
        elif wind == 4 :
            hurricane_turtle.color("orange")
            hurricane_turtle.pensize(5)
        elif wind == 5 :
            hurricane_turtle.color("red")
            hurricane_turtle.pensize(6)
        else :
            hurricane_turtle.color("white")
            hurricane_turtle.pensize(1)
    
        hurricane_turtle.goto(long,lat)
        hurricane_turtle.pendown()
        hurricane_turtle.showturtle()
        if int(wind) > 0 :
            hurricane_turtle.write(wind)
    f.close()


    
    
            


    # DO NOT MODIFY THE FOLLOWING LINE! (It make sure the turtle window stays
    # open).
    turtle.done()



# Do not modify anything after this point.
if __name__ == "__main__":
    filename = input("Enter the name of the hurricane data file: ")
    animate(filename)
