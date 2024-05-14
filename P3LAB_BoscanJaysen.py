#Jaysen Boscan
#3/16/2024
#P3Lab exact change
#Write a program with total change amount

input_change = int(input())

if input_change == 0:
    print('No change')

dollars = input_change // 100
input_change -= dollars * 100
if dollars: print(dollars, 'Dollars' if dollars > 1 else 'Dollar')

quarters = input_change // 25
input_change -= quarters * 25
if quarters: print(quarters, 'Quarters' if quarters > 1 else 'Quarter')

dimes = input_change // 10
input_change -= dimes * 10
if dimes: print(dimes, 'Dimes' if dimes > 1 else 'Dime')

nickels = input_change // 5
input_change -= nickels * 5
if nickels: print(nickels, 'Nickels' if nickels > 1 else 'Nickel')

pennies = input_change
if pennies: print(pennies, 'Pennies' if pennies > 1 else 'Penny')
       
