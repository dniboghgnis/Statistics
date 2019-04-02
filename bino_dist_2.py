def cal_fac(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

t=raw_input().strip().split(" ")
prob=float(t[0])/100
n=int(t[1])

sum1=0
for i in range(0,3):
    fac_n=cal_fac(n)
    fac_x=cal_fac(i)
    fac_n_x=cal_fac(n-i)
    nx=fac_n/(fac_x*fac_n_x)
    p_x=(prob)**(i)
    q_x=(1-prob)**(n-i)

    bino_nxp=nx*p_x*q_x
    sum1=sum1+bino_nxp

print (("{:.3f}").format(sum1))


sum=0
for i in range(2,11):
    fac_n=cal_fac(n)
    fac_x=cal_fac(i)
    fac_n_x=cal_fac(n-i)
    nx=fac_n/(fac_x*fac_n_x)
    p_x=(prob)**(i)
    q_x=(1-prob)**(n-i)

    bino_nxp=nx*p_x*q_x
    sum=sum+bino_nxp

print (("{:.3f}").format(sum))
