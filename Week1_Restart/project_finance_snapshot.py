# STEP (Procedure)
# This is project Finance python project

# TEST TABLE
# income=5000, expenses=3500 --> monthly_savings=1500
# monthly_savings * 12       --> yearly=18000
# yearly * 3                 --> total=54000
# expenses < income          --> True
# years=3, years & 1         --> 1 (odd)

# Inputs (use input(), cast with float() / int()):-


Greet_Application_Name = "----Welcome To Fidel Project Finance Snapshot----"
print(f"{Greet_Application_Name:>50}")
Application_Name = "Fidel Project Finance Snapshot"
User_name = input("What is your name: ")
Monthly_income  = float(input("What is your monthly income: "))
Monthly_expenses = float(input("What is your Monthly expenses: "))
Savings_goal = int(input("What is your Savings goal amount: "))
Years_to_save = int(input("How many years do you wish to save: "))

# Calculations (arithmetic operators):
monthly_savings = Monthly_income - Monthly_expenses
yearly_savings = monthly_savings * 12
total_savings_in_years = yearly_savings * Years_to_save

# Comparison results (these produce True/False — no if/else needed):
cash_flow_positive = Monthly_expenses < Monthly_income
validate_saving = monthly_savings <= Savings_goal
saving_extent = Monthly_expenses < Monthly_income and Years_to_save > 5
accountability = monthly_savings < 0 or Years_to_save > 10


# Bitwise demo (curriculum requirement — one line):
is_odd = Years_to_save & 1
print(f"Is {Years_to_save} odd? {is_odd}")

# Output (f-strings with formatting):
Finalizing = """
Cash Flow: {CFL} 🎉🎉🎉 Cash-flow positive
Validate Saving: {VS} 🎉🎉🎉 Fit to save
Saving Extent: {SE} 
Saving Extension: {A}"""
print("---------------------------------------")
print(Finalizing.format(CFL=cash_flow_positive, VS=validate_saving, SE=saving_extent, A=accountability))
print("=======================================")

print("=======================================")
print(f"{Application_Name:^50}")
output = """
Name: {first}
Monthly Savings: {second:.2f}
Savings in a year: {third:.2f}
Total saved over the years: {fourth:.2f}
"""
print(output.format(first=User_name, second=monthly_savings, third=yearly_savings, fourth=total_savings_in_years))
print("---------------------------------------")