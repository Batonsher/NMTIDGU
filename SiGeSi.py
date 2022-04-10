"""
Si/Si(1-x)Ge(x)Si
"""

import tkinter
from math import pi


class DisabledEntry(tkinter.Entry):
    def __init__(self, parent, text="", *args, **kwargs):
        tkinter.Entry.__init__(self, parent, *args, **kwargs)
        if type(text) != str(123): text = str(text)
        self.insert(0, text)
        self.config(state=tkinter.DISABLED)


class Calculator(tkinter.Frame):
    def __init__(self, parent=None, title='untitled', **kwargs):
        tkinter.Frame.__init__(self, parent, **kwargs)

        self.title = title

        self.parent = parent
        self.parent.title("Namangan Engineering Technological Institute: IT: Drawer: " + title)
        self.parent.bind('<Return>', self.calc_button)

        self.free_row = 0
        self.frame = tkinter.Frame(self, bg="green").grid(row=0, column=0)

        self.c = {              # CONSTANTS
            'n':  tkinter.IntVar(value=1),
            'm':  tkinter.DoubleVar(value=9.828e-31),
            'e':  tkinter.DoubleVar(value=1.6e-19),
            'pi': tkinter.DoubleVar(value=pi),
            'h':  tkinter.DoubleVar(value=1.06e-34),
            'd':  tkinter.DoubleVar(value=5e-9),
            # 'Eg': tkinter.DoubleVar(value=0.414),
        }

        self.v = {              # VARIABLES
            'B':  (tkinter.IntVar(value=0), tkinter.IntVar(value=10), tkinter.IntVar(value=2)),
            'N':  (tkinter.IntVar(value=0), tkinter.IntVar(value=4), tkinter.IntVar(value=1)),
            }
        self.grid(row=0, column=0)

        self.gui()
        self.calc_button()

    def func(self, B, N):
        n, m, e, h, d = self.c['n'].get(), self.c['m'].get(), self.c['e'].get(), \
                        self.c['h'].get(), self.c['d'].get()

        ans = h * B * (N + .5) / m + (self.c['pi'].get() * h * n) ** 2 / (2 * m * e * d**2)

        return ans

    def gui(self):
        tkinter.Label(self.frame, text="O'zgarmas qiymatlar",
                      relief=tkinter.GROOVE).grid(row=0, column=0,
                                                  columnspan=4, sticky='ew',
                                                  pady=(30, 1), padx=(10, 0))
        r = 1
        for key in self.c.keys():
            frm = tkinter.Frame(self.frame)
            tkinter.Label(frm, text=key, width=4).grid(row=r, column=0)
            DisabledEntry(frm, text=self.c[key].get()).grid(row=r, column=1, columnspan=3)
            frm.grid(row=r, column=0, columnspan=4, sticky=tkinter.W)
            r += 1

        tkinter.Label(self.frame, text="O'zgaruvchi qiymatlar",
                      relief=tkinter.GROOVE).grid(row=r, column=0,
                                                  columnspan=4, sticky='ew',
                                                  pady=(30, 1), padx=(10, 0)
                                                  )
        r += 1
        tkinter.Label(self.frame, text="dan").grid(row=r, column=1)
        tkinter.Label(self.frame, text="gacha").grid(row=r, column=2)
        tkinter.Label(self.frame, text="qadam").grid(row=r, column=3)
        r += 1
        for key in self.v.keys():
            frm = tkinter.Frame(self.frame)

            tkinter.Label(frm, text=key, width=4).grid(row=r, column=0)
            for c in range(1, 4):
                tkinter.Entry(frm, textvariable=self.v[key][c-1], width=6).grid(row=r, column=c)

            frm.grid(row=r, column=0, columnspan=4)
            r += 1
        tkinter.Button(self.frame, command=self.calc_button, bg='#66FF66',
                       text='Hisobla').grid(row=r, column=0, columnspan=4,
                                            sticky='we', padx=20, pady=(20, 2))

        self.free_row = r + 1

    def calc_button(self, event=None):
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        tkinter.Label(self.parent, text=self.title).grid(row=0, column=6)

        figure2 = plt.Figure(figsize=(6, 5), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self.parent)
        line2.get_tk_widget().grid(row=1, column=6, rowspan=12,
                                   padx=10, pady=10, )  # sticky='nwse')

        # ax2.set_title('AlGaAs 2D')
        ax2.set_xlabel('Magnit maydon (B)')
        ax2.set_ylabel('Funksiyaning qiymati')

        x = list(range(self.v['B'][0].get(), self.v['B'][1].get()+1, self.v['B'][2].get()))

        for N in range(
                self.v['N'][0].get(),
                self.v['N'][1].get()+1,
                self.v['N'][2].get(),
                ):

            y = []
            for B in x:
                y.append(self.func(B, N))

            ax2.plot(x, y, label=str(N))

        ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
                   ncol=4, fancybox=True, shadow=True)
        # print('CALC')

        pass


if __name__ == '__main__':
    win = tkinter.Tk()

    calc = Calculator(win, 'Si/Si(1-x)Ge(x)Si')

    win.mainloop()

