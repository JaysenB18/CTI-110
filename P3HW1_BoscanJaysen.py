#Jaysen Boscan
#3/18/2024
#P3HW1

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

print("------------Results------------")
#lowest grade
lowest_grade = min (mod_1, mod_2, mod_3, mod_4, mod_5, mod_6)
print(f"Lowest grade:{lowest_grade:.1f} ")
#highest grade
highest_grade = max(mod_1, mod_2, mod_3, mod_4, mod_5, mod_6)
print(f"Highest grade:{highest_grade:.1f} ")
#calculate the sum
sum = mod_1 +mod_2 + mod_3 +mod_4 + mod_5 + mod_6
print(f"Sum of grades: {sum:.2f} ")
#calculate average
average = (mod_1 +mod_2 + mod_3 + mod_4 + mod_5 + mod_6) /6
print(f"Average: {average:.2f} ")

print("--------------------------------------")
# determine letter grade for average

if average >= 90:
    print("Your grade is A")
elif average >= 80:
    print("Your grade is B")
elif average >= 70:
    print("Your grade is C")
elif average >=60:
    print("Your grade is D")
else:
    print(" Your grade is F")






