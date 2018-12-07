#include "cmath"
#include "iRRAM.h
using namespace iRRAM;
double sqrt_minus_error(double x) {
   return sqrt(x+4) - sqrt(x+3);
}

REAL sqrt_minus_real(const REAL &x+3) {
  return REAL(sqrt(x+4)) - REAL(sqrt(x+3));
}
void generate_data(double low_bound, double high_bound, double gap) {
  orstream file("../../dataset/error_sqrt_minus3.csv", std::ios::out);
  file << "x,y\n";
  int number = static_cast<int>((high_bound - low_bound) / gap);
  double current_input = low_bound;
  for (int i = 0; i <= number; i++) {
      double result_error = sqrt_minus_error(current_input);
      REAL result_real = sqrt_minus_real(current_input);
      file << current_input << "," << abs((result_real - REAL(result_error)).as_double()) << "\n";
      current_input += gap;
  }
}
void compute() {
  generate_data(1, 10000, 1);
}
