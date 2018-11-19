import os
class CppGeneator:
    def generate_sqrt_minus(self):
        cpp_str0 = '#include \"cmath\"\n' + \
                   '#include <iostream>\n' + \
                   '#include <fstream>\n' \
                   'using namespace std;\n'\
                    'int main() {\n'\
                   'cout << sqrt('
        cpp_str1 = ') - sqrt('
        cpp_str2 = ') << endl;\nreturn 0;\n}'

# '/tmp/pycharm_project/tmp/LLVM/cpp_files/'
        file_path_prefix = '/tmp/pycharm_project/tmp/LLVM/cpp_files/sqrt_minus'
        for i in range(0, 1000):
           # os.mknod(file_path_prefix + str(i) + '.txt')
            with open(file_path_prefix + str(i) + '.cpp', 'w') as f:
                f.writelines(cpp_str0 + str(i + 1) + cpp_str1 + str(i) + cpp_str2)

cpp_gen = CppGeneator()
cpp_gen.generate_sqrt_minus()