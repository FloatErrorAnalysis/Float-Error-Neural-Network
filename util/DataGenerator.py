import os
import csv


class DataGenerator:
    def __init__(self):
        print(os.getcwd())
        self.data_list = []
        with open('../dataset/double_ll', 'r') as file:
            self.data_list.append(file.read())
        with open('/root/tmp/dataset/sqrt_minus.csv') as f:
            reader = csv.reader(f)
            error_list = list(reader)
            self.data_list.append(error_list)


generator = DataGenerator()
print(generator.data_list)


