import numpy as np
import pivot as pt
#変数の初期化
eps=10**-6
m=0

#                1,2,3,4,5,6,7,8,9,0,1,2,b
data=np.array([[-4,1,0,1,0,0,0,0,0,0,0,0,-100],
               [1,-4,1,0,1,0,0,0,0,0,0,0,-100],
               [0,1,-4,0,0,1,0,0,0,0,0,0,-100],
               [1,0,0,-4,1,0,1,0,0,0,0,0,0],
               [0,1,0,1,-4,1,0,1,0,0,0,0,0],
               [0,0,1,0,1,-4,0,0,1,0,0,0,0],
               [0,0,0,1,0,0,-4,1,0,1,0,0,0],
               [0,0,0,0,1,0,1,-4,1,0,1,0,0],
               [0,0,0,0,0,1,0,1,-4,0,0,1,0],
               [0,0,0,0,0,0,1,0,0,-4,1,0,100],
               [0,0,0,0,0,0,0,1,0,1,-4,1,100],
               [0,0,0,0,0,0,0,0,1,0,1,-4,100]
               ],dtype="float64")
n=12

#部分ピポット選択
data=pt.part_pivot(data,n)
a=data[:,:-1]
b=data[:,-1]
x=np.array([1.2]*n,dtype="float64")


while(m<=n):
    #行についての計算
    for i in range(n):
        s=0.
        #列についての計算
        for j in range(n):
            s+=a[i,j]*x[j]
        X=(b[i]-s+a[i,i]*x[i])/a[i,i]
        temp=((X-x[i])/X)
        if temp<0:temp*=-1
        #収束判定
        if temp<eps:
            m+=1
        x[i]=X

#表示
for i in range(n):
    print(f"x({i+1}):{round(x[i],3)}")
