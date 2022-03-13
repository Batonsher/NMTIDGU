"""
AlGaAs/GaAs/AlGaAs

restart; n:=1; m:=0.067*9.1e-31; e:=1.6e-19; pi:=3.14; h:=1.06e-34;
d:=12e-9;

E:=proc(B,N,d);
h*B*(N+0.5)/m+pi^2*h^2*n^2/(2*m*e*d^2);
end proc:

plot3d([E(B,0,d), E(B,1),E(B,2),E(B,3),E(B,4)],
B=0..20,
d=2..12,
numpoints=100,
linestyle=[1,1,1,1,1],
thickness=2, color=[blue,red,green,black,pink]);
"""

import tkinter
from math import pi


class DisabledEntry(tkinter.Entry):
    def __init__(self, parent, text="", *args, **kwargs):
        tkinter.Entry.__init__(self,parent, *args, **kwargs)
        if type(text) != str(123): text = str(text)
        self.insert(0, text)
        self.config(state=tkinter.DISABLED)



class Calculator(tkinter.Frame):
    def __init__(self, parent=None, **kwargs):
        tkinter.Frame.__init__(self, parent, **kwargs)

        self.frame = tkinter.Frame(parent).pack(fill=tkinter.Y)

        self.c = {              # CONSTANTS
            'pi': tkinter.DoubleVar(value=pi),
            'n' : tkinter.IntVar(value=1),
            'm' : tkinter.DoubleVar(value=0.067*9.1*10**-31),
            'e' : tkinter.DoubleVar(value=1.6*10**-19),
            'h' : tkinter.DoubleVar(value=1.06*10**-34),
            'd' : tkinter.DoubleVar(value=12*10**-9),
        }
        self.w = {              # WIDGETS
        }

    def func(self, B, N, d):
        n, m, e, h, d = self.c['n'].get(), self.c['m'].get(), self.c['e'].get(), \
                        self.c['h'].get(), self.c['d'].get()

        ans = h * B * (N + 0.5) / m * pi**2 * \
              h**2 * n**2 / (2*m * e * d**2)
        return ans

    def gui(self):

        tkinter.Label(self.frame, text="CONSTANTS").pack(side=tkinter.TOP)
        for key in self.c.keys():
            frm = tkinter.Frame()
            tkinter.Label(frm, text=key, width=3).pack(side=tkinter.LEFT)
            DisabledEntry(frm, text=self.c[key].get()).pack(side=tkinter.RIGHT, fill=tkinter.X)
            # tkinter.Entry(frm, textvariable=self.c[key]).pack(side=tkinter.RIGHT, fill=tkinter.X)
            # self.w[key] = tkinter.Button(frm).pack(side=tkinter.RIGHT)
            frm.pack(side=tkinter.TOP)

        pass


win = tkinter.Tk()
calc = Calculator(win)
print(calc.func(1, 2, 3))
calc.gui()
win.mainloop()
