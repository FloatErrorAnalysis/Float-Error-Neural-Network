import os
class CppGeneator:
    def generate_sqrt_minus(self):
        cpp_str_prefix = '#include \"cmath\" \nusing namespace std;\n' \
                   'double sqrt_minus(double x) {\n'
        cpp_str0 ='   return sqrt(x + 1) - sqrt(x);\n' \
        '}'
        file_path_prefix = '/tmp/pycharm_project/tmp/LLVM/cpp_files/sqrt_minus'
        # for i in range(0, 20):
        #    # os.mknod(file_path_prefix + str(i) + '.txt')
        #     with open(file_path_prefix + str(i) + '.cpp', 'w') as f:
        #         f.writelines()
        for i in range(1, 10):
            with open(file_path_prefix + str(i) + 'cpp', 'w') as f:
                f.writelines(cpp_str_prefix + cpp_str0.replace('x', str(i) + '*x'))
cpp_gen = CppGeneator()
cpp_gen.generate_sqrt_minus()