import os
import csv
import operator
import numpy as np
from py.util.BCTool import generate_bytecode

cpp_dir_path = '/root/tmp/sqrt_minus_raw'
ll_dir_path = '/root/tmp/sqrt_minus_raw/ll'
bc_dir_path = '/root/tmp/sqrt_minus_raw/bc'


def generate_ll():
    lls = []
    generate_bytecode(cpp_dir_path)
    for ll in sorted(os.listdir(ll_dir_path)):
        with open(ll_dir_path + '/' + ll, 'rb') as f:
            byte = f.read(1)
            bytes = []
            while byte:
                byte = f.read(1)
                bytes.append(byte)
            lls.append(bytes)

    return lls


def generate_error():
    error_list = []
    for i in range(1, 31):
        f = str(i) + '.csv'
        print(f)
        error_list.append(get_top5(f))
    return error_list


def get_top5(csv_name):
    reader = csv.reader(open('/root/tmp/dataset/' + csv_name), delimiter=',')
    data_list = dict(reader)
    for k, v in data_list.items():
        data_list[k] = float(v)
    sorted_list = sorted(data_list.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_list[:5]


def read_data():
    lls = generate_ll()
    errors = generate_error()
    print('Length of ll: ' + str(len(lls)))
    lls = np.array(lls)
    errors = np.array(errors)
    print('The length of error: ' + str(len(errors)))
    print("shape of lls: {}\tshape of errors: {}".format(lls.shape, errors.shape))
    return lls, errors


if __name__ == '__main__':
    generate_ll()
