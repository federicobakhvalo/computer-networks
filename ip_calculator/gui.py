
import tkinter as tk
from tkinter import ttk, messagebox
from calculator import IPCalculator


class IPCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('IP Calculator')
        self.calc = IPCalculator()
        self._build()


    def _build(self):
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        ttk.Label(frm, text='IP / Prefix (10.1.33.133/25):').grid(column=0, row=0, sticky='w')
        self.entry = ttk.Entry(frm, width=30)
        self.entry.grid(column=0, row=1, sticky='w')

        self.compute_btn = ttk.Button(frm, text='Compute', command=self.on_compute)
        self.compute_btn.grid(column=0, row=2, pady=6, sticky='w')

        # Results
        self.net_var = tk.StringVar()
        self.brd_var = tk.StringVar()
        self.hosts_var = tk.StringVar()
        self.mask_var = tk.StringVar()



        ttk.Label(frm, text='Адрес сети:').grid(column=0, row=3, sticky='w')
        ttk.Label(frm, textvariable=self.net_var).grid(column=0, row=4, sticky='w')
        ttk.Label(frm, text='Широковещательный (broadcast):').grid(column=0, row=5, sticky='w')
        ttk.Label(frm, textvariable=self.brd_var).grid(column=0, row=6, sticky='w')
        ttk.Label(frm, text='Количество хостов : ').grid(column=0, row=7, sticky='w')
        ttk.Label(frm, textvariable=self.hosts_var).grid(column=0, row=8, sticky='w')
        ttk.Label(frm, text='Маска сети : ').grid(column=0, row=9, sticky='w')
        ttk.Label(frm, textvariable=self.mask_var).grid(column=0, row=10, sticky='w')

    def on_compute(self):
        inp = self.entry.get().strip()
        try:
            res = self.calc.compute(inp)
        except Exception as e:
            messagebox.showerror(title='Error', message=str(e))
            return
        self.net_var.set(res['network'])
        self.brd_var.set(res['broadcast'])
        self.hosts_var.set(res['hosts'])
        self.mask_var.set(res['mask'])



