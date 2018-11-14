import os


class DateGenerator:
    def __init__(self):
        print(os.getcwd())
        with open('../dataset/double_ll', 'r') as file:
            self.ll_key = file.read()

    def generate_real_vals(self):

