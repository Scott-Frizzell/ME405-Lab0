"""! @file main.py

"""

import pyb
from utime import sleepmillis
import cqueue

pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP)
adc0 = pyb.ADC(pyb.Pin.board.PB0)
int_queue = cqueue.IntQueue(10)

while True:
    pinC0.value(0)
    sleepmillis(5000)
    pinC0.value(1)
    step_response()
    sleepmillis(5000)

def step_response():
    i = 10
    while True:
        if  int_queue.any():
            temp = int_queue.get()
            if temp >= 3.3:
                print("End")
                break
            print("{:d},{:d}".format(i, temp))
            i += 10
    return

def timer_int():
    int_queue.put(adc0.read())
    return