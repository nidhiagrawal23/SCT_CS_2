from PIL import Image

# Load an image
img = Image.open('p2.jpeg')
pixels = img.load()

# Coordinates of the pixels you want to swap
x1, y1 = 50, 50
x2, y2 = 100, 100

# Swap the pixels
temp = pixels[x1, y1]
pixels[x1, y1] = pixels[x2, y2]
pixels[x2, y2] = temp

# Save the modified image
img.save('swapped_p2.jpeg')
