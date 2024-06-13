def calculate_simple_compounded_amount(principal, annual_interest_rate, time_years, compounding_periods_per_year):
    """
    Calculate the future value of an investment based on simple compounding with different compounding frequencies.
    
    Args:
    - principal (float): The initial amount of money before interest.
    - annual_interest_rate (float): The annual interest rate as a decimal.
    - time_years (float): The time period in years for the investment.
    - compounding_periods_per_year (int): The number of times the interest is compounded per year.
    
    Returns:
    - float: The future value after applying simple compounding.
    """
    future_value = principal * (1 + annual_interest_rate / compounding_periods_per_year) ** (compounding_periods_per_year * time_years)
    return future_value

# Example Usage:
principal_amount = 1000  # $1,000
annual_interest_rate = 0.05  # 5%
time_in_years = 3  # 3 years
compounding_periods_per_year = 4  # Quarterly compounding

future_value = calculate_simple_compounded_amount(principal_amount, annual_interest_rate, time_in_years, compounding_periods_per_year)
print(f"The future value after 3 years with quarterly compounding is: ${future_value:.2f}")
