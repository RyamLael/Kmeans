import matplotlib.pyplot as plt
import random

x = []
y = []

for _ in range (1000):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))

    plt.xlim(0,100)
    plt.ylim(0,100)

    plt.scatter(x, y, color= 'black')
    plt.pause(0.001)
