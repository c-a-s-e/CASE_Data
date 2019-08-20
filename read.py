import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
import seaborn as sns


def smoothing(points, f=0.3):
    result = [points[0], ]
    for i in range(1, len(points) - 1):
        result.append(points[i - 1] * f / 2 + points[i] * (1 - f) + points[i + 1] * f / 2)
    result.append(points[len(points) - 1])
    return result


def transient_components_emphasizing(points, f=0.95):
    pre = points[0]
    result = [points[0], ]
    for i in range(1, len(points)):
        cur = f * (pre + points[i] - points[i-1])
        result.append(cur)
        pre = cur
    return result


sns.set()
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
    acceleration = smoothing(acceleration)
    time = time - min(time)
    time = time / 1000
    velocity = integrate.cumtrapz(acceleration, time)
    velocity = transient_components_emphasizing(velocity)
    distance = integrate.cumtrapz(velocity, time[:-1])
    distance = transient_components_emphasizing(distance)
    fig, (p1, p2, p3) = plt.subplots(1, 3, figsize=(15, 5))
    p1.plot(time, acceleration, '-')
    p1.plot(time, acceleration, 'o', markersize=3)
    p1.set_title('time (s) vs z-acceleration (m/s^2)')

    p2.plot(time[:-1], velocity, '-')
    p2.set_title('time (s) vs velocity (m/s)')

    p3.plot(time[:-2], distance, '-')
    p3.set_title('time (s) vs depth (m)')

    fig.savefig("full.png")
    fig.show()
    print(f'Processed {line_count} lines.')
