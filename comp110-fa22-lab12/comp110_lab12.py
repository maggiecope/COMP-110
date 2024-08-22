"""
Module: comp110_lab12

Code for COMP110 Lab 12 (Image Manipulation).

Author(s):
1) Name - USD Email Address
2) Name - USD Email Address
"""

import comp110_image

def negative(my_pic):
    """
    Applies the "negative" filter to the given picture.

    Parameter(s):
    my_pic (type: Picture) - The image to filter.
    """
    for row in range(my_pic.getHeight()):
        for col in range(my_pic.getWidth()):
            pix = my_pic.getPixel(col, row)
            pix.setRed(255 - pix.getRed())
            pix.setGreen(255 - pix.getGreen())
            pix.setBlue(255 - pix.getBlue())

def grayscale(my_pic):
    for row in range(my_pic.getHeight()):
        for col in range(my_pic.getWidth()):
            pix = my_pic.getPixel(col, row)
            red = pix.getRed()
            green = pix.getGreen()
            blue = pix.getBlue()
            average = (red+green+blue)//3
            pix.setRed(average)
            pix.setGreen(average)
            pix.setBlue(average)

def custom(my_pic):

    stripe = 0
    if stripe==0:
        x=255
        y=0
        z=0
    if stripe==1:
        x=255
        y=255
        z=255


    for row in range(0, my_pic.getHeight(), 4):
        for col in range(my_pic.getWidth()):
            pix = my_pic.getPixel(col, row)
            pix.setRed(x)
            pix.setGreen(y)
            pix.setBlue(z)
            if stripe==0:
                stripe=1
            else:
                stripe=0
            
    for row in range(my_pic.getHeight()//4):
        for col in range(my_pic.getWidth()//2):
            pix = my_pic.getPixel(col, row)
            pix.setRed(0)
            pix.setGreen(0)
            pix.setBlue(255)



    


def main():
    image_filename = input("Enter the name of a picture file: ")
    pic = comp110_image.Picture(filename=image_filename)
    pic.setTitle("Original Picture")
    pic.show()

    custom(pic)

    pic.setTitle("Filtered Picture")
    pic.show()

    # saves the modified picture to a new file
    pic.save("filtered.jpg")



""" DO NOT MODIFY ANYTHING BELOW THIS LINE! """
if __name__ == "__main__":
    main()
