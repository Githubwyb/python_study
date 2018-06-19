#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import math
import serial

myserial = serial.Serial()
myserial.port = 'COM10'
myserial.baudrate = 115200
#设置等待时间，若超出这停止等待
myserial.timeout = 2
myserial.open()
data = ''
dataGroup = ''
tempData = []
acceX = [0]
acceY = [0]
acceZ = [0]
offsetX = 0
offsetY = 0
offsetZ = 0
stateX = 0
stateY = 0
stateZ = 0
countX = 0
countY = 0
countZ = 0
sumX = 0
sumY = 0
sumZ = 0
if myserial.isOpen():
    print("serial open success")
    fig = plt.figure()
    plt.clf()
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)
    ax1.set_xlim(0, 99)
    ax2.set_xlim(0, 99)
    ax3.set_xlim(0, 99)

    ax1.set_ylim(-20, 20)
    ax2.set_ylim(-20, 20)
    ax3.set_ylim(-20, 20)

    line1, = ax1.plot(range(len(acceX)), acceX, c = 'r', marker = '.')
    line2, = ax2.plot(range(len(acceY)), acceY, c = 'g', marker = '.')
    line3, = ax3.plot(range(len(acceZ)), acceZ, c = 'b', marker = '.')
    while True:
        n = myserial.inWaiting()
        if n > 0:
            data += myserial.read(n).decode()
        if data.find(';') != -1:
            indexSplit = data.find(';')
            dataGroup = data[:indexSplit]
            data = data[indexSplit + 1:]
            tempData = dataGroup.split()

            if len(tempData) == 3:
                acceX.append(int(tempData[0]) / 256 - offsetX)
                acceY.append(int(tempData[1]) / 256 - offsetY)
                acceZ.append(int(tempData[2]) / 256 - offsetZ)

                if offsetX == 0:
                    sumX += int(tempData[0]) / 256
                    sumY += int(tempData[1]) / 256
                    sumZ += int(tempData[2]) / 256
                else:
                    if acceX[len(acceX) - 1] > 3 or acceX[len(acceX) - 1] < -3:
                        countX = countX + 1
                    if acceY[len(acceY) - 1] > 3 or acceY[len(acceY) - 1] < -3:
                        countY = countY + 1
                    if acceZ[len(acceZ) - 1] > 3 or acceZ[len(acceZ) - 1] < -3:
                        countZ = countZ + 1

                if len(acceX) > 100:
                    if offsetX == 0:
                        offsetX = sumX / 100
                        offsetY = sumY / 100
                        offsetZ = sumZ / 100

                    if acceX[len(acceX) - 21] > 3 or acceX[len(acceX) - 21] < -3:
                        countX = countX - 1
                    if acceY[len(acceY) - 21] > 3 or acceY[len(acceY) - 21] < -3:
                        countY = countY - 1
                    if acceZ[len(acceZ) - 21] > 3 or acceZ[len(acceZ) - 21] < -3:
                        countZ = countZ - 1

                    del acceX[0]
                    del acceY[0]
                    del acceZ[0]

                if countX > 5:
                    stateX = 2
                elif countX > 2:
                    stateX = 1
                else:
                    stateX = 0

                if countY > 5:
                    stateY = 2
                elif countY > 2:
                    stateY = 1
                else:
                    stateY = 0

                if countZ > 5:
                    stateZ = 2
                elif countZ > 2:
                    stateZ = 1
                else:
                    stateZ = 0

                line1.set_ydata(acceX)
                line1.set_xdata(range(len(acceX)))
                line2.set_ydata(acceY)
                line2.set_xdata(range(len(acceY)))
                line3.set_ydata(acceZ)
                line3.set_xdata(range(len(acceZ)))

                if stateX == 2 or stateY == 2 or stateZ == 2:
                    ax1.set_xlabel("move")
                elif stateX == 1 or stateY == 1 or stateZ == 1:
                    ax1.set_xlabel("vibrate")
                else:
                    ax1.set_xlabel("static")

                plt.pause(0.01)
else:
    print("serial open fail")
