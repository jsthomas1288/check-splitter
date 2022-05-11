def split_check(total, people):
    if people <=1:
        raise ValueError("More than 1 person is required to split the check")
    # This is the cost per person
    return round((total/people), 2)

try:
    total_amt = float(input("How much is the total cost of the bill?   "))
    total_ppl = int(input("How many people will be splitting the check?   "))
    amount = split_check(total_amt, total_ppl)
except ValueError as err:
    print("Oh no! That's not a valid value. Try again!")
    print("({})".format(err))
else:
    print("Each person owes ${}".format(amount))