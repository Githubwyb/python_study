#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import dsp as d

n1 = d.seq(-6, 10)
x1 = d.delta(-3, n1)
n2 = d.seq(-4, 2)
x2 = [5, 2, -3, 6, -7, 4, 9]
d.conv_m(x1, n1, x2, n2)
plt.show()