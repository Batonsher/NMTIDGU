from gui_classes import *
import tkinter
import matplotlib.pyplot as plt

win = tkinter.Tk()
f = tkinter.Frame(win, bd=10, bg="red").pack(side=tkinter.LEFT)
calc = Calculator(f)
calc.gui()
calc.pack(side=tkinter.LEFT, padx=10, pady=10, ipadx=20)
print(calc.func(1, 2, 3))
# f.pack(side=tkinter.LEFT)
tkinter.Label(win, text='asdasd').pack(side=tkinter.RIGHT)

################################################################
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

x = list(range(-50, 50))
y = [q**2 for q in x]

figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, win)
line2.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
ax2.plot(x, y)

ax2.set_title('Year Vs. Unemployment Rate')


win.mainloop()

