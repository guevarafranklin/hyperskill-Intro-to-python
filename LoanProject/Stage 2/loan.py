import math

principal = int(input("Enter the loan principal: "))
print("What do you want to calculate? ")
print("type \"m\" - for number of monthly payments, ")
print("type \"p\" - for the monthly payment: ")
selection = input()

if selection == "m":
    monthly_payment = int(input("Enther the monthly payment: "))
    number_of_payments = math.ceil(principal / monthly_payment)
    if number_of_payments <= 1:
        print(f"It will take {number_of_payments} month to repay the loan")
    else:
        print(f"It will take {number_of_payments} months to repay the loan")
elif selection == "p":
    number_of_months = int(input("Enter the number of months: "))
    payment = principal / number_of_months
    if type(payment) == float:
        to_pay = math.ceil(payment)
        last_payment = round(principal - ((number_of_months - 1) * to_pay))
        print(f"Your monthly payment = {to_pay} and the last payment = {last_payment}")
    else:
        print(f"Your monthly payment = {payment}")
else:
    print("Please select the correct letter (m or p): ")
