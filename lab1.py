import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

def put_pixel(canvas, x, y, color):
    canvas.create_rectangle((x, y, x+1, y+1), outline=color, fill=color)

def draw_circle(canvas, x0, y0, radius, color):
    x = radius
    y = 0
    err = 0

    while x >= y:
        put_pixel(canvas, x0 + x, y0 + y, color)
        put_pixel(canvas, x0 + y, y0 + x, color)
        put_pixel(canvas, x0 - y, y0 + x, color)
        put_pixel(canvas, x0 - x, y0 + y, color)
        put_pixel(canvas, x0 - x, y0 - y, color)
        put_pixel(canvas, x0 - y, y0 - x, color)
        put_pixel(canvas, x0 + y, y0 - x, color)
        put_pixel(canvas, x0 + x, y0 - y, color)

        y += 1
        if err <= 0:
            err += 2 * y + 1
        else:
            x -= 1
            err += 2 * (y - x) + 1

draw_circle(canvas, 200, 200, 70, 'red')

root.mainloop()
