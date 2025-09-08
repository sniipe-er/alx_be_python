monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
monthly_saving = monthly_income - monthly_expenses
projected_savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print(f"your monthly savings: {monthly_saving}")
print(f"your projected annual savings after including interes: {projected_savings}")