N=int(raw_input())
arr=[]
t=raw_input().strip().split(" ")
for i in range(len(t)):
    t[i]=float(t[i])
def mean(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    return sum/len(arr)

print (("{:.1f}".format(mean(t))))

def median(arr):
    arr.sort()
    if (len(arr)%2!=0):
        return arr[len(arr)/2]
    else:
        return (arr[len(arr)/2] + arr[(len(arr)/2)-1])/2
print (median(t))
count=[0]*100000
def mode(arr):
    max=0
    index=0
    for i in range(len(arr)):
        count[int(arr[i])]=count[int(arr[i])]+1
    for i, value in enumerate(count):
        if (value>max):
            max=value
            index=i

    return (index)

print(mode(t))


# 10
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060


# 43900.6
# 44627.5
# 4978