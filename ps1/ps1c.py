from month_from_savings_rate import savings_in_36mo

# Integer -> Float
# Given a starting sallary (int), return the best rate of saving (float) that can be achieved in 36 months and how many steps (int) it took

# stub
# def best_savings_rate(sallary: int):
#     # return (sallary * 0, 0)
#     return (0.4411, 12)

def best_savings_rate(sallary: int):
    # constants
    total_house_cost = 1000000 
    downpayment = total_house_cost * 0.25
    epsilon = 100
    low = 0
    high = 100000
    steps = 0
    guess = (low + high) / 2

    # check for no saving possibility
    if (savings_in_36mo(10000) < downpayment):
        return "impossible chump" 

    while ( abs(savings_in_36mo(guess) - downpayment) >= epsilon ):
        if savings_in_36mo(guess) < downpayment:
            low = guess 
        else:
            high = guess
        guess = (low + high) / 2
        ++steps
        




 


