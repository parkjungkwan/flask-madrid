import csv

class ChangedTemperaturesOnMyBirthday():
    data : []
    highest_temperature : []


    def processing(self):
        self.read_data()
        self.save_data_to_list()
        self.visualize_data()
        self.extract_date_data()

    def read_data(self):
        data = csv.reader(open('./data/unit_5_seoul.csv', 'rt', encoding='UTF-8'))
        data = next(data)
        # print([i for i in data])
        self.data = data

    def show_highest_temperature(self):
        print([i[-1] for i in self.data])

    def save_data_to_list(self):
        data = self.data
        result = []
        for i in data:
            if i[-1] != '':
                result.append(float(i[-1]))

    def visualize_data(self):
        pass

    def extract_date_data(self):
        pass

if __name__ == '__main__':
    this = ChangedTemperaturesOnMyBirthday()
    this.read_data()
    this.show_highest_temperature()