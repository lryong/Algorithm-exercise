// 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

class Solution:
  public:
  double Power(double base, int exponet) {
  long long p = abs((long long)exponet);
  double r = 1.0;
  while(p) {
    if(p & 1) r*=base;
    base *= base;
    p >>= 1;
  }
  return n>=0?res:(1/res);
}
