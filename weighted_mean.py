# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(raw_input())
values=raw_input().strip().split(" ")
weights=raw_input().strip().split(" ")

for i in range(len(values)):
    values[i]=float(values[i])
    weights[i]=float(weights[i])

#print (values)

def w_sum(values,weights):
    sum=0
    weighted_sum=0
    for i in range(len(values)):
        weighted_sum=weighted_sum+(values[i]*weights[i])
        sum=sum+weights[i]
    return weighted_sum/sum

print (("{:.1f}").format(w_sum(values,weights)))



# 5
# 10 40 30 50 20
# 1 2 3 4 5

# 32.0