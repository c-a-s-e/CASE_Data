import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    time = []
    acceleration = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row)
            time.append(int(row[0]))
            acceleration.append(float(row[1]))
            line_count += 1
    time = np.array(time)
    acceleration = np.array(acceleration)
    time = time - min(time)
    time = time / 1000
    velocity = integrate.cumtrapz(acceleration, time)
    distance = integrate.cumtrapz(velocity, time[:-1])
    plt.plot(time, acceleration, '-b')
    plt.plot(time, acceleration, 'ro', markersize=3)
    plt.xlabel("time (s)")
    plt.ylabel("z-acceleration (m/s^2)")
    plt.savefig("accel.png")
    plt.show()
    plt.figure()
    plt.plot(time[:-1], velocity, '-g')
    plt.xlabel('time (s)')
    plt.ylabel('velocity (m/s)')
    plt.savefig("velocity.png")
    plt.show()
    plt.figure()
    plt.plot(time[:-2], distance, '-b')
    plt.xlabel('time (s)')
    plt.ylabel('depth (m)')
    plt.savefig('distance.png')
    plt.show()
    print(f'Processed {line_count} lines.')
