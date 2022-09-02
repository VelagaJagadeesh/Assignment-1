it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
a=len(it_companies)
print("Length of the companies:",a)
it_companies.add("twitter")
print("Adding twitter to the company:",it_companies)
it_companies1={"Infosys","Cisco","Accenture"}
it_companies.update(it_companies1)
print("Adding multiple companies to the set:",it_companies)
it_companies.remove("IBM")
print("After removing one company:",it_companies)
print("The discard()stratergy eliminates the predetermined thing from the set.This technique is unique in relation to remove() stratergy.")
print("Because the remove() method will raise a error if the specified item doesn't exist, and the discard() method will not.")
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]
C=A.union(B)
print("Joining A and B sets:",C)
D=A.intersection(B)
print("Intersection of A and B:",D)
E=A.issubset(B)
print("A is a subset of B or not:",E)
F=A.isdisjoint(B)
print("A and B disjoint sets or not;",F)
G=A.union(B)
H=B.union(A)
print("joining A with B and B with A:",G,H)
I=A.symmetric_difference(B)
print("symmetric difference:",I)
del A
del B
print(len(age))
s=set(age)
print(s)
print(len(s))
