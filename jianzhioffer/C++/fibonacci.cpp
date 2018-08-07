// Fibonacci数列， 动态规划版本
class Solution {
public:
  int Fibonacci(int n)
  {
    int f = 0, g = 1;
    while(n--)
      {
	g += f;
	f = g -f;
      }
    return f;
  }
};
