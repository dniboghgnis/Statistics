# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(raw_input())

values=raw_input().strip().split(" ")
freq=raw_input().strip().split(" ")

for i in range(N):
    values[i]=float(values[i])
    freq[i]=int(freq[i])
temp=[]
for i in range(N):
    for j in range(freq[i]):
        temp.append(values[i])
temp.sort()
def med(arr):
    if(len(arr)%2==0):
        return (arr[len(arr)/2]+arr[(len(arr)/2)-1])/2
    else :

if (len(temp)%2==0):
    median= (med(temp))
    q1=temp[:(len(temp)/2)]
    q2=temp[-(len(temp)/2):]
    print ("{:.1f}").format(int(med(q2))-(int)(med(q1)))
if (len(temp)%2!=0):
    median= (med(temp))
    q1=temp[:(len(temp)/2)]
    q2=temp[-(len(temp)/2):]


# 6
# 6 12 8 10 20 16
# 5 4 3 2 1 5

# 9.0