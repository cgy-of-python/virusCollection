import tkinter as tk
import tkinter.messagebox as tm
import random
def do_nothing(event):
        tm.showerror("Error", "The system is unresponsive. Please contact support. DO NOT RESTART YOUR COMPUTER OR YOU MAY LOSE DATA.")

def redboom(event):
    window = tk.Tk()
    window.overrideredirect(True)
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width-690)
    b = random.randrange(0, height-170)
    window.geometry("690x170" + "+" + str(a) + "+" + str(b))
    tk.Label(window, text='The system is unresponsive. Please contact support. \nDO NOT RESTART YOUR COMPUTER \nOR YOU MAY LOSE DATA.', bg='red',
             font=('system', 40), width=20, height=4).pack(fill=tk.BOTH, expand=True)
    window.protocol("WM_DELETE_WINDOW", do_nothing)
    window.mainloop()

def simulate_freeze():
    root = tk.Tk()
    root.overrideredirect(True)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.attributes('-topmost', True)
    root.attributes('-alpha', 0.01)
    root.configure(background='red')
    
    root.bind('<Button-1>', redboom)
    root.bind('<Button-2>', redboom)
    root.bind('<Button-3>', redboom)
    i=0.01
    step = 0.01
    while True:
        i += step
        if i >= 0.4:
             step = -0.0005
        elif i <= 0.01:
             step = 0.001    
        root.attributes('-alpha', i)    
        root.attributes('-topmost', True)
        root.update_idletasks()
        root.update()

if __name__ == "__main__":
    simulate_freeze()