'''
使用递归的几种情况
（1）指数函数
（2）优化的指数函数
（3）判断回文字符串
（4）二分查找
（5）选择子集和
'''

import time

# 使用递归的几种情况：

# (1)指数函数
def power(n, k):  # 计算n的k次方
    # 边界条件 当k减少到0的时候
    if k == 0:
        return 1
    else:
        return n * power(n, k - 1)


# (2)优化的指数函数
def power_optimize(n, k):
    if k == 0:
        return 1
    else:
        half = power_optimize(n, k // 2)
        if k % 2 == 0:
            return half * half
        else:
            return n * half * half


# (3)判断回文字符串
def loop_str(s):
    if len(s) <= 1:  # 边界条件
        return True
    else:
        return s[0] == s[-1] and loop_str(s[1:-1])


# (4)二分查找
def binary_search(s, start, end, value):
    # 边界条件
    if start > end:
        return -1
    else:
        mid = (end + start) // 2
        if s[mid] == value:
            return mid
        elif s[mid] < value:
            return binary_search(s, mid + 1, end, value)
        else:
            return binary_search(s, start, mid-1, value)

# (5)统计子集个数
#一共要选4个人，假设有一个Bob，可以分为选中Bob和没选中Bob两种情况
def C(n,k):#从n个人中选择k个人
    if k==0 or k==n:
        return 1
    else:
        return C(n-1,k)+C(n-1,k-1)


if __name__ == '__main__':
    time_a = time.time()
    print(power(5, 11))
    time_b = time.time()
    print('%fms' % ((time_b - time_a) * 1000))
    time_a = time.time()
    print(power_optimize(5, 11))
    time_b = time.time()
    print('%fms' % ((time_b - time_a) * 1000))
    print(loop_str('abcb'))
    print(binary_search([1,3,5,7,9],0,4,5))
    print(C(8,4))
