def calculate_balance(withdrawal_amt, bal_before, ATM_type, transaction_loc):
    
    if (ATM_type == 'NBU') and (transaction_loc == 'Utopia'):
        new_balance = bal_before - withdrawal_amt
        if new_balance < 0:
            new_balance -=50
            
    elif (ATM_type != 'NBU') and (transaction_loc == 'Utopia'):
        new_balance = bal_before - withdrawal_amt - 10
        if new_balance < 0:
            new_balance -=50
            
    elif (transaction_loc != 'Utopia'):
        fee = withdrawal_amt * 0.10
        new_balance = bal_before - withdrawal_amt - fee
        if new_balance < 0:
            new_balance -=50
    
    return new_balance