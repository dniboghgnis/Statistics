# Enter your code here. Read input from STDIN. Print output to STDOUT
def cal_fac(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

sum=0
for i in range(3,7):
    fac_n=cal_fac(6)
    fac_x=cal_fac(i)
    fac_n_x=cal_fac(6-i)
    nx=fac_n/(fac_x*fac_n_x)
    p_x=(1.09/2.09)**(i)
    q_x=(1/2.09)**(6-i)

    bino_nxp=nx*p_x*q_x
    sum=sum+bino_nxp

print (("{:.3f}").format(sum))