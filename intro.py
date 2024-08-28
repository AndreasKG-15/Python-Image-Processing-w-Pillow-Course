from PIL import Image

# Create an image via import
image = Image.open("cat.jpg")

# Analyze the image
# print(image.size)
# print(image.filename)
# print(image.format)

# Flip the image
# image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

# Shows the image
# image.show()

# Exercise
cat_rotated = image.rotate(30)
cat_rotated.show()
cat_rotated.save("cat_rotated.png", "png")

