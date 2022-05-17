# Nilber Mota

# Qualifying for a Loan Activity

print("#########################################################")
print("\nPlease rating the following questions from 1-10:\n")

large_loan = int(input("How large is the loan?\n"))
credit_history = int(input("How good is your credit history?\n"))
income = int(input("How high is your income?\n"))
down_payment = int(input("How large is your down payment?\n"))

decision = False

if large_loan >= 5:
  if credit_history >= 7 and income >= 7:
    decision = True
  elif down_payment >= 5:
    decision = True
  else:
    decision = False
elif credit_history < 4:
  decision = False
elif income >= 7 or down_payment >= 7:
  decision = True
elif income >= 4 and  down_payment >= 7:
  decision = True
else:
  decision = False

if decision:
  print(f"Loan size: {large_loan}, Income: {income}, Down Payment: {down_payment}, Decision: Approved")
else:
  print(f"Loan size: {large_loan}, Income: {income}, Down Payment: {down_payment}, Decision: Reject")


