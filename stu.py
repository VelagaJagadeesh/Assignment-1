N=int(input("Enter number of students:"))
if(N>0):
    W_kg=[]
    for i in range(0,N):
        lb=float(input("Enter the weight in lbs:"))
        Kg=lb*0.454
        W_kg.append(Kg)
    else:
        print("Enter the number of students in positive and non zero value:")
    print(W_kg)
