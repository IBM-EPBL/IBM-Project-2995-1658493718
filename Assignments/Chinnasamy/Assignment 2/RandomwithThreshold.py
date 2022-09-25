import random
threshold = int(input("Enter Threshold Temperature(Range 0,50):"))
a=1
while(a==1):
    val=random.randint(0,50)
    print("Random Temperature: ",val)
    if val>threshold:
        print("Random Temp:",val,"higher than",threshold,"(Threshold Temperature)")
    elif threshold>val:
        print("Random Temp:",val,"less than",threshold,"(Threshold Temperature)")
    else:
        print("Random Temp:",val,"equals to",threshold,"(Threshold Temperature)")
    a=int(input("Enter 1 to Repeat:"))