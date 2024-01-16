"""! @file main.py

"""

import pyb
import cqueue

pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP) # Initialize C0 as output
pinC0.low() # Set C0 to low
adc0 = pyb.ADC(pyb.Pin.board.PB0) # Initialize B0 as ADC input
timer = pyb.Timer(1, freq=100) # Initialize timer channel 1 to 100Hz (10ms)
timer.callback(None) # Set TC1 to have no callback
int_queue = cqueue.IntQueue(200) # Initialize a queue to store ADC readings

def step_response():
    """!
    
    @returns None
    """
    pinC0.high() # Set C0 to high
    timer.counter(0) # Reset TC1 counter
    timer.callback(timer_int) # Set TC1 callback to timer_int()
    
    while not int_queue.full(): # Wait until queue is full
        pass
    
    timer.callback(None) # Clear TC1 callback
    
    for i in range(int_queue.available()):
        print("{:d},{:d}".format(i * 10, int_queue.get())) # For each reading in the queue, print comma-separated time and value
    
    print("End") # Print end to indicate function is finished
    
    return

def timer_int(channel):
    """!
    
    @param channel The timer channel that called the function
    @returns None
    """
    if channel == 1:
        int_queue.put(adc0.read())
    return

if __name__ == "__main__":
    step_response()