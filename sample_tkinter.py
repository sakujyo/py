# https://qiita.com/SquidSky/items/90eb450310f1697d03e9
# DO NOT NAME this file "tkinter.py"
import tkinter as tk

def bLeftClicked(canvas):
    #print(dir(canvas))
    canvas.delete("all")
    canvas.create_rectangle(80, 80, 400, 250, fill = 'green')
    #canvas.create_rectangle(80, 80, 400, 250, fill = 'green', stipple = 'gray25')
    print("bLeft Clicked")

def test_tkinter():
    print(dir(tk))
    root = tk.Tk()
    root.title("tkinter test")
    root.geometry("640x480")
    canvas = tk.Canvas(root, width=640, height=480)
    bLeft = tk.Button(root, text="to left", command=lambda: bLeftClicked(canvas))
    bLeft.grid()
    canvas.place(x=0, y=40)
    canvas.create_rectangle(80, 80, 250, 400, fill = 'green')
    root.mainloop()

if __name__ == '__main__':
    test_tkinter()
