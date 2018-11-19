import os


class DataGenerator:
    CMD0 = 'cd dataset'
    CMD1 = 'clang -S -emit-llvm dataset/sqrt_minus.cpp'

    def generate_ll(self):
        os.system(self.CMD1)
        os.system(self.CMD)


generator = DataGenerator()
generator.generate_ll()
