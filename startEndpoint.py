# #1 wap to takes start_point and end_point from the user input and print all number divisible 2&3

print("\nDivisiblity check krne ka tool....")
x= int(input("Enter your starting point :::"))
y= int(input("Enter your ending point :::"))

for i in range(x,y+1,1):
    if i%2==0:
        print(f"{i} is divisable by 2")
    
    elif i%3==1:
        print(f"{i} is divisable by 3")
