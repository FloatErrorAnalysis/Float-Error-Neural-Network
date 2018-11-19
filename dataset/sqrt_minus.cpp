//
// Created by py on 2018/10/18.
//
#include "cmath"
#include <iostream>
#include <fstream>
using namespace std;
// sqrt(x + 1) - sqrt(x)
double sqrt_minus(double x) {
    return sqrt(x + 1) - sqrt(x);
}
bool is_zero(double x) {
    return sqrt_minus(x) != 0;
}


int main() {
    cout << sqrt_minus(1) << endl;
    return 0;
}
