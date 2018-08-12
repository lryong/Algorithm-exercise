
public void reOrderArray(int [] a) {
  if (a == null || a.length == 0)
    return;
  int i = 0,j;
  while(i < a.length) {
    while(i < a.length && !isEven(a[i]))
      i++;
    j = i +1;
    while (j < a.length && isEven(a[j]))
      j++;
    if(j<a.length) {
      int tmp = a[j];
      for ( int j2 = j-1; j2 >= i;j2--) {
	a[j2+1] a[j2];
      }
      a[i++] = tmp;
    } esel {
      break; // 查找失败
    }
  }
}

boolean isEven(int n) {
  if (n%2 == 0) {
    return true;
  }
  return false;
}
