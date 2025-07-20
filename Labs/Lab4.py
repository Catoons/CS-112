def calc_years(initial_balance, rate, target):
    current_bal = initial_balance
    years = 0
    while current_bal < target:
        current_bal = current_bal + (current_bal*rate)
        years += 1
    return years