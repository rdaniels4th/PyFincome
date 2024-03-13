import math

def calculate_continuous_compounded_amount(principal, annual_interest_rate, time_years):
    """
    Calculate the future value of an investment based on continuous compounding.
    
    Args:
    - principal (float): The initial amount of money before interest.
    - annual_interest_rate (float): The annual interest rate as a decimal.
    - time_years (float): The time period in years for the investment.
    
    Returns:
    - float: The future value after applying continuous compounding.
    """
    future_value = principal * math.exp(annual_interest_rate * time_years)
    return future_value

# Example Usage:
principal_amount = 1000  # $1,000
annual_interest_rate = 0.05  # 5%
time_in_years = 3  # 3 years

future_value = calculate_continuous_compounded_amount(principal_amount, annual_interest_rate, time_in_years)
print(f"The future value after 3 years with continuous compounding is: ${future_value:.2f}")
