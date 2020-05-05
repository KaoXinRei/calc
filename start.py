import tkinter as tk
import Main


def main():
    application = tk.Tk()
    application.title("Calculator")
    application.resizable(width=False, height=False)
    application.configure(bg='white')
    Main.Window(application)
    application.mainloop()


main()
