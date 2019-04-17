import numpy as np
import sys

def load():
    try:
        data = np.genfromtxt(sys.argv[1], delimiter = ',')
    except:
        print("Error. Programm abort.")
        exit()
    return data

def ft_percentile(array, percent):
   lena = len(array)
   array.sort()
   n = lena * percent / 100
   return array[int(n)]

def ft_std(array, mean):
    lena = len(array) - 1
    suma = 0
    for elem in array:
        if np.isnan(elem) == False:
            suma += (elem - mean)**2
        else:
            lena -= 1
    std = (suma / lena)**0.5
    return std

def display_stat(stats):
    labels = ["", "Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
    columns, lines = np.shape(stats)
    for i in range(0, lines + 1):
        sys.stdout.write("%-8s" % labels[i])
        for j in range(0, columns):
            if i == 0:
                sys.stdout.write("%12s %2d " % ("Feature", j + 1))
            else:
                sys.stdout.write("%15.6f " % stats[j][i - 1])
        sys.stdout.write("\n")

def main():
    data = load()
    try:
        lines, columns = np.shape(data)
    except:
        print("Error. Programm abort.")
        exit()
    final_stat = []
    for i in range(0, columns):
        stats = np.zeros(8)
        stats[3] = np.inf
        stats[7] = -np.inf
        for j in range(0, lines):
            if (np.isnan(data[j][i]) == False):
                stats[0] += 1
                stats[1] += data[j][i]
                if data[j][i] < stats[3]:
                    stats[3] = data[j][i]
                if data[j][i] > stats[7]:
                    stats[7] = data[j][i]
                stats[4] = ft_percentile(data[:, i], 25)
                stats[5] = ft_percentile(data[:, i], 50)
                stats[6] = ft_percentile(data[:, i], 75)
        if stats[3] != np.inf:
            if stats[0] != 0:
                stats[1] = stats[1] / stats[0]
            stats[2] = ft_std(data[:, i], stats[1])
            final_stat.append(stats)
    display_stat(final_stat)

if __name__ == "__main__":
    main()
