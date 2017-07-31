import turtle
turtle.shape('turtle')
square = turtle.clone()
square.shape('square')
square.pendown()
square.goto(100,0)
square.stamp()
square.goto(100,100)
square.stamp()
square.goto(0,100)
square.stamp()
square.goto(0,0)
triangle = turtle.clone()
triangle.shape('triangle')
triangle.goto(-100,0)
triangle.stamp()
triangle.goto(-100,100)
triangle.stamp()
triangle.goto(0,-10)
triangle.stamp()










turtle.mainloop()
