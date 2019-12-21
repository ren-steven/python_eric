import arcade

# set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#Open the window, Set the window title and dimentions(width and height)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Rectangle With Face")

# Set the background color to white. 
# For a list of named colors see: 
# http://arcade.academy/arcade.color.html 
# Colors can also be specified in (red, green, blue) format and # (red, green, blue, alpha) format.

arcade.set_background_color(arcade.color.BLUE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Draw the face
x1 = 300
y1 = 500
x2 = 500
y2 = 100
x3 = 100
y3 = 100

arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, arcade.color.YELLOW)

# Draw the right eye
x = 350
y = 300
radius = 20

arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the left eye
x = 250
y = 300
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)



# Draw the smile
x = 300
y = 260
width = 50
height = 50
start_angle = 190
end_angle = 350 
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

# Draw the smile
x = 300
y = 280
width = 60
height = 50
start_angle = 210
end_angle = 330
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)




# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()


