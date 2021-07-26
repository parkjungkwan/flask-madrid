import csv
'''
next() 는 두가지 포맷으로 사용된다.
function 구조로 사용되면 header 만 리턴한다.
consumer 구조로 사용되면 data에서 header 를 제거한다.

row[날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃)] 최고기온은 -1 이다.

data : [] = list() 는 list 타입의 data 를 list() 로 초기화 시키는 것이다.
단, 한 메소드 내에서만 사용하면 로컬에서 초기화한다. 예제는 다음과 같다. 
data : [] = None
def save_highest_temperatures(self):
     data = list()
그러나, 여러 메소드에서 사용하면 필드에서 초기화한다. 예제는 다음과 같다. 
data : [] = list()
'''
class ChangedTemperaturesOnMyBirthday():

    data : [] = list()
    highest_temperatures: [] = list()


    def processing(self):
        self.read_data()
        self.save_data_to_list()
        self.visualize_data()
        self.extract_date_data()

    def read_data(self):
        data = csv.reader(open('./data/unit_5_seoul.csv', 'rt', encoding='UTF-8'))
        next(data)
        # print([i for i in data])
        self.data = data

    def show_highest_temperature(self):
        # print([i[-1] for i in self.data])
        return [i[-1] for i in self.data]

    def save_highest_temperatures(self):
        self.highest_temperatures.append([float(i[-1]) for i in self.data if i[-1] != ''])
        print(self.highest_temperatures)

    def visualize_data(self):
        pass

    def extract_date_data(self):
        pass

if __name__ == '__main__':
    this = ChangedTemperaturesOnMyBirthday()
    this.read_data()
    # this.show_highest_temperature()
    this.save_highest_temperatures()