import turtle

def check_pixel_color(x, y, target_color):
    """Returns 1 if  pixel at location (x, y) matches the target_color string.
       Returns 0 otherwise."""
    y = -y
    canvas = turtle.getcanvas()
    color = turtle.Screen().bgcolor()
    ids = canvas.find_overlapping(x, y, x, y)
    for id in ids:
        true_color = canvas.itemcget(id, "fill")
        if true_color:
            color = true_color
    return int(color == target_color)
