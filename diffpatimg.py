import os
from PIL import Image, ImageDraw
from PIL import ImageFont

def create_circles_image(filename, xpositions, intensity, text):
    # Create a blank image with white background
    width, height = 800, 400   
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    y= height//2
    start_x = 400
    radius = 40
    radiusinv = 40
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default
    text_x = 10
    text_y = 10
    draw.text((text_x, text_y), text, fill="black", font=font)


    for m in range(5):
        current_x = start_x + xpositions[m]*10
        radius = radius*intensity[m]
        top = y - radius
        bottom = y + radius
        left = current_x - radius
        right = current_x + radius
        draw.ellipse([left, top, right, bottom], outline="grey", fill="grey")
    for m in range (5):
        current_x = start_x - xpositions[m]*10
        radiusinv = radiusinv*intensity[m]
        top = y - radiusinv
        bottom = y + radiusinv
        left = current_x - radiusinv
        right = current_x + radiusinv
        draw.ellipse([left, top, right, bottom], outline="grey", fill="grey")
    # Save the image
    image.save(filename)
    print(f"Image saved as {filename}")

      
