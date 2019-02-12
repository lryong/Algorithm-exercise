# -*- coding:utf-8 -*-
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        # B = [1]
        num = len(A)
        B = [None]*num
        B[0] = 1
    # B[i]的意义是A数组不包括i位置的所有乘积，分为 i左边的元素乘积和 i右边的所有元素乘积。第一个for计算i左边的乘积，第二个for计算右边的。初始化B[0]=1，是因为0左边没有元素，所以乘积为1。

        # 先计算左下部分
        for i in range(1,num):
            # 可以数学推导
            B[i]= A[i-1]*B[i-1]

        # 计算右上部分
        # 保留上次的计算结果乘本轮新的数,因为只是后半部分进行累加，所以设置一个tmp,能够保留上次结果
        tmp = 1
        for i in range(num-2,-1,-1):
            tmp *= A[i+1]
            B[i] *= tmp
        return B

def main():
    a = Solution()
    input1 = [1,3,6,7,9]
    ret = a.multiply(input1)
    print 'result is ',ret

main()
