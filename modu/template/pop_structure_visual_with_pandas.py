import matplotlib.pyplot as plt
import csv
import pandas as pd

class Population(object):

    data: [] = list()

    def read_data(self):
        df = pd.read_csv('./data/202106_202106_연령별인구현황_월간.csv', encoding='UTF-8', thousands = ',')
        df.to_csv('./data/202106_202106_연령별인구현황_월간_without_comma.csv', sep=',', na_rep='NaN')
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간_without_comma.csv', 'rt', encoding='UTF-8'))
        next(data)
        print([i for i in data])
        self.data = data

    def pop_per_dong(self, dong: str) -> []:
        # [주의 ]csv reader 는 1회 이상 사용하면 GC 가 제거한다
        # print([i for i in self.data])
        arr = []
        [arr.append(int(j)) for i in self.data if dong in i[0] for j in i[3:]]
        print('*'*100)
        print([i for i in arr])
        return arr

    def show_plot(self, arr: []):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()




if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    # pop.show_plot(pop.pop_per_dong('역삼2동'))