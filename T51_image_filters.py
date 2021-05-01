#Group 51
#Organized by Ngo Huu Gia Bao 101163137 

from Cimpl import *

"""""""""BASIC FILTERS FUNCTIONS FROM MILESTONE 1"""""""""

def red_channel(original_image: Image) -> Image:                    #RED FILTER
    """ Written by Alexander Szabo, 101151844, Group 51
    Returns the photo with all the green and blue values filtered out.
    The photo returned will only have its red values, making the final photo only different shades of red.

    >>> original_image = load_image(choose_file())
    >>> show(red_channel(original_image))
    """
    new_image = copy (original_image)
    height_restraint = get_height(new_image)
    width_restraint = get_width(new_image)
    height = 0
    while height < height_restraint:
        length = 0
        while length < width_restraint:
            open_pixel = get_color(new_image, length, height)
            r, g, b = open_pixel
            new_colour = create_color(r, 0, 0)
            set_color(new_image, length, height, new_colour)
            length += 1
        height += 1
        
    return new_image


def green_channel(original_image: Image) -> Image:                 #GREEN FILTER
    """ Written by Jaden Paget, 101119947, Group 51
    Returns an image that only contains its green components of each pixel.

    >>> green_channel(original_image)
    >>> "Test passed, all pixels contain only their green componant"
    """
    
    new_image = copy (original_image)
    for pixel in new_image:
        x,y,(r, g, b) = pixel
        color = create_color(0, g, 0)
        set_color(new_image, x, y, color)

    return new_image


def blue_channel (original_image: Image) -> Image:                  #BLUE FILTER
    """ Written by Ngo Huu Gia Bao, 101163137, Group 51
    The function takes the original image and returns blue image by setting the red, green color in each pixel in a picture is equal to 0
    
    >>> original_image = load_image(choose_file())
    >>> show(blue_channel(original_image))
    """
    new_image = copy(original_image)                     
    for pixel in new_image:
        
        x,y,(r,g,b) = pixel
        color = create_color (0,0,b)
        set_color (new_image,x,y,color)
    
    return new_image


def combine(red_image: Image, green_image: Image, blue_image: Image) -> Image:              #COMBINE FILTER
    """ Written by Ahmed Moussa, 101142994, Group 51
    Returns a combination of 3 images passed to the function. The colors of the images at every pixel are summed.
    
    ! The Recieved Images Must be of the Same Size !
    *Note: The reason I did not create a copy of the image was to not waste time allocating space for a new object and since the passed image is local it will not be globally modified or desroyed*
    *Note: This function is designed for maximum efficiency without multithreading*
    
    >>>  combine(red_image, green_image, blue_image)
    returns: Object <Cimpl.Image>
    """
    for x, y, color in red_image:                        # for every pixel in the current image image[i] (*note that the data of the pixel is collected from within the for loop's structure*)
        newColour = [r + g + b for r, g, b in zip(red_image.pixels[x,y], green_image.pixels[x,y], blue_image.pixels[x,y])] # Combine the colors of all 3 images into one tuple of colors
        set_color(red_image, x, y, Color(newColour[0], newColour[1], newColour[2]))  # Set the color of the final image at the pixel to the combined color
    return red_image                                    # return the combined image


"""""""""FILTERS FROM MILESTONE 2"""""""""
def grayscale(image: Image) -> Image:
    """ Written by Carleton University Staff
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)      
    return new_image


"""""""""FILTERS FROM P4"""""""""

def two_tone( original_image: Image, color1: str, color2: str) -> Image:              # TWO TONE FILTER
    """ Written by Ngo Huu Gia Bao, 101163137, Group 51
    Return an two tone image whose colors can be chose 

    >>> original_image = load_image(choose_file())
    >>> show(two_tone(original_image))
    """
    
    new_image = copy (original_image)
    
    #BLACK
    if color1 == "black":
        color1 = create_color (0,0,0)
        
    if color2 == "black":
        color2 = create_color (0,0,0)
          
    #WHITE   
    if color1 == "white":
        color1 = create_color (255,255,255)     
    
    if color2 == "white":
        color2 = create_color (255,255,255)
        
    #RED    
    if color1 == "red":
            color1 = create_color (255,0,0)    
        
    if color2 == "red":
            color2 = create_color (255,0,0)
              
    #LIME    
    if color1 == "lime":
            color1 = create_color (0,255,0)
            
    if color2 == "lime":
            color2 = create_color (0,255,0)
            
    #BLUE        
    if color1 == "blue":
            color1 = create_color (0,0,255)
            
    if color2 == "blue":
            color2 = create_color (0,0,255)
            
    #YELLOW        
    if color1 == "yellow":
            color1 = create_color (255,255,0)  
            
    if color2 == "yellow":
            color2 = create_color (255,255,0)
            
    #CYAN        
    if color1 == "cyan":
            color1 = create_color (0,255,255) 
            
    if color2 == "cyan":
            color2 = create_color (0,255,255)
            
    #MAGNETA        
    if color1 == "magneta":
            color1 = create_color (255,0,255) 
            
    if color2 == "magneta":
            color2 = create_color (255,0,255)
            
    #GRAY        
    if color1 == "gray":
            color1 = create_color (128,128,128)
                   
    if color2 == "gray":
            color2 = create_color (128,128,128)
               
    for pixel in new_image:
        
        x,y, (r,g,b ) = pixel 
        brightness = (r + g + b) // 3
        
        if 0 <= brightness <= 127:
            set_color (new_image,x,y,color1)
            
        if 128 <= brightness <= 255:
            set_color (new_image,x,y,color2)
        
    return new_image


def three_tone( original_image: Image, color1: str, color2: str, color3: str) -> Image:         # THREE TONE FILTER
    """ Written by Ngo Huu Gia Bao, 101163137, Group 51
    Return an three tone image whose colors can be chose 

    >>> original_image = load_image(choose_file())
    >>> show(three_tone(original_image))
    """
    
    new_image = copy (original_image)
    
    #BLACK
    if color1 == "black":
        color1 = create_color (0,0,0)
        
    if color2 == "black":
        color2 = create_color (0,0,0)
        
    if color3 == "black":
        color3 = create_color (0,0,0)    
    
    #WHITE   
    if color1 == "white":
        color1 = create_color (255,255,255)     
    
    if color2 == "white":
        color2 = create_color (255,255,255)
        
    if color3 == "white":
        color3 = create_color (255,255,255)
        
    #RED    
    if color1 == "red":
            color1 = create_color (255,0,0)    
        
    if color2 == "red":
            color2 = create_color (255,0,0)
            
    if color3 == "red":
            color3 = create_color (255,0,0) 
            
    #LIME    
    if color1 == "lime":
            color1 = create_color (0,255,0)
            
    if color2 == "lime":
            color2 = create_color (0,255,0)
            
    if color3 == "lime":
            color3 = create_color (0,255,0)            
    
    #BLUE        
    if color1 == "blue":
            color1 = create_color (0,0,255)
            
    if color2 == "blue":
            color2 = create_color (0,0,255)
            
    if color3 == "blue":
            color3 = create_color (0,0,255)            
    
    #YELLOW        
    if color1 == "yellow":
            color1 = create_color (255,255,0)  
            
    if color2 == "yellow":
            color2 = create_color (255,255,0)
            
    if color3 == "yellow":
            color3 = create_color (255,255,0)            
    
    #CYAN        
    if color1 == "cyan":
            color1 = create_color (0,255,255) 
            
    if color2 == "cyan":
            color2 = create_color (0,255,255)
            
    if color3 == "cyan":
            color3 = create_color (0,255,255)            
    
    #MAGNETA        
    if color1 == "magenta":
            color1 = create_color (255,0,255) 
            
    if color2 == "magenta":
            color2 = create_color (255,0,255)
            
    if color3 == "magenta":
            color3 = create_color (255,0,255) 
            
    #GRAY        
    if color1 == "gray":
            color1 = create_color (128,128,128)
                   
    if color2 == "gray":
            color2 = create_color (128,128,128)
            
    if color3 == "gray":
            color3 = create_color (128,128,128)            
            
    for pixel in new_image:
        
        x,y, (r,g,b ) = pixel 
        brightness = (r + g + b) // 3
        
        if 0 <= brightness <= 84:
            set_color (new_image,x,y,color1)
            
        if 85 <= brightness <= 170:
            set_color (new_image,x,y,color2)
            
        if 171 <= brightness <= 255:
            set_color (new_image,x,y,color3)
            
    return new_image


def extreme_contrast(original_image: Image) -> Image :                              #EXTREME CONTRAST FILTER
    """ Written by Jaden Paget, 101119947, Group 51
    Returns a copy of an image in which the contrast between the pixels has been maximized.
    
    >>> original_image = load_image(choose_file())
    >>> show(extreme_contrast(original_image))
    """
    
    new_image = copy(original_image)
    for pixel in new_image:
        x,y,(r, g, b) = pixel
        if r < 128:
            r = 0
        else:
            r = 255
        if g < 128:
            g = 0
        else:
            g = 255
        if b < 128:
            b = 0
        else:
            b = 255
        color = create_color(r, g, b)
        set_color(new_image, x, y, color)
    return new_image



def sepia(original_image: Image) -> Image:                        # SEPIA FILTER
    """ Written by Ahmed Moussa, 101142994, Group 51
    Tint the provided image with a sepia tone
   
    >>> original_image = load_image(choose_file())
    >>> show(sepia(original_image))
    """
    new_image = copy (original_image)
    grayImg = grayscale(new_image)
    for x, y, (r, g, b) in grayImg:
        if r < 63:
            set_color(grayImg, x, y, create_color(r*1.1, g, b*0.9))
        if r >= 63 and r <= 191:
            set_color(grayImg, x, y, create_color(r*1.15, g, b*0.85))
        if r > 191:
            set_color(grayImg, x, y, create_color(r*1.08, g, b*0.93))
    return grayImg


def _adjust_component(original_image: Image) -> list:                        # ADJUST COMPONENT FOR POSTERIZE FILTER 
    """ Written by Alexander Szabo, 101151844, Group 51
    Returns the midpoint value of the quadrant for the RGB values, respectively, of each pixel in an image. 
        
    >>>(43,147,235)
    (31, 159, 223)
    """    
    
    adjust = copy (original_image)
    height_restraint = get_height(adjust)
    width_restraint = get_width(adjust)
    centered_values = [[0,0,0]] * (height_restraint * width_restraint)
    list_count = 0
    height = 0
    while height < height_restraint:
        width = 0
        while width < width_restraint:
            open_pixel = get_color(adjust, width, height)
            values = list(open_pixel)
            i = 0
            for item in values:
                if item <= 63:
                    values[i] = 31
                elif 63 < item <= 127:
                    values[i] = 95
                elif 127 < item <= 191:
                    values[i] = 159
                elif 192 < item <= 255:
                    values[i] = 223
                i += 1 
            centered_values[list_count] = values
            list_count += 1
            width += 1
        height += 1
    
    return centered_values


def posterize(selected_image: Image) -> Image:                       # POSTERIZE FILTER
    """ Written by Alexander Szabo, 101151844, Group 51
    Returns the posterized version of a selected image
    """
    new_image = copy(selected_image)
    
    height_restraint = get_height(new_image)
    width_restraint = get_width(new_image)
    count = 0
    height = 0
    pixel_list = _adjust_component(selected_image)
    while height < height_restraint:
        width = 0
        while width < width_restraint:
            posterized_values = tuple(pixel_list[count])
            r, g, b = posterized_values
            new_colour = create_color(r, g, b)
            set_color(new_image, width, height, new_colour)
            count += 1
            width += 1
        height += 1
    
    return new_image


"""""""""FILTERS FROM P5"""""""""

def detect_edges (original_image: Image, threshold: str) -> Image:                  #DECTECT EDGES FILTER    
    """ Written by Ngo Huu Gia Bao, 101163137, Group 51
    Return an image that looks like a pencil sketch, by changing the pixels'colours to black or white,
    for every pixel that has a pixel below it, check the contrast between the two pixels. If the contrast is high, change the top pixel's colour to black, but if the contrast is low, change the top pixel's colour to white.
    """
    new_image = copy (original_image)
    for h in range ( 1, get_height (new_image) - 1):
        for w in range ( 1, get_width (new_image) - 1):
            top_red, top_green, top_blue = get_color ( new_image, w, h )
            bottom_red, bottom_green, bottom_blue = get_color ( new_image, w, h+1 )
            
            avg_rgb_top = (top_red + top_green + top_blue) // 3
            avg_rgb_bottom = (bottom_red + bottom_green + bottom_blue) // 3
            brightness = abs ( avg_rgb_top - avg_rgb_bottom )
            
            if brightness > int(threshold):
                new_color = create_color (0,0,0)
        
            else:
                new_color = create_color (255,255,255)
                
                
            set_color ( new_image, w, h, new_color )
            
    return new_image


def detect_edges_better(original_image: Image, threshold: str) -> Image:            # BETTER DECTECT EDGES FILTER    
    """ Written by Alexander Szabo, 101151844, Group 51 
    Developed by the same pair that developed detect_edges
    """
    
    new_image = copy (original_image)
    for h in range(get_height(new_image) - 1):
        for w in range(get_width(new_image) - 1):
            top_red, top_green, top_blue = get_color ( new_image, w, h )
            bottom_red, bottom_green, bottom_blue = get_color ( new_image, w, h+1 )
            right_red, right_green, right_blue = get_color( new_image, w + 1, h)
            avg_rgb_top = (top_red + top_green + top_blue) / 3
            avg_rgb_bottom = (bottom_red + bottom_green + bottom_blue) / 3
            avg_rgb_right = (right_red + right_green + right_blue ) / 3
            
            
            if abs(avg_rgb_top - avg_rgb_bottom) > int(threshold) or abs(avg_rgb_top - avg_rgb_right) > int(threshold):
                new_color = create_color (0,0,0)
        
            else:
                new_color = create_color (255,255,255)
                
                
            set_color ( new_image, w, h, new_color )
    
    white = create_color(255,255,255)
    bottom_c = 0
    width = get_width(new_image)
    height = get_height(new_image)
    while bottom_c < width:
        set_color(new_image, bottom_c, height - 1, white)
        bottom_c += 1
        
    right_c = 0
    while right_c < height:
        set_color(new_image, width - 1, right_c, white)
        right_c += 1
    
    return new_image


def vertical(img: Image) -> Image:                                  # VERTICAL FLIP FILTER
    """ Written by Ahmed Moussa, 101142994, Group 51
    Vertically flip provided image

    >>> original_image = load_image(choose_file())
    >>> show(vertical(original_image))
    """
    height = get_height(img) - 1                                    # Get height of the selected image subtract 1
    newimg = copy(img)                                              # Create copy of the original image to manipulate
    for y in range(height + 1):                                     # For every row of pixels
        for x in range(get_width(img)):                             # For every pixel in the row
            newimg.pixels[x,y] = img.pixels[x,y + height - 2 * y]   # Flip the pixel onto it's vertically flipped equivalent accross the central axis of the image
    return newimg                                                   # Return flipped image# Return flipped image


def horizontal(original_image: Image) -> Image:                    # HORIZONTAL FLIP FILTER
    """ Written by Jaden Paget, 101119947, Group 51
    Horizontally flips the passed image

    >>> original_image = load_image(choose_file())
    >>> show(horizontal(original_image))
    """
    new_image = copy(original_image)
    width = get_width(new_image)
    height = get_height(new_image)
    fliphorizontal = create_image(width, height)
    n = 1
    for pixel in new_image:
        x,y,(rgb) = pixel
        set_color(fliphorizontal, width - n, y, rgb)
        n += 1
        if n == width+1:
            n = 1
    
    return fliphorizontal