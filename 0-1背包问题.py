#0-1背包问题（动态规划）

#初始化商品价值和重量以及背包的容量
#商品价值v
v = [0,60,100,120]  #商品价值
w = [0,1,2,3]       #重量
c = 5               #背包的容量


#二维数组f[i][j]表示在背包容量为j的条件下前i件物品的总价值
f = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]


#构建状态矩阵
for i in range(1,len(v)):           #外层循环控制物品的数量 确保每种物品都会被遍历到

    for j in range(1,c+1):          #内层循环遍历背包的容量 确保每种容量都被遍历到

        if j < w[i]:                #容量不足够装第i件商品的情况
            f[i][j] = f[i-1][j]
        else:
            x = f[i-1][j]           #将第i件物品不放入背包
            y = f[i-1][j-w[i]]+v[i] #将第i件物品放入背包
            f[i][j] = x if x>y else y

for i in range(len(f)):
    print(f[i])
print('最大价值是：%d' % f[len(v)-1][c])

#追踪解的过程

i = len(v)-1
j = c

while i:
    if f[i][j] == f[i-1][j-w[i]]+v[i]:
        print('%d weight:%d value:%d' % (i,w[i],v[i]))
        j -= w[i]
    i -= 1

