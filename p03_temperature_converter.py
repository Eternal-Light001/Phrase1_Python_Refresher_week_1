# STEP 1:-
# Create two functions with c_to_f(c) and f_to_c(f)
# Create a while loop, set it to True
# Created options from 1 to 3
# Take option input "selection"
# Use if "selection" then perform first function f_to_c(f) vise verse for elif
# Exit message 
# A break

# TEST TABLE
# c_to_f(0)	  -->   32.0	
# c_to_f(100) -->	212.0	
# f_to_c(32)  -->	0.0	
# f_to_c(212) -->	100.0	





def c_to_f(c):
    return (c * 1.8) + 32

def f_to_c(f):
    return (f - 32) / 1.8

if __name__ == "__main__":
    while True:
            option = """
            1. Convert Fahrenheit to celsius           
            2. Covert Celsius to Fahrenheit
            3. Exit
            """
            print(option)

            selection = input("Choose option from (1 - 3): ")

            if selection == "1":
                f = float(input("Fahrenheit: "))
                print(f"Celsius = {f_to_c(f)}°C")
            elif selection == "2":
                c = float(input("Celsius: "))
                print(f"Fahrenheit = {c_to_f(c)}°F")
            elif selection == "3":
                print("Have a nice day")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")