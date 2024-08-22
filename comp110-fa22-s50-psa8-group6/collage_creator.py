"""
Module: collage_creator

A program to create an Andy Warhol-style collage.

Authors:
1) Maggie Cope - mcope@sandiego.edu
2) Ella Fahrendorf - efahrendorf@sandiego.edu
"""

import comp110_image


def copy_to(src_img, dest_img, start_x, start_y):
    """
    Copies one image into another, start at the given starting coordinate.

    DO NOT MODIFY THIS FUNCTION!!!

    Parameters:
    src_img (type: Picture) - The picture to copy.
    dest_img (type: Picture) - The picture to copy into.
    start_x (type: int) - The column where we start copying to dest_img.
    start_y (type: int) - The row where we start copying to dest_img.
    """
    for x in range(src_img.getWidth()):
        for y in range(src_img.getHeight()):
            srcPixel = src_img.getPixel(x,y)
            dest_img.setPixel(x + start_x, y + start_y, srcPixel)

def unique_filter(img):
    """Parameters: img - picture obj 
    returns: filtered image  """
    filtered_img = img.copy() 
    for y in range(filtered_img.getHeight()):
        for x in range(filtered_img.getWidth()):
            p = filtered_img.getPixel(x,y)
            red = p.getRed()
            if red > 100:
                p.setRed(250)
            else:
                p.setRed(0)

            
    return filtered_img


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

def convolution_filter(img, kernel):
    """
    Performs convolution on all non-border pixels in the img, using the given
    convolution kernel.

    Params:
    img (type: Picture obj) - The picture to modify.
    kernel (type: 2D list of int) - The kernel to apply.
    """

    # Make a copy of the original image. This copy will be modified while the
    # original will remain unchanged.
    filtered_img = img.copy()

    # To Do: modify range to avoid border pixels
    for x in range(1,img.getWidth()-1):
        for y in range(1, img.getHeight()-1):
            apply_kernel(img, filtered_img, x, y, kernel)

    return filtered_img

def flip_filter(img):
    """Parameters: img (picture obj) 
    Returns: flipped picture around axis as filtered_img  """
    filtered_img = img.copy()
    w = filtered_img.getWidth()
    for y in range(filtered_img.getHeight()):
        for x in range(w//2):
            left_pix = img.getPixel(x,y)
            right_pix = img.getPixel(w-1-x,y)
            filtered_img.setPixel(x,y,right_pix)
            filtered_img.setPixel(w-1-x, y, left_pix)
    return filtered_img

def mirror_filter(img):
    """Paramters: img (picture obj)
    returns: filtered image of the orginal image mirrored"""
    filtered_img = img.copy()
    w = filtered_img.getWidth()
    mirror_pt = w//2
    for y in range(filtered_img.getHeight()):
        for x in range(mirror_pt):
            left_pix = filtered_img.getPixel(x,y)
            filtered_img.setPixel(w-w-x,y,left_pix)
    return filtered_img

def grayscale_filter(img):
    """ paramters: img - picture obj 
    returns filtered image 
    
    this function creates acopy of the image in a grayscale filter """
    my_pic = img.copy()
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
    return my_pic
def negative_filter(img):
    """
    Applies the "negative" filter to the given picture.

    Parameter(s):
    img (type: picture obj) - The image to filter.
    returns: my_pic (type: Picture)
    """
    my_pic = img.copy()
    for row in range(my_pic.getHeight()):
        for col in range(my_pic.getWidth()):
            pix = my_pic.getPixel(col, row)
            pix.setRed(255 - pix.getRed())
            pix.setGreen(255 - pix.getGreen())
            pix.setBlue(255 - pix.getBlue())
    return my_pic

def create_filtered_pics(img):
    """ paramter: img (type: picture obj)
    returns a tuple of the filtered images """
    unique = unique_filter(img)
    convolution = convolution_filter(img, [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    flip = flip_filter(img)
    mirror = mirror_filter(img)
    grayscale = grayscale_filter(img)
    negative = negative_filter(img)
    
    return (unique, convolution, flip, mirror, grayscale, negative)

def assemble_collage(filtered_pics):
    """Paramter: filtered pics - a tuple of the filtered imagges
    Returns - collage of all the filtered pictures 
    
    """
    h = filtered_pics[0].getHeight()
    w = filtered_pics[0].getWidth()
    collage = comp110_image.Picture(w*3, h*2)
    copy_to(filtered_pics[0], collage, 0, 0)
    copy_to(filtered_pics[1], collage, w, 0)
    copy_to(filtered_pics[2], collage, 0, h)
    copy_to(filtered_pics[3], collage, w, h)
    copy_to(filtered_pics[4], collage, w*2,0)
    copy_to(filtered_pics[5], collage, w*2, h)

    return collage

def shrink(img, scale_factor):
    """Paraters: img - picture obj 
    scale factor -int 

    Returns: new image whose height and width are a shrunk size of the orginal 
    """
   
    smaller_img = comp110_image.Picture(img.getWidth()//scale_factor, img.getHeight()//scale_factor)
    for x in range(smaller_img.getWidth()):
        for y in range(smaller_img.getHeight()):
            orig_x = x * scale_factor
            orig_y = y * scale_factor
            orig_pixel = img.getPixel(orig_x, orig_y)
            smaller_img.setPixel(x, y, orig_pixel)

    return smaller_img

def get_shrink_factor(img, max_width, max_height):
    """Paramters:
    img - picture obj 
    max_width - maximum allowed width after shrinking 
    max_height = maximum allowed height after shrinking 
    
    Returns - factor (int) """
    h = img.getHeight()
    w = img.getWidth()
    
    factor = 2

    if h <= max_height and w<= max_width:
        return int(1)
    else:
        while h >= max_height or w >= max_width:
            h = img.getHeight()//factor
            w = img.getWidth()//factor
            if h <= max_height and w <= max_width:
                return factor
            else:
                factor+=1 



def main():
    """Asks user to input the name of the image they want to make a collage out of, 
    that images max height and max width, and what they  want to save the image as"""


    og_image = comp110_image.Picture(filename = input("Enter the name of the original image file: "))
    filtered_img= input("Enter the filename you will save the collage to: ")
    max_w = int(input("Enter the maximum collage width: "))
    max_h = int(input("Enter the maximum collage height: "))
    factor = get_shrink_factor(og_image, max_w//3, max_h//2)
    scale = shrink(og_image, int(factor))
    filter = create_filtered_pics(scale)
    collage = assemble_collage(filter)
    collage.show()
    collage.save(filtered_img)

if __name__ == "__main__":
    main()
