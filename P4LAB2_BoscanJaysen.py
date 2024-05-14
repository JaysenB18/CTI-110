#Jaysen Boscan
#3/27/2024
#P4LAB2
#Use a while loop

#Get two integer values from the user 
var1 = int(input("Enter the smaller integer: "))
var2 = int(input("Enter a larger integer: "))

#while var1 is larger allow the user to re-enter values
while var1 >= var2:
    print("First number must be smaller. Try again. ")
    var1 = int(input("Enter the smaller integer: "))
    var2 = int(input("Enter a larger integer: ")) 

#The while loop has broken. Values entered correctly.
for num in range (var1, var2+1, 5):
    print(num, end = " ")

