import os
import csv


class DataGenerator:
    def __init__(self):
        print(os.getcwd())
        with open('../dataset/double_ll', 'r') as file:
            ll_file = file.read()
        with open('/root/tmp/dataset/sqrt_minus.csv') as f:
            reader = csv.reader(f)
            error_list = list(reader)
            self.data_dict = {ll_file: error_list}


# generator = DataGenerator()
# with open('../dataset/double_ll', 'r') as file:
#     ll_file = file.read()
# print(len(generator.data_dict[ll_file]))


