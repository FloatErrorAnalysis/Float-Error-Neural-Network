from bitstring import BitArray
from py.util.data_generator import get_top5

with open('../cpp_bc/sqrt_minus1.bc', 'rb') as f:
    data = f.read()
    print(data)
   # print(bytes(int(data[i: i + 8], 2) for i in range(0, len(data), 8)))

with open('../cpp_bc/sqrt_minus2.bc', 'rb') as f:
    data1 = f.read()
    print(data1.hex())


print(get_top5())