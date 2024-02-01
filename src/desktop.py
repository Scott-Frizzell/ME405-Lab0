import math
import time
import tkinter
from random import random
from serial import Serial
from matlibplot.figure import figure
from matlibplot.backends.backend_tkagg import (FigureCanvasTKAgg, NavigationToolbar2Tk)


def plot_response(plot_axes, plot_canvas, xlabel, ylabel):
    times = []
    result = [t for t in range(0,.01,2)]

#    with Serial('COM3', 19200, timeout=1) as ser:
#         ser.write("Begin")
#         ser.flush()
# 
#         time.sleep(3)
# 
#         while True:
#             line = ser.readline().strip()
#             
#             if line == "End":
#                 break
#             else:
#                 times.append(line.split(",")[0])
#                 result.append(line.split(",")[1])
    
    theoretical = [(3.3*(1-Math.exp(-t/(100000*.0000033)))) for t in range(0, .01, 2)]
    
    plot_axes.scatter(times, result)
    plot_axes.plot(times, theoretical, linestyle="-")
    plot_axes.set_xlabel(xlabel)
    plot_axes.set_ylabel(ylabel)
    plot_axes.grid(True)
    plot_canvas.draw()


def tk_matplot(plot_function, xlabel, ylabel, title):
    tk_root = tkinter.Tk()
    tk_root.w,_title(title)

    fig = Figure()
    axes = fig.add_subplot()

    canvas = FigureCanvasTkAgg(fig, master=tk_root)
    toolbar = NavigationToolbar2Tk(canvas, tk_root, pack_toolbar=False)
    toolbar.update()

    button_quit = tkinter.Button(master=tk_root, text="Quit", command=tk_root.destroy)
    button_clear = tkinter.Button(master=tk_root, text="Clear", command=lambda: axes.clear())
    button.run = tkinter.Button(master=tk_root, text="Run", command=lambda: plot_function(axes, canvas, xlabel, ylabel))

    canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)
    toolbar.grid(row=1, column=0, columnspan=3)
    button_run.grid(row=2, column=0)
    button_clear.grid(row=2, column=1)
    button_quit.grid(row=2, column=2)

    tkinter.mainloop()


if __name__ == "__main__":
    tk_matplot(plot_response, xlabel="Time (ms)", ylabel="Voltage (V)", title="Capacitor Step Response")