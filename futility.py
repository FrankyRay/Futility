import tkinter as tk

class Futility:
    def __init__(self):
        self.bg_color = "#222222"
        self.fg_color = "#FFFFFF"

        self.window = tk.Tk()
        self.window.title("Futility")
        self.window.geometry(f"800x400+{int(self.window.winfo_screenwidth()/2-400)}+{int(self.window.winfo_screenheight()/2-250)}")
        self.window.config(background=self.bg_color)
        self.window.option_add("*Background", self.bg_color)
        self.window.option_add("*Foreground", self.fg_color)
        self.window.grid_columnconfigure(0, weight=1)

        # Run the program
        self.window.mainloop()


if __name__ == "__main__":
    Futility()