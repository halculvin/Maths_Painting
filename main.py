from canvas import Canvas
from shapes import Square, Rectangle

# Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas  with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw? Enter quit to quit. ")

    # Ask for rectangle data and create rectangle if the user entered "rectangle"
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green should the rectangle have? "))
        blue = int(input("How much blue should the rectangle have? "))
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width,
                       color=(red, green, blue))
        r1.draw(canvas)

    # Ask for square data and create square if user entered 'square'
    if shape_type.lower() == "square":
        sq_x = int(input("Enter x of the square: "))
        sq_y = int(input("Enter y of the square: "))
        sq_side = int(input("Enter a side of the square: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green should the square have? "))
        blue = int(input("How much blue should the square have? "))
        s1 = Square(x=sq_x, y=sq_y, side=sq_side, color=(red, green, blue))
        s1.draw(canvas)

    # Break the loop if user enters 'quit'
    if shape_type.lower() == "quit":
        break

canvas.make('canvas.png')
