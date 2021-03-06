#Answer is Arithmancy and Care of Magical Creatures

import numpy as np
import matplotlib.pyplot as plt
import sys

def get_data():
    try:
        data = np.genfromtxt(sys.argv[1], delimiter = ',')
        data_str = np.genfromtxt(sys.argv[1], delimiter = ',', dtype = np.str)
    except:
        print("Error. Program abort.")
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
    rvc = np.extract(np.isnan(rvc) == False, rvc)
    slr = np.extract(np.isnan(slr) == False, slr)
    gfd = np.extract(np.isnan(gfd) == False, gfd)
    hfpf = np.extract(np.isnan(hfpf) == False, hfpf)
    return rvc, slr, gfd, hfpf

def main():
    data, data_str = get_data()
    for i in range(4, data.shape[1]):
        plt.hist(get_col(data, data_str, i), bins = 15)
        plt.title(data_str[0, i])
        plt.legend(["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"],fontsize = "small")
        plt.show()

if __name__ == "__main__":
    main()
