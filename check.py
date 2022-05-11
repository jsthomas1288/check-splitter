def split_check(total, people):
    # This is the cost per person
    return round((total/people), 2)

total_amt = float(input("How much is the total cost of the bill?   "))
total_ppl = int(input("How many people will be splitting the check?   "))
amount = split_check(total_amt, total_ppl)

print("Each person owes ${}".format(amount))