import math
from matplotlib import pyplot

times = [n for n in range(200)]
boing = [math.sin(n)*math.exp(-n/7) for n in times]

pyplot.plot(times, boing)
pyplot.xlabel("Times (hours)")
pyplot.ylabel("Distance (furlongs)")
pyplot.show()