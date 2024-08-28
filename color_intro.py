from PIL import Image

image = Image.open("checkerboard.png")

# Get one pixel
#print(image.getpixel((0, 0)))

#  Greyscale images
#red_greyscale_image = image.getchannel("R")
#blue_greyscale_image = image.getchannel("B")

#red_greyscale_image.show()
#blue_greyscale_image.show()

# Change the pixel colour
#image.putpixel((0, 0), (255, 0, 0))

# Exercise
print(image.getpixel((0, 0)))
for x in range(image.size[0]):
    for y in range(image.size[1]):
        if image.getpixel((x, y)) [0] == 0:
            image.putpixel((x, y), (200, 20, 20))
        
image.show()