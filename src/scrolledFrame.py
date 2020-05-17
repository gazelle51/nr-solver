import tkinter as tk


class Tkscrolledframe(tk.Frame):
    def __init__(self, container=None, **kwds):
        tk.Frame.__init__(self, container)
        self.no_hbar = False
        if "no_hbar" in kwds.keys():
            self.no_hbar = kwds["no_hbar"]
            kwds.pop("no_hbar")
        self.no_vbar = False
        if "no_vbar" in kwds.keys():
            self.no_vbar = kwds["no_vbar"]
            kwds.pop("no_vbar")
        self.canvas = tk.Canvas(self, **kwds)
        self.canvas.grid(row=0, column=0, sticky="nswe ")
        if not self.no_hbar:
            self.hscroll = tk.Scrollbar(
                self, orient=tk.HORIZONTAL, command=self.canvas.xview
            )
            self.hscroll.grid(row=1, column=0, sticky="we")
            self.canvas.configure(xscrollcommand=self.hscroll.set)
        if not self.no_vbar:
            self.vscroll = tk.Scrollbar(
                self, orient=tk.VERTICAL, command=self.canvas.yview
            )
            self.vscroll.grid(row=0, column=1, sticky="ns")
            self.canvas.configure(yscrollcommand=self.vscroll.set)
        self.frame = tk.Frame(self.canvas)

    def getFrame(self):
        """returns the frame where to place the graphic objects"""
        return self.frame

    def update(self):
        self.frame.update()
        self.canvas.create_window(0, 0, window=self.frame, anchor=tk.NW)
        self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))
