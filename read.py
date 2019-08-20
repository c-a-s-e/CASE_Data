import csv
import matplotlib.pyplot as plt
import numpy as np

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    time = []
    value = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row)
            time.append(int(row[0]))
            value.append(float(row[1]))
            line_count += 1
    time = np.array(time)
    value = np.array(value)
    time = time - min(time)
    plt.plot(time, value)
    plt.xlabel("time (ms)")
    plt.ylabel("z-acceleration (m/s^2)")
    plt.savefig("plot.png")
    plt.show()
    print(f'Processed {line_count} lines.')
