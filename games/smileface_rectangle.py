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
x = 300
y = 300
height =300
width = 300
tilt_angle = 0
arcade.draw_rectangle_filled(x, y,width ,height, arcade.color.YELLOW,tilt_angle)

# Draw the right eye
x = 350
y = 350
radius = 20

arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the left eye
x = 250
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the left Nostril
x = 290
y = 290
radius = 5
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)

# Draw the rght Nostril
x = 310
y = 290
radius = 5
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)


# Draw the smile
x = 300
y = 250
width = 50
height = 50
start_angle = 190
end_angle = 350 
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()


