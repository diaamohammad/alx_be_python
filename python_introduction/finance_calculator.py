#promt the user for their monthly income

income = float(input("Enter your monthly income: "))

#promt the user for their total monthly expenses

expenses = float(input("Enter your total monthly expenses: "))

#calculate monthly saving

monthly_savings = income - expenses

# Calculate projected annual savings with a simple 5% interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

#display the result

print(f"Your monthly savings are: {monthly_savings:.2f} units.")
print(f"Your projected annual savings with interest are: {projected_savings:.2f} units.")

