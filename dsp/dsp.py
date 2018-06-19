#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

def seq(n0, n1):
    return list(range(n0, n1 + 1))

def delta(x, n):
    y = np.zeros(len(n))
    y[n.index(x)] = 1
    return y

def impseq(n0, n1, n2):
    n = seq(n1, n2)
    x = delta(n0, n)
    return x, n

def u(x, n):
    y = np.zeros(len(n))
    y[n.index(x) : ] = (len(n) - n.index(x)) * [1]
    return y

def stepseq(n0, n1, n2):
    n = seq(n1, n2)
    x = u(n0, n)
    return x, n

def reaction(b, a, x, n):
    y = signal.lfilter(b, a, x)
    plt.figure()

    plt.subplot(2, 1, 1)
    plt.stem(n, x)
    plt.title("x(n)")
    plt.xlabel("n")
    plt.ylabel("x(n)")

    plt.subplot(2, 1, 2)
    plt.stem(n, y)
    plt.title("The response of the system to x(n)")
    plt.xlabel("n")
    plt.ylabel("y(n)")

    plt.tight_layout()
    return y

def show(x, n):
    plt.figure()

    plt.subplot(2, 2, 1)
    plt.stem(n, x.real)
    plt.title("real part")
    plt.xlabel("n")
    plt.ylabel("Re[x(n)]")

    plt.subplot(2, 2, 2)
    plt.stem(n, x.imag)
    plt.title("imaginary part")
    plt.xlabel("n")
    plt.ylabel("Im[x(n)]")

    plt.subplot(2, 2, 3)
    plt.stem(n, abs(x))
    plt.title("amplitude")
    plt.xlabel("n")
    plt.ylabel("|x(n)|")

    plt.subplot(2, 2, 4)
    plt.stem(n, np.angle(x))
    plt.title("phase")
    plt.xlabel("n")
    plt.ylabel("ψ(n)")

    plt.tight_layout()
    return

def spReaction(b, a, n):
    x = delta(0, n)
    y1 = signal.lfilter(b, a, x)

    plt.figure()

    plt.subplot(2, 1, 1)
    plt.stem(n, y1)
    plt.title("impulse response")
    plt.xlabel("n")
    plt.ylabel("h(n)")

    x = u(0, n)
    y2 = signal.lfilter(b, a, x)

    plt.subplot(2, 1, 2)
    plt.stem(n, y2)
    plt.title("step response")
    plt.xlabel("n")
    plt.ylabel("s(n)")

    plt.tight_layout()
    return y1, y2

def conv_m(x1, n1, x2, n2):
    n = seq(n1[0] + n2[0], n1[len(n1) - 1] + n2[len(n2) - 1])
    y = signal.convolve(x1, x2)
    nt = seq(min(n + n1 + n2), max(n + n1 + n2))
    yt = np.zeros(len(nt))
    x1t = np.zeros(len(nt))
    x2t = np.zeros(len(nt))
    yt[nt.index(min(n)) : nt.index(max(n)) + 1] = y
    x1t[nt.index(min(n1)) : nt.index(max(n1)) + 1] = x1
    x2t[nt.index(min(n2)) : nt.index(max(n2)) + 1] = x2

    plt.figure()

    plt.subplot(3, 1, 1)
    plt.stem(nt, x1t)
    plt.title("x1")
    plt.xlabel("n")
    plt.ylabel("x1(n)")

    plt.subplot(3, 1, 2)
    plt.stem(nt, x2t)
    plt.title("x2")
    plt.xlabel("n")
    plt.ylabel("x2(n)")

    plt.subplot(3, 1, 3)
    plt.stem(nt, yt)
    plt.title("y")
    plt.xlabel("n")
    plt.ylabel("y(n)")

    plt.tight_layout()
    return y, n
