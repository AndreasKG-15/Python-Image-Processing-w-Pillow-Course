from PIL import Image, ImageOps

# create an image
image = Image.open("dog.jpg")


# position changes
image_mirror = ImageOps.mirror(image)
# image_scale = ImageOps.scale(image, 0.5)

# colour changes
image_invert = ImageOps.invert(image_mirror)
# add and remove
image_border = ImageOps.expand(
    image_invert, 
    border=50, 
    fill=(255, 255, 255))
# image_padded = ImageOps.pad(image, (4000, 6000))
# image_crop = ImageOps.crop(image=image, border=200)


# show
# image_invert.show()
image_border.show()
# image_mirror.show()
# image_padded.show()
# image_crop.show()

# print(image.size)
# print(image_scale.size)
# image_scale.show()