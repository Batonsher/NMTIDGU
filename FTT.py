"""
FTT
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
            'm':  tkinter.DoubleVar(value=9.1e-31),
            'e':  tkinter.DoubleVar(value=1.6e-19),
            'pi': tkinter.DoubleVar(value=pi),
            'h':  tkinter.DoubleVar(value=1.06e-34),
            # 'd':  tkinter.DoubleVar(value=5e-9),
            # 'Eg': tkinter.DoubleVar(value=0.414),
        }

        self.v = {              # VARIABLES
            'd':  (tkinter.DoubleVar(value=1e-9),
                   tkinter.DoubleVar(value=1e-8),
                   tkinter.IntVar(value=100)),
            'Em':  (tkinter.DoubleVar(value=.0),
                    tkinter.DoubleVar(value=0.004),
                    tkinter.IntVar(value=4))
            }
        self.grid(row=0, column=0)

        self.gui()
        self.calc_button()

    def func(self, d, Em):
        n, m, e, h = self.c['n'].get(), self.c['m'].get(), self.c['e'].get(), \
                        self.c['h'].get()

        ans = Em + (pi * n * h)**2 / (2 * 1.08 * m * e * d**2)
        # print(f"{ans:2.2f}")

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
        tkinter.Label(self.frame, text="el.soni").grid(row=r, column=3)
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
        import numpy as np

        tkinter.Label(self.parent, text=self.title).grid(row=0, column=6)

        figure2 = plt.Figure(figsize=(6, 5), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self.parent)
        line2.get_tk_widget().grid(row=1, column=6, rowspan=12,
                                   padx=10, pady=10, )  # sticky='nwse')


        # ax2.set_title('AlGaAs 2D')
        ax2.set_xlabel('d')
        ax2.set_ylabel('E')

        # x = list(range(self.v['B'][0].get(), self.v['B'][1].get()+1, self.v['B'][2].get()))
        x = np.linspace(self.v['d'][0].get(), self.v['d'][1].get(), self.v['d'][2].get())
        Em = np.linspace(self.v['Em'][0].get(), self.v['Em'][1].get(), self.v['Em'][2].get())
        # Em = [0.0, 0.01, 0.02, 0.03]
        for q in Em:

            y = []
            for el in range(len(x)):
                y.append(self.func(x[el], q))
            # for d in x:
            #     y.append(self.func(d, q))

            ax2.plot(x, y, label=f"Em={q:1.4f}")
            # print("x=", x)
            # print(Em)

        ax2.legend(loc='best', bbox_to_anchor=(0.5, 1.1),
                   ncol=1, fancybox=True, shadow=True)
        ax2.set_ylim([4e-5, 4e-2])
        print('CALC')
        """best
        upper right
        upper left
        lower left
        lower right
        right
        center left
        center right
        lower center
        upper center
        center"""
        pass


if __name__ == '__main__':
    win = tkinter.Tk()

    calc = Calculator(win, 'Si/Si(1-x)Ge(x)Si')

    win.mainloop()

