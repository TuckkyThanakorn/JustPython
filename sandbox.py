from tkinter import *

root = Tk()
frame = Frame(root, border="5", relief=GROOVE, padx=10, pady=10)
frame.pack()
redbutton = Button(frame, text="Red", fg="red")
redbutton.pack(side = LEFT)
brownbutton = Button(frame, text="Brown", fg="brown")
brownbutton.pack(side = RIGHT)
bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack(side = BOTTOM)

bottomframe = Frame(root, bd="3", relief=GROOVE, padx=10, pady=10)
bottomframe.pack(side = BOTTOM)
blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack(side = BOTTOM)

root.mainloop()
