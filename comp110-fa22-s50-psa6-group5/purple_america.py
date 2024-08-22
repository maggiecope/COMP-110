"""
Module: purple_america

Program for visualizing election results in interesting ways.

Authors:
1) Andrew Ling - aling@sandiego.edu
2) Maggie Cope - mcope@sandiego.edu
"""

import turtle

def draw_subregion(my_turtle, polygon_points):
    """
    Draws a polygonal subregion.

    Parameters:
    my_turtle (type: Turtle) - The turtle that will do the drawing.
    polygon_points (type: List) - List of tuples of the coordinates of the
      polygonal region.

    Returns:
    None
    """
    #creates turtle and hides it and makes it pen up 
    t = my_turtle 
    t.hideturtle()
    t.penup()


#makes the turtle draw a polygon by moving the turtle to the (x,y)
#coordinates of polygon_points
    for i in range(len(polygon_points)):
        x, y = (polygon_points[i])
        
        t.goto(x,y)
        t.showturtle()
        t.pendown()
#closes the polygon 
    t.goto(polygon_points[0])


    


def draw_filled_subregion(my_turtle, polygon_points, style, votes):
    """Parameters:
        my_turtle: a turtle object 
        polygon_points: a list of (x,y) points (ie: tuples) that define the points of a polygon 
        style: string describing the style of drawing 
        votes: tuple containing 1)the number of votes for the democratic candidate,
            2)number of votes for the republican canidate, 
            and 3)number of votes for the other candidates 
        
    Return: turtle draws a filled polygon """
    #defines and sets up turtle 
    t = my_turtle
    t.hideturtle()
    t.penup()
    
    #associates the political party with the number of votes it recieved 
    republican,democrat,other = votes
    #adds all of the votes together and assigns value to total_votes 
    total_votes = republican + democrat + other
    
    #based on the style parameter, sets pen color and fill color 
    if style == "black-white":
        t.pencolor("black")
        t.fillcolor("white")
    elif style == "red-blue":
        t.pencolor("white")
        if int(democrat) < int(republican) > int(other):
            t.fillcolor("red")
        elif int(republican) < int(democrat) > int(other):    
            t.fillcolor("blue")
        else:
            t.fillcolor("gray")
    elif style == "purple":
        t.pencolor("white")
        if total_votes != 0: 
            purple_fill = ((republican)/(total_votes)), ((other)/(total_votes)),((democrat)/(total_votes))
            t.fillcolor(purple_fill) 
        else: 
            t.fillcolor("gray")
    else:
        t.pencolor("gray")
    #once the style is set the turtle begins to fill and draw the subregion
    t.begin_fill()
    draw_subregion(my_turtle, polygon_points)
    #done 
    t.end_fill()
  



def read_subregion(geo_file):
    """ Parameters: 
            geo_file: a file object of an already opened file containing 
            data about the subregion 
            
        Return:
        Name of subregion and a list of (longitude, latitude) tuples """
    
  
    long_lat = []
    #reads blank line
    blank_line = geo_file.readline()
   
    #reads subregion name and cleans it
    subregion_name = geo_file.readline()
    clean_name = subregion_name.strip()
    
    #reads the enclosing regions name
    enclosing_region = geo_file.readline()
    
    #reads the number of points in the subregions polygon and makes 
    #points equal to the integer of that value 
    number_points = geo_file.readline()
    clean_points = number_points.strip()
    points = int(clean_points)
    
    # reads "points" number of lines 
    # accumulating (longitude/latitude) tuples to long_lat 

    while len(long_lat)!= points:
        lines = geo_file.readline()
        clean_line = lines.strip()
        
        x,y = clean_line.split()
        n = (float(x),float(y))
        long_lat.append(n)
        
       

    return clean_name, long_lat 

def get_election_results(election_filename):
    """ Parameters:
            election_filename:The name of a file containing election data 
            
        Return: 
          dictionary that associates region names 
          with a tuple of vote counts for that region."""
    
    f = open(election_filename, 'r')
    line = f.readline()

    #creates dictionary called results 
    results = {}

    #reads each line in the file and adds the region names associated with
    #a tuple of votes counts for that region to results 
    for line in f:
        vals = line.split(",")
        results[vals[0]] = (int(vals[1]),int(vals[2]),int(vals[3]))
    f.close()

    return results

def draw_map(geo_filename, election_results, style):
    """ Parameters:
            geo_filename: The name of a file containing geographic data for the whole region
            election_results: A dictionary associating subregion names with voting data tuples.
            style: A string describing the map style; either “black-white”, “red-blue”, or “purple”.
        
        Return:
    
     """
    f = open(geo_filename, 'r')
    #reads in minimum values longitude and latitude data 
    minimums = f.readline()
    min_long, min_lat = minimums.split()
   
   #reads in maximum values longitude and latitude data 
    maximums = f.readline()
    max_long, max_lat = maximums.split()
    ###reads in the number of subregions 
    number_sub = f.readline()
    subregions = int(number_sub)
    
    #creates and sets up turtle###
    t = turtle.Turtle()
    s = turtle.Screen()
    s.setworldcoordinates(float(min_long), float(min_lat), float(max_long), float(max_lat))
    t.speed("fastest")
    s.tracer(0,0)

    #reads the subregion, draws the subregion using the correct style 
    #and election results 
    for n in range(0, subregions):    
        name, points = read_subregion(f)
        draw_filled_subregion(t, points, style, election_results.get(name,(0,0,0)))
    

    #clean up
    s.update()
    turtle.done()
    f.close()



 



    

def main():
    """
    Returns: map of the US votes in the selected style, election file, geography file
    """

    geo_filename = input("Enter the name of the geography file: ")
    election_filename = input("Enter the name of the election data file: ")

    valid_input = False
    while not valid_input:
        prompt_string = "What style of map would you like?\n"
        prompt_string += "Enter 1 for black & white.\n"
        prompt_string += "Enter 2 for red & blue.\n"
        prompt_string += "Enter 3 for purple.\n"
        style_selection = input(prompt_string)
        if style_selection == "1":
            valid_input = True
            style = "black-white"
        elif style_selection == "2":
            valid_input = True
            style = "red-blue"
        elif style_selection == "3":
            valid_input = True
            style = "purple"
        else:
            print("Invalid selection!")

    #calls election_results and draw_map to 
    # draw the subregion (with a turtle),  using the election data 
    # to determine the color fill of the subregion  

    election_results = get_election_results(election_filename)
    draw_map(geo_filename, election_results, style)

    pass # Replace this line with your implementation of main


"""
WARNING: Do NOT modify anything below this point.
"""
if __name__ == "__main__":
    main()
