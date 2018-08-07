#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
  int minNumberInRotateArray(vector<int> rotateArray) {
    int size = rotateArray.size();
    if (size == 0)
      {
	return 0;
      }
    int left = 0, right = size -1;
    int mid = 0;

    // 确保旋转
    while(rotateArray[left] > rotateArray[right])
      {
	if (left - right == 1)
	  {
	    min = right;
	    break;
	  }

	// 二分
	mid = left + (left + right) / 2;

	// 无法确定中间元素是属于前面的还是后面的递归子数组
	if (rotateArray[left] == rotateArray[right] && rotateArray[left] == rotateArray[mid])
	  {
	    return MinOrder(rotateArray, left, right);
	  }

	// 中间元素位于前面的递归子数组，此时最小元素位于中间元素的后面
	if (rotateArray[mid] >= rotateArray[left])
	  {
	    left = mid:
	  }
	else
	  {
	    right = mid;
	  }
      }
    return rotateArray[mid];
  }

private:
  // 顺序寻找最小值
  int MinOrder(vector<int> &num, int left, int right)
  {
    int result = num[left];
    for (int i = left + 1; i < right; ++i)
      {
	if (num[i] < result)
	  {
	    result = num[i];
	  }
      }
    return result;
  }
};


