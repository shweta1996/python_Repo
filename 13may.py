# #wap to sum of the indices of a string: "python"
# #wap to print the factorial from 1 to 8
# #wap to print only prime number from 1 to 15

# str="python"
# size=len(str)
# sum=0
# for i in range(size):
#     sum= sum+i
# print(sum)

# #wap to print the fact=orial from 1 to 8
# factorial=1
# for i in range(1,9):
#     factorial = factorial*i
#     print("factorial of ", i, "=", factorial)

# #wap to print only prime number from 1 to 15

for num in range(1,16):
   if num>1:
    for i in range(2,num):
       if num%i==0:
           break
    else:
           print(num)  