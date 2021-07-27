import random
# random.randint(1, 6)
# range(5)
import matplotlib.pyplot as plt

from modu.template import ChangedTemperaturesOnMyBirthday


def random_dice(count):
    ls = []
    [ls.append(random.randint(1, 6)) for i in range(count)]
    return ls

def show_hist(ls):
    plt.hist(ls, bins=6)
    plt.show()

def show_hist_about_highest_temperature(month: str):
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    # [print(i) for i in birth.data]
    arr = []
    '''
    for i in birth.data:
        if i[-1] != '':
            if i[0].split('-')[1] == '08':
                arr.append(float(i[-1]))
    '''
    [arr.append(float(i[-1])) for i in birth.data if i[-1] != ''  if i[0].split('-')[1] == month]
    plt.hist(arr, bins=100, color = 'r', label=f'{month} Month')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    # ls = random_dice(1000000)
    # print(ls)
    # show_hist(ls)
    show_hist_about_highest_temperature('01')