#jaysen Boscan

#3/10/2024

#P2HW2

#Asks the user to enter grades for following tests

#get info from user
mod1 = float(input("Enter grade for module 1: "))
mod2 = float(input("Enter grade for module 2: "))
mod3 = float(input("Enter grade for module 3: "))
mod4 = float(input("Enter grade for module 4: "))
mod5 = float(input("Enter grade for module 5: "))
mod6 = float(input("Enter grade for module 6: "))

print("------------Results------------")
#lowest grade
lowest_grade = min (mod1, mod2, mod3, mod4, mod5, mod6)
print(f"Lowest grade:{lowest_grade:.1f} ")
#highest grade
highest_grade = max(mod1, mod2, mod3, mod4, mod5, mod6)
print(f"Highest grade:{highest_grade:.1f} ")
#calculate the sum
sum = mod1 +mod2 + mod3 + mod4 + mod5 + mod6
print(f"Sum of grades: {sum:.2f} ")
#calculate average
average = (mod1 +mod2 + mod3 + mod4 + mod5 + mod6) /6
print(f"Average: {average:.2f} ")

print("--------------------------------------")
