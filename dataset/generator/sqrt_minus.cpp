//
// Created by py on 2018/11/13.
//
#include "iRRAM.h"

const double start = 10e7;
const double gap = 10000;
using namespace iRRAM;

double usual_sqrt_minus(double x) {
    return sqrt(x + 1) - sqrt(x);
}

REAL sqrt_minus(REAL x) {
    return REAL(1) / (REAL(sqrt(x + 1)) + REAL(sqrt(x)));
}

double error(double x) {
    return abs(sqrt_minus(x)- REAL(usual_sqrt_minus(x))).as_double();

}


void compute() {
    orstream file("../dataset/sqrt_minus.csv", std::ios::out);
    file << "x,error\n";

    for(double i = 0; i < 10e4; i += 1) {
        //    cout << i << ' ' << error(i) << "\n";
            file << i << "," << error(i) << "\n";
    }

}