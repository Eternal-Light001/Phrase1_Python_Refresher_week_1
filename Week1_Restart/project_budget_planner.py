# STEP (Procedure)
# This is a Budget planner that I created using Python function (def)
# It Takes your monthly income and expenses, shows you what you're saving and tells you if you're on track for a goal
# TEST TABLE (Expectation)
# SCENARIO 1 — healthy:
#   income=200000, expense=50000, goal=300000, years=3
#   → savings=150000, yearly=1800000, progress=50.00%, On_track=True
# SCENARIO 2 — over budget:
#   income=100000, expense=150000, goal=50000, years=2
#   → savings=-50000, progress=-100.00%, On_track=False
# SCENARIO 3 — exact break-even:
#   income=100000, expense=100000, goal=20000, years=1
#   → savings=0, progress=0.00%, On_track=False

import datetime

def budget_planner():
    """It Takes your monthly income and expenses, shows you what you're saving and tells you if you're on track for a goal"""      # This is the docstring for the budget_planner function, explaining its purpose

    # App Name
    app_name = "Light Skill Hub Budget Planner"      # This the Application Name
    print(f"--- Welcome To {app_name} ---")      # Print the Application Name

    # 1 - Inputs Section
    while True:      # Start an infinite loop to repeatedly prompt the user for input until valid data is provided
        try:      # Prompt the user for their name, monthly income, monthly expense, saving goal, and years of saving
            user_name = input("What is your name: ").strip()      # Get the user's name and remove any leading/trailing whitespace
            monthly_income = float(input('What is your Monthly Income: '))     # Get the user's monthly income and convert it to a float
            monthly_expense = float(input("What is your Monthly Expense: "))      # Get the user's monthly expense and convert it to a float
            saving_goal = float(input("What is your saving amount goal: "))      # Get the user's saving goal and convert it to a float
            years_of_saving = int(input("How many years do you which to save: "))      # Get the number of years the user wants to save and convert it to an integer
        except NameError:      # Handle the case where the user inputs an invalid name
            print("Input valid name")      # Print an error message indicating that the name input is invalid
        except ValueError:      # Handle the case where the user inputs an invalid number (e.g., non-numeric characters)
            print("Input valid digit, without (,)")     # Print an error message indicating that the number input is invalid
        except Exception as e:      # Handle any other unexpected exceptions that may occur during input
            print(f"An error occured {e}")      # Print a generic error message with the exception details
            continue      # Continue the loop to prompt the user for input again if an error occurred

        # 2 Calculations Section
        try:      # Perform calculations based on the user's input
            monthly_savings = monthly_income - monthly_expense      # Calculate the monthly savings by subtracting expenses from income
            savings_percentage = (monthly_savings / saving_goal) * 100      # Calculate the savings percentage by dividing monthly savings by the saving goal and multiplying by 100
            annual_saving = monthly_savings * 12      # Calculate the annual savings by multiplying monthly savings by 12
            months = years_of_saving * 12      # Calculate the total number of months by multiplying years of saving by 12
            On_track = (monthly_savings >= saving_goal / months)      # Determine if the user is on track to meet their saving goal by comparing monthly savings to the required monthly savings to reach the goal in the specified time frame
            
        except ZeroDivisionError:      # Handle the case where the saving goal is zero, which would cause a division by zero error
            print("Saving goal cannot be zero")      # Print an error message indicating that the saving goal cannot be zero
        except Exception as e:      # Handle any other unexpected exceptions that may occur during calculations
            print(f"An error occurred: {e}")      # Print a generic error message with the exception details

        # 3 Comparisons (If Statements)
        if monthly_income > monthly_expense:
            print(f"✅ Cash-flow positive")
        elif monthly_income < monthly_expense:
            print(f"⚠️ You are over budget")
        else:
            print(f"Breaking even — no savings this month")      # 

        # 4 Output Layout:-
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = """
    BUDGET SUMMARY - {date}
    ===============================
    Name: {first:14}
    Monthly Income: #{second:,.2f}
    Monthly Expense: #{third:,.2f}
    ----------------------------
    Monthly Savings: #{fourth:,.2f}
    Yearly Savings: #{Fifth:,.2f}
    ----------------------------
    Saving Years: {sixth} Years
    Savings Goal: #{seventh:,.2f}
    progress: {eighth:.2f}%
    On Track: {nineth}
    ==============================
    """


        print(output.format(date=date, first=user_name, second=monthly_income, third=monthly_expense, fourth=monthly_savings, Fifth=annual_saving, sixth=years_of_saving, seventh=saving_goal, eighth=savings_percentage, nineth=On_track))

        break  # Exit the loop after successful execution
if __name__ == "__main__":
    budget_planner()