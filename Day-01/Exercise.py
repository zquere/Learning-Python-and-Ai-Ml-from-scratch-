lis = [20,30,10,40,50,60,70,80,90,100,33,87,67,56,87,5,4,46,34,57,86,97,97,67,56,56,98,76,56,45,]
top = []
average =[]
low =[]

for i in lis:
    if i <=30:
        low.append(i)
    if i>30:
        average.append(i)
    if i>=50:
        top.append(i)


def mean(top):
    sum = 0
    for i in top:
        sum = sum +i
    sum = sum/len(top)
    return sum

print(f"top_average-{mean(top)}",f"Average - {mean(average)}",f"Low_average-{mean(low)}")




