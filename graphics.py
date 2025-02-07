from tkinter import Tk, BOTH, Canvas, Button

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("aMAZing")
        self.__canvas = Canvas(self.__root, width = width, height = height)
        self.__canvas.pack()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self._draw_button = Button(self.__root, text="Draw Maze", state="normal")
        self._solve_button = Button(self.__root, text = "Solve Maze", state = "disabled")
        self._draw_button.pack()
        self._solve_button.pack()

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__root.mainloop()

    def close(self):
        self.__canvas.quit()
    
    def draw_line(self, line, fill_color="black"):
        return line.draw(self.__canvas, fill_color)
    
    def delete_line(self, line_id):
        self.__canvas.delete(line_id)
    
    def delay(self, delay_ms, callback):
        self.__root.after(delay_ms, callback)
    
    def set_draw_command(self, command):
        self._draw_button.config(command=command)
    
    def set_solve_command(self, command):
        self._solve_button.config(command=command)
    
    def enable_solve_button(self):
        self._solve_button.config(state="normal")
    
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color = "black"):
        return canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
            )