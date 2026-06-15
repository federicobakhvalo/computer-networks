from gui import IPCalculatorApp
from tkinter import Tk


def run_app():
    root = Tk()
    app = IPCalculatorApp(root)
    root.mainloop()


if __name__ == '__main__':
    run_app()
