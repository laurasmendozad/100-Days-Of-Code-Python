''' Function to find the coordinates for the map '''

import turtle

def get_mouse_click_coor(x,y):
    " Print the coordinates of the mouse click "
    print(x,y)

screen = turtle.Screen()
IMAGE = "departamentos_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
