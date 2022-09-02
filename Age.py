import statistics
age=[19,22,19,24,20,25,26,24,25,24]
age.sort()
print("Sorting order of the given list is:",age)
a=min(age)
print("Minimum age of the given list:",a)
b=max(age)
print("Maximum age of the given list:",b)
age.append(a)
age.append(b)
print("Adding min and max again to the list:",age)
print("Median age of the list is:",statistics.median(age))
def Average(age):
    avg=sum(age)/len(age)
    return avg
avg=Average(age)
print("Average of the list is:",avg)
range=b-a
print("Range of the list is:",range)

