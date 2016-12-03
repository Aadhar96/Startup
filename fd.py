def pred1(a,b,c):
    import pandas as pd
    d1=a[b].rolling(window=c).mean().to_frame().join(a[b].to_frame(),rsuffix='g')
    sum=0
    for i in  range(c-1,d1.shape[0]):
        sum+=(d1.loc[i][b]-d1.loc[i][b+'g'])**2
    sum=sum**0.5
    tmp=0
    try:
        for i in  range(a.shape[0]-2):
            if((a.loc[i][b]-a.loc[i+1][b]>0 and a.loc[i]['VOLUME']-a.loc[i+1]['VOLUME']>0) or (a.loc[i][b]-a.loc[i+1][b]<0 and a.loc[i]['VOLUME']-a.loc[i+1]['VOLUME']>0)):
                tmp+=1
            else:
                tmp-=1

        if((a.loc[i+1][b]-a.loc[i+2][b]>0 and a.loc[i+1]['VOLUME']-a.loc[i+2]['VOLUME']>0) or (a.loc[i+1][b]-a.loc[i+2][b]<0 and a.loc[i+1]['VOLUME']-a.loc[i+2]['VOLUME']>0)):
            tmp+=c
        else:
            tmp-=c
    except:
        for i in  range(a.shape[0]-2):
            if((a.loc[i][b]-a.loc[i+1][b]>0 and a.loc[i]['Volume']-a.loc[i+1]['Volume']>0) or (a.loc[i][b]-a.loc[i+1][b]<0 and a.loc[i]['Volume']-a.loc[i+1]['Volume']>0)):
                tmp+=1
            else:
                tmp-=1

        if((a.loc[i+1][b]-a.loc[i+2][b]>0 and a.loc[i+1]['Volume']-a.loc[i+2]['Volume']>0) or (a.loc[i+1][b]-a.loc[i+2][b]<0 and a.loc[i+1]['Volume']-a.loc[i+2]['Volume']>0)):
            tmp+=c
        else:
            tmp-=c

    tmp1=a[(a.shape[0]-20):a.shape[0]][b].std()
    tmp2=0
    for j in range(d1.shape[0]-c,d1.shape[0]):
        tmp2+=d1.loc[i][b]
    tmp2=tmp2/c
    if((d1.loc[d1.shape[0]-1][b]+tmp2)<=d1.loc[d1.shape[0]-1][b+'g']<=(d1.loc[d1.shape[0]-1][b]+2*tmp2)):
        tmp-=2*tmp2    
    elif((d1.loc[d1.shape[0]-1][b]-2*tmp2)<=d1.loc[d1.shape[0]-1][b+'g']<=(d1.loc[d1.shape[0]-1][b]-tmp2)):
        tmp+=2*tmp2
    if((d1.loc[d1.shape[0]-1][b]+2*tmp2)<=d1.loc[d1.shape[0]-1][b+'g']):
        tmp=-1
    elif((d1.loc[d1.shape[0]-1][b]-2*tmp2)>=d1.loc[d1.shape[0]-1][b+'g']):
        tmp=1
    sum1=0
    sum2=0
    for i in range(d1.shape[0]-c,d1.shape[0]):
        sum1+=d1.loc[i][b]
        sum2+=(d1.loc[i][b]-d1.loc[i][b+'g'])**2

    sum1=sum1/c
    sum2=sum2**0.5
    dev=.8*sum2+.2*sum
    if(tmp>0):
        return sum1+dev
    else:
        return sum1-dev
    
def pred2(a,b):
    import pandas as pd
    tmp=[a[b].mean()]
    for i in range(1,a.shape[0]+1):
        tmp.append(tmp[i-1]*0.15+a.loc[i-1][b]*0.85)
    tmp1=[]
    for i in range(a.shape[0]):
       tmp1.append(tmp[i]/a.loc[i][b])
    return sum(tmp1)/len(tmp1)*tmp[-1]


def pred3(a,b):
    import pandas as pd
    x2=0
    c2=0
    mean=a[b].mean()
    dev=0
    x1=a.shape[0]*(a.shape[0]+1)/2
    c1=sum(a[b])
    for i in range(a.shape[0]):
        x2+=(i+1)**2
        c2+=(i+1)*a.loc[i][b]
        dev+=(a.loc[i][b]-mean)**2/a.shape[0]


    x=(c1*x2-c2*x1)/(a.shape[0]*x2-x1**2)
    dev=dev**0.5
    y=(c1-x*a.shape[0])/x1
    if(y>0):
        return x+(a.shape[0]+1)*y-0.64*dev
    else:
        return x+(a.shape[0]+1)*y+0.71*dev


def pred4(a,b):
    from scipy.optimize import curve_fit as z
    import numpy as np
    def func(x,a,b,c):
        return a*(x**2)+b*x+c
    def func1(x,a,b,c,d):
        return a*x+b*np.sin(c*x)+d
    def func2(x,a,b,c,d,e):
        return a*(x**2)+b*x+c*np.sin(d*x)+e
    def func3(x,a,b,c,d,e):
        return a*x+b*np.sin(c*x)+d*np.cos(x)+e
    def func4(x,a,b,c,d,e):
        return a*(x**4)+b*(x**3)+c*(x**2)+d*x+e
    def func5(x,a,b,c,d,e):
        return a*(x**3)+b*(x)+c*np.exp(-x)+ d*np.sin(x)+e
    def func6(x,a,b,c,d,e):
        return a*(x**3)+b*(x)+c*np.exp(-x)+ d*np.log(x)+e
    def func7(x,a,b,c,d,e):
        return a*(x**3)+b*(x)+c*np.log(x)+ d*np.sin(x)+e
    def func8(x,a,b,c,d,e):
        return a*np.log(b*x)+c*np.exp(-d*x)+e
    arr=[]
    tmp,tmp1=z(func,range(1,a.shape[0]+1),a[b])
    arr.append(func(a.shape[0]+1,tmp[0],tmp[1],tmp[2]))
    tmp,tmp1=z(func1,range(1,a.shape[0]+1),a[b])
    arr.append(func1(a.shape[0]+1,tmp[0],tmp[1],tmp[2],tmp[3]))
    tmp,tmp1=z(func2,range(1,a.shape[0]+1),a[b])
    arr.append(func2(a.shape[0]+1,tmp[0],tmp[1],tmp[2],tmp[3],tmp[4]))
    tmp,tmp1=z(func3,range(1,a.shape[0]+1),a[b])
    arr.append(func3(a.shape[0]+1,tmp[0],tmp[1],tmp[2],tmp[3],tmp[4]))
    tmp,tmp1=z(func4,range(1,a.shape[0]+1),a[b])
    arr.append(func4(a.shape[0]+1,tmp[0],tmp[1],tmp[2],tmp[3],tmp[4]))
    tmp,tmp1=z(func5,range(1,a.shape[0]+1),a[b])
    arr.append(func5(a.shape[0]+1,tmp[0],tmp[1],tmp[2],tmp[3],tmp[4]))
    tmp,tmp1=z(func6,range(1,a.shape[0]+1),a[b])
    arr.append(func6(a.shape[0]+1,tmp[0],tmp[1],tmp[2],tmp[3],tmp[4]))
    tmp,tmp1=z(func7,range(1,a.shape[0]+1),a[b])
    arr.append(func7(a.shape[0]+1,tmp[0],tmp[1],tmp[2],tmp[3],tmp[4]))
    return sum(arr)/8
    
