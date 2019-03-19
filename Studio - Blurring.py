import image
import sys
import random

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for col in range(1, img.getWidth() - 1):
    for row in range(1, img.getHeight() - 1):
        orig_pixel = img.getPixel(col,row)
        
        red = orig_pixel.getRed()
        green = orig_pixel.getGreen()
        blue = orig_pixel.getBlue()  
        
        #switch_pixel is a list of all surrounding pixels (including orig_pixel)
        switch_pixel = [img.getPixel(col,row),img.getPixel(col+1,row-1),img.getPixel(col+1,row),img.getPixel(col+1,row+1),
                        img.getPixel(col,row+1),img.getPixel(col-1,row+1),img.getPixel(col-1,row),img.getPixel(col-1,row-1),
                        img.getPixel(col,row-1),img.getPixel(col+1,row-1)]
        
        new_pixel = random.choice(switch_pixel)
        image.Pixel(red,green,blue)
        new_img.setPixel(col,row,new_pixel)                                      
                                                            
new_img.draw(win)
win.exitonclick()
