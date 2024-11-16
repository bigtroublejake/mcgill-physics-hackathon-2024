from PIL import Image, ImageDraw

def create_circles_image(filename, xpositions, intensity):
    # Create a blank image with white background
    width, height = 800, 400   
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    y= height//2
    start_x = 400
    radius = 40
    # Draw circles
    for m in range(5):
        current_x = start_x + xpositions[m]*10
        print(current_x)
        radius = radius*intensity[m]
        print(radius)
        top = y - radius
        bottom = y + radius
        left = current_x - radius
        right = current_x + radius
        draw.ellipse([left, top, right, bottom], outline="black", fill="black")

    # Save the image
    image.save(filename)
    print(f"Image saved as {filename}")

      
