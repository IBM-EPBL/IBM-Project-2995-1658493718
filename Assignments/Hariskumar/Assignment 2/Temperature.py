import random
threshold = int(input("Enter Temperature Threshold value(Range 0,40):"))
a=1
while(a==1):
    randvalue=random.randint(0,40)
    print("Randomly generated Temperature: ",randvalue)
    if randvalue>threshold:
        print(randvalue,"higher than",threshold,"(Threshold value)")
    elif threshold>randvalue:
        print(randvalue,"less than",threshold,"(Threshold value)")
    else:
        print(randvalue,"equals to",threshold,"(Threshold value)")
    a=int(input("Enter 1 to generate another number:"))