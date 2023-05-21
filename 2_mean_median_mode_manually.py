#let's calculate Mean
# The mean is the average value of all the values in a dataset.
def mean_manually(l):
    total=sum(l)
    no_elements=len(l)
    result=total/no_elements
    return result

#The Median is the middle value among all the values in sorted order.
def mediatn_manually(l):
    l.sort()
    no_elements = len(l)
    if no_elements%2!=0:
        ind=no_elements//2+1
        return l[ind]
    else:
        val1=l[no_elements//2]
        val2=l[no_elements//2+1]
        return val1+val2

#Mode is the most frequently occurring value among all the values.
def mode_manuall(l):
    # Mode
    frequency = {}
    for i in l:
        frequency.setdefault(i, 0)
        frequency[i] += 1

    frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            mode = i
    return mode

l=[1,4,5,6,8,4,2,5,7,5,3,2,5,7,7]
print("Mean of Given list is : ",mean_manually(l))
print("Median of Given list is : ",mediatn_manually(l))
print("Mode of Given list is : ",mode_manuall(l))