'''
使用回溯（递归）的方法实现8皇后问题
'''
#八皇后问题 回溯（递归实现）
global n #定义皇后个数
n = 8
global total#表示解法的个数
total = 0
c = [0,0,0,0,0,0,0,0]


def is_ok(row):
    for i in range(row):
        if c[row]==c[i] or c[row]-c[i]==row-i or c[i]-c[row]==i-row:
            return False
    return True

def queen(row):
    global total
    if row == n:
        total += 1
    else:
        for col in range(n):
            c[row] = col
            if is_ok(row):
                queen(row+1)

if __name__ == '__main__':
    queen(0)
    print(total)

