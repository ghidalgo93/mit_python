
# Adjust Anual Salary
# Float, Float -> Float
# Given an anual salary and a semi-anual raise, return new anual salary
def adjust_anual_salary(anual_salary: float, anual_raise_perc: float):
    return anual_salary + (anual_salary * anual_raise_perc)

# Calculate Monthly Savings
# Float, Float -> Float
# Given an anual salary and a percent saved per month, return the dollar amount saved per month
# stub
def calc_monthly_savings(anual_salary, percent_saved):
    monthly_salary = anual_salary / 12
    monthly_savings = monthly_salary * percent_saved;
    return monthly_savings

# Float, Float, Float -> Int
# Given a starting annual salary (Float), a portion of salary to be saved (Float), a semi-anual-raise (Float), and total cost of a dream home (Float), return the months it will take you to save up enough money for a down payment

# ask for user input

# calculate months it will take to save up 
# stub
# def calc_month_to_downpayment_with_raise(salary, perc_of_salary_saved, semi_anual_raise, total_house_cost):
#     return 0
def calc_month_to_downpayment_with_raise(anual_salary: float, percent_saved: float, anual_raise_perc: float, total_cost: float):
    # consts
    portion_down_payment: float = 0.25  # perc. of total cost needed for downpayment
    roi: float = 0.04                   # return on investment constant
    down_payment: float = total_cost * portion_down_payment # down_payment needed to purchase house

    # variables  
    current_savings: float = 0          # current savings starts at 0 
    month: int = 0                      # current month starts at 0
    adjusted_anual_salary: float = anual_salary


    while (current_savings <= down_payment):
        if ( month != 0) and (month % 6 == 0):
            adjusted_anual_salary = adjust_anual_salary(adjusted_anual_salary, anual_raise_perc)
            
        current_month_roi = current_savings * (roi / 12)
        current_savings = current_savings + current_month_roi + calc_monthly_savings(adjusted_anual_salary, percent_saved)
        month = month + 1

    return month

calc_month_to_downpayment_with_raise(75000, .05, .05, 1500000)
