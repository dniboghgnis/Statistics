N=int(raw_input())
values=raw_input().strip().split(" ")

for i in range(len(values)):
    values[i]=float(values[i])

def std_devn(values):
    sum=0
    dev=0
    mean=0
    for i in range(len(values)):
        sum=sum+values[i]
        mean=sum/N
    for i in range(len(values)):
        dev=dev+((values[i]-mean)**(2))
    dev=dev/N
    return dev**(0.5)


print (("{:.1f}").format(std_devn(values)))


# 5
# 10 40 30 50 20

# 14.1