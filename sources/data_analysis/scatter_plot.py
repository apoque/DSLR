#Answer is Astronomy and Defense Against the Dark Arts

import numpy as np
import matplotlib.pyplot as plt
import sys

def get_data():
    try:
        data = np.genfromtxt(sys.argv[1], delimiter = ',')
        data_str = np.genfromtxt(sys.argv[1], delimiter = ',', dtype = np.str)
    except:
        print("Error.Program abort.")
        exit()
    best_hand = np.where(data_str == "Best Hand")[1]
    data_str[np.where(data_str == "Left")[0], best_hand] = 1
    data_str[np.where(data_str == "Right")[0], best_hand] = 2
    data[1:, best_hand] = data_str[1:, best_hand]
    birthday = np.where(data_str == "Birthday")[1]
    for i in range(1, len(data_str)):
        nb_bday = data_str[i, birthday]
        data[i, birthday] = int(nb_bday[0][:4]) + \
                            (int(nb_bday[0][5:7]) / 120 * 10) + \
                            (int(nb_bday[0][8:9]) / 3100 * 10)
    return data, data_str

def get_col(data, data_str, column):
    rvc = np.array([])
    slr = np.array([])
    gfd = np.array([])
    hfpf = np.array([])
    for k in range(1, len(data)):
        if data_str[k, 1] == "Ravenclaw":
            rvc = np.append(rvc, data[k, column])
        elif data_str[k, 1] == "Slytherin":
            slr = np.append(slr, data[k, column])
        elif data_str[k, 1] == "Gryffindor":
            gfd = np.append(gfd, data[k, column])
        elif data_str[k, 1] == "Hufflepuff":
            hfpf = np.append(hfpf, data[k, column])
    return rvc, slr, gfd, hfpf

def main():
    data, data_str = get_data()
    colors = ['r', 'b', 'g', 'y']
    for i in range(4, data.shape[1]):
        for j in range(i + 1, data.shape[1]):
            for k in range (0, 4):
                plt.scatter(get_col(data, data_str, i)[k], \
                        get_col(data, data_str, j)[k], c = colors[k], \
                        edgecolors = "none", alpha = 0.8)
                plt.xlabel(data_str[0, i])
                plt.ylabel(data_str[0, j])
                plt.legend(["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"], \
                        fontsize = "small")
            plt.show()

if __name__ == "__main__":
    main()

