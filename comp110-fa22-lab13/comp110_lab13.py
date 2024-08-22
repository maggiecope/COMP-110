"""
Module: comp110_lab13

Starter code for Lab 13 (Image convolution)
"""

import comp110_image


def apply_kernel(img, filtered_img, x, y, kernel):
    """
    Applies the given kernel to the pixel in img at (x,y).

    Params:
    img (type: Picture) - The original (unmodified) image.
    filtered_img (type: Picture) - A copy of the original that will have the
        kernel applied to it.
    x (type: int) - The x value of the pixel to modify
    y (type: int) - The y value of the pixel to modify
    kernel (type: 2D list of int) - The kernel to apply.
    """

    # accumulator variables
    red_sum = 0
    green_sum = 0
    blue_sum = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            pix = img.getPixel(x+i,y+j)
            red_sum += pix.getRed() * kernel[j+1][i+1]
            green_sum += pix.getGreen() * kernel[j+1][i+1] 
            blue_sum += pix.getBlue() * kernel[j+1][i+1]
    if red_sum>255:
        red_sum=255
    elif red_sum<0:
        red_sum=0
    if green_sum>255:
        green_sum=255
    elif green_sum<0:
        green_sum=0
    if blue_sum>255:
        blue_sum=255
    elif blue_sum<0:
        blue_sum=0  
    pix = filtered_img.getPixel(x,y)
    pix.setRed(red_sum)
    pix.setGreen(green_sum)
    pix.setBlue(blue_sum)


       
    # To Do: If red_sum, green_sum, or blue_sum are outside of the correct
    # range, set them to be within the range. For example, if red_sum is less
    # than 0, change it to 0.
    # For this step, you'll need to have three consecutive chained conditionals
    # (one for each of the color components).

    # To Do: Update the pixel at (x, y) in filtered_img to change the red,
    # green, and blue components to the sums we calculated.


def convolution(img, kernel):
    """
    Performs convolution on all non-border pixels in the img, using the given
    convolution kernel.

    Params:
    img (type: Picture) - The picture to modify.
    kernel (type: 2D list of int) - The kernel to apply.
    """

    # Make a copy of the original image. This copy will be modified while the
    # original will remain unchanged.
    filtered_img = img.copy()

    # To Do: modify range to avoid border pixels
    for x in range(img.getWidth()-1):
        for y in range(img.getHeight()-1):
            apply_kernel(img, filtered_img, x, y, kernel)

    return filtered_img

def main():
    # Do not modify this function

    cat_img = comp110_image.Picture(filename="cute-cat.jpg")
    cat_img.setTitle("Before convolution (edge detect)")
    cat_img.show()
    convoluted_cat = convolution(cat_img, [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    convoluted_cat.setTitle("After convolution (edge detect)")
    convoluted_cat.show()


""" DO NOT MODIFY ANYTHING BELOW THIS LINE! """
if __name__ == "__main__":
    main()
