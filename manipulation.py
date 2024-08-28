from PIL import Image

# import an image
image = Image.open("cat.jpg")


# Flip
image_transpose = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

# Rotation
image_rotate = image.rotate(45, expand = False, center = (0, 0))

# Crop                              Left, Top, Right, Bottom
image_crop = image.crop((800, 600, 1600, 1600))

# Resize                               Width, Height
image_resize = image.resize((1000, 600))

# Combine
combined_image = image.transpose(Image.Transpose.ROTATE_90).resize((2000, 1500)).rotate(10)

combined_image.show()
#image.show()
#image_resize.show()