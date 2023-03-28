# CTI-110

   # P3HW2 - Salary

   # Ronnie Hutchins
   # 03/23/2023

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's pay rate: "))

ovthrs = 0.0
ovtpay = 0.0
if hours > 40:
       regpay = payrate * 40
       ovthrs = hours - 40
       ovtpay = payrate * ovthrs * 1.5
       grosspay = ovtpay + regpay
else:
    regpay = hours * payrate
    grosspay = ovtpay + regpay
print('-----------------------------------------------------------------------------')
print('Employee name:', name)

print()
print("Hours Worked"+"   "*3 +"Pay Rate"+" "*16+"OverTime"+" "*10+"Overtime Pay"+" "*12+"RegHour Pay"+" "*15+"Gross Pay")
print('-------------------------------------------------------------------------------------------------------------------------------------------------')

print(hours, '\t\t', payrate,'\t\t',ovthrs, '\t'+'       $' +  str(format(ovtpay,' ,.2f')) +'\t' + '      $' +  str(format(regpay,' ,.2f')) +'\t' + '     $' +  str(format(grosspay,' ,.2f')))



 
     







