

#!/usr/bin/env python3
import string 
import cv2
import os 
import math 

class GrayImageConverter:
    def __init__(self):
        self.load_image()
        self.resize(260, 90)
        self.i2a()
        self.ascii = string.punctuation
        self.display()

    def load_image(self):
        image = cv2.imread(os.path.join(".", "swan.jpg"))
        return image 

    def resize(self, width, height):
        image = self.load_image()
        image  = cv2.resize(image, (width, height))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        return image

    def i2a(self):
        ascii_image = ""
        ascii =  string.punctuation
        
        image = self.resize(260, 90)
        for row in image:
            for pixel in row:
                ascii_image += ascii[pixel // 40]
            ascii_image += "\n"
        return ascii_image

    def display(self):
        ascii_text = self.i2a()
        print(ascii_text)


if __name__ == "__main__":
   GrayImageConverter() 
