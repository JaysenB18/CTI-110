#Jaysen Boscan
#3/23/2024
#P3HW2_salary
#write program to calculate employees salary

#Enter user info

employee_name = input('Enter employees name: ')
hours_worked = float(input('Enter number of hours worked: '))
pay_rate = float(input('Enter employees pay rate: '))
print('---------------------------------------')

print(employee_name)
#calculate hourly pay
if hours_worked < 40:
   gross_pay = rate * hours  
else:
    Overtime = hours_worked - 40           
#calculate gross pay    
Gross_pay = (pay_rate * 40.0) + (1.5 * pay_rate * Overtime)
#calculate overtime pay
Overtime_pay = (1.5 * pay_rate * Overtime)
#calculate regular hourly pay -OT
RegHour_pay = (hours_worked * pay_rate)

print('Hours worked    Pay rate    Overtime      Overtime pay   Reghour pay    Gross pay ')
print('-------------------------------------------------------------------------------------------------------------------')
print(f'{hours_worked:<15.2f}{pay_rate:<15.2f}{Overtime:<15.2f}{Overtime_pay:<15.2f}{RegHour_pay:<15.2f}{Gross_pay:<15.2f}')      











    
