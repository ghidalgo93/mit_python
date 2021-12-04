
# Float, Float, Float -> Int
# Given a starting annual salary (Float), a portion of salary to be saved (Float), and total cost of a dream home (Float), return the months it will take you to save up enough money for a down payment

# ask for user input

# calculate months it will take to save up 
# stub
# def calc_month_to_downpayment(salary, perc_of_salary_saved, total_house_cost):
#     return 0


# template
def calc_month_to_downpayment(anual_salary: float, percent_saved: float, total_cost: float):
    # consts
    portion_down_payment: float = 0.25  # perc. of total cost needed for downpayment
    roi: float = 0.04                   # return on investment constant
    down_payment: float = total_cost * portion_down_payment # down_payment needed to purchase house
    monthly_salary: float = anual_salary / 12 
    monthly_salary_saved: float = monthly_salary * percent_saved; 

    # variables  
    current_savings: float = 0          # current savings starts at 0 
    month: int = 0                      # current month starts at 0


    while (current_savings <= down_payment):
        current_month_roi = current_savings * (roi / 12)
        current_savings = current_savings + current_month_roi + monthly_salary_saved
        month = month + 1

    return month

calc_month_to_downpayment(120000, .10, 1000000)
