# noinspection PyPackageRequirements
import math

print("What do you want to calculate? ")
print("type \"n\" - for number of monthly payments, ")
print("type \"a\" - for annuity monthly payment amount: ")
print("type \"p\" - for loan principal: ")
selection = input()

if selection == "n":
    principal = float(input("Enter the loan principal: "))
    monthly_payment = float(input("Enter the monthly payment: "))
    loan_interest = float(input("Enter the loan interest: "))
    i = loan_interest / 12 * 0.01
    n = math.log(monthly_payment / (monthly_payment - i * principal), i + 1)
    years = math.ceil(n) // 12
    months = math.ceil(n) % 12
    if n < 12:
        print(f"I will take {math.ceil(n)} months to repay this loan!")
    else:
        print(f"It will take {round(years)} years and {round(months)} months to repay this loan!")
elif selection == "a":
    principal = float(input("Enter the loan principal: "))
    periods = float(input("Enter the number of periods: "))
    loan_interest = float(input("Enter the loan interest: "))
    i = loan_interest / 12 * 0.01
    annuity_payment = math.ceil(principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
    print(f"Your monthly payment  = {round(annuity_payment)}!")

elif selection == "p":
    annuity_payment = float(input("Enter the annuity payment: "))
    number_of_periods = float(input("Enter the number of periods: "))
    loan_interest = float(input("Enter loan interest: "))
    i = loan_interest / 12 * 0.01
    loan_principal = math.ceil(annuity_payment / ((i * math.pow(1 + i, number_of_periods)) / (math.pow(1 + i, number_of_periods) - 1)))
    print(f"Your loan principal = {round(loan_principal)}!")
else:
    print("Please select the correct menu letter: ")