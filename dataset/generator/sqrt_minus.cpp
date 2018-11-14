//
// Created by py on 2018/11/13.
//

// cd /root/tmp/examples/
#include "iRRAM.h"

const double gap = 10000;
using namespace iRRAM;
orstream file("../dataset/sqrt_minus.csv", std::ios::app);

double usual_sqrt_minus(double x) {
    return sqrt(x + 1) - sqrt(x);
}

REAL sqrt_minus(REAL x) {
    return REAL(1) / (REAL(sqrt(x + 1)) + REAL(sqrt(x)));
}

double error(double x) {
    return abs(sqrt_minus(x)- REAL(usual_sqrt_minus(x))).as_double();

}

void generate_data(int count) {
    for(double i = count * gap; i < (count + 1) * gap; i++) {
        file << i << "," << error(i) << "\n";
    }
    cout << "Part " << count << " finished..." << "\n";
}


void compute() {
    file << "x,error\n";
    // 极限是400次，多次执行获取数据
    for(int i = 0; i < 400; i++) {
        generate_data(i);
    }




}