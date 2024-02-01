"""!
@file main.py
Tests input and output of the Nucleo board with a capacitive step response.
"""

import pyb
import cqueue
import time

pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP) # Initialize C0 as output
pinC0.low() # Set C0 to low
adc0 = pyb.ADC(pyb.Pin.board.PB0) # Initialize B0 as ADC input
timer = pyb.Timer(1, freq=100) # Initialize timer channel 1 to 100Hz (10ms)
timer.callback(None) # Set TC1 to have no callback
queue = cqueue.IntQueue(200) # Initialize a queue to store ADC readings

def step_response():
    """!
    Enables timer interrupts and begins a step response. After the response is done, prints each value.
    @returns None
    """
    timer.counter(0) # Reset TC1 counter
    timer.callback(timer_int) # Set TC1 callback to timer_int()
    time.sleep(.02) # Read first two data points as zero
    pinC0.high() # Set C0 to high
    
    while not queue.full(): # Wait until queue is full
        pass
    
    for i in range(queue.available()):
        print(f"{(i * 10)},{queue.get() * 3.3 / 4095}") # For each reading in the queue, print comma-separated time and value
    
    print("End") # Print end to indicate function is finished

    pinC0.low() # Reset C0 to low

    return

def timer_int(channel):
    """!
    Puts the value from adc0 into the queue. If the queue is full, it removes the callback function.
    @param channel The timer channel that called the function
    @returns None
    """
    queue.put(adc0.read())
    
    if  queue.full():
        timer.callback(None) # Clear TC1 callback
    return

if __name__ == "__main__":
    step_response()