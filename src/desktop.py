import math
import time
import tkinter
from random import random
from serial import Serial
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def plot_response(plot_axes, plot_canvas, xlabel, ylabel):
    times = []
    result = []

    with Serial('COM5', 9600, timeout=1) as ser:
        ser.write("Begin\n".encode())
        ser.flush()

        time.sleep(3)

        while True:
            line = ser.readline().decode().strip()
            
            print(line)
            if line == "End":
                break
            else:
                times.append(float(line.split(",")[0])/1000)
                result.append(float(line.split(",")[1]))
    
    theoretical = [(3.3*(1-math.exp(-(t/100)/(100000*.0000033)))) for t in range(0,200)]
    
    plot_axes.scatter(times, result)
    plot_axes.plot(times, theoretical, linestyle="-")
    plot_axes.set_xlabel(xlabel)
    plot_axes.set_ylabel(ylabel)
    plot_axes.set_xticks([0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2])
    plot_axes.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5])
    plot_axes.grid(True)
    plot_canvas.draw()


def tk_matplot(plot_function, xlabel, ylabel, title):
    tk_root = tkinter.Tk()
    tk_root.wm_title(title)

    fig = Figure()
    axes = fig.add_subplot()

    canvas = FigureCanvasTkAgg(fig, master=tk_root)
    toolbar = NavigationToolbar2Tk(canvas, tk_root, pack_toolbar=False)
    toolbar.update()

    button_quit = tkinter.Button(master=tk_root, text="Quit", command=tk_root.destroy)
    button_clear = tkinter.Button(master=tk_root, text="Clear", command=lambda: axes.clear())
    button_run = tkinter.Button(master=tk_root, text="Run", command=lambda: plot_function(axes, canvas, xlabel, ylabel))

    canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)
    toolbar.grid(row=1, column=0, columnspan=3)
    button_run.grid(row=2, column=0)
    button_clear.grid(row=2, column=1)
    button_quit.grid(row=2, column=2)

    tkinter.mainloop()


if __name__ == "__main__":
    tk_matplot(plot_response, xlabel="Time (s)", ylabel="Voltage (V)", title="Capacitor Step Response")