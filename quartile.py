N=int(raw_input())
values=raw_input().strip().split(" ")

for i in range(len(values)):
    values[i]=float(values[i])
values.sort()
def med(arr):
    if(len(arr)%2==0):
        return (arr[len(arr)/2]+arr[(len(arr)/2)-1])/2
    else :
        return arr[len(arr)/2]

if (len(values)%2==0):
    median= (med(values))
    q1=values[:(len(values)/2)]
    q2=values[-(len(values)/2):]
    print (int)(med(q1))
    print int((med(values)))
    print int(med(q2))
if (len(values)%2!=0):
    median= (med(values))
    q1=values[:(len(values)/2)]
    q2=values[-(len(values)/2):]
    print (int)(med(q1))
    print int((med(values)))
    print int(med(q2))


# 9
# 3 7 8 5 12 14 21 13 18

# 6
# 12
# 16
