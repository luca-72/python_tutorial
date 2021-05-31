import math

has_good_credit = True
good_down_payment = 1000000 * .10
bad_down_payment = 1000000 * .20

if has_good_credit:
    print(f"You have good credit your down payment needs to be, ${good_down_payment}")
else:
    print(f"You don't have good credit, your down payment needs to be, ${bad_down_payment}")
has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for a Loan")