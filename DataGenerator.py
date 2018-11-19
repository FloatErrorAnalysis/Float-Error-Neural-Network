import os


class DataGenerator:
    CMD0 = 'cd dataset'
    CMD1 = 'clang -S -emit-llvm /tmp/pycharm_project/tmp/LLVM/cpp_files/'
    CMD2 = ' -S -o /tmp/pycharm_project/tmp/LLVM/dataset/'

    def generate_ll(self):
        for cpp in self.list_file_names():
            cmd = self.CMD1 + cpp + self.CMD2 + cpp.split('.')[0] + '.ll'
            os.system(cmd)

    @staticmethod
    def list_file_names():
        names = []
        for root, dirs, files in os.walk('cpp_files'):
            for file in files:
                if os.path.splitext(file)[1] == '.cpp':
                    names.append(file)
        return names


generator = DataGenerator()
generator.generate_ll()
