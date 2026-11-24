# 🎯 Goal
# A User Registration & Role Validator.
# The program asks for:
# Name (string)
# Age (int)
# Role — one of: admin, editor, viewer, guest
# Then it validates each field with multi-conditional logic. Role branching uses match-case. 
# Field validation uses if-elif-else. — This deliberately shows you when to use which.

# TEST TABLE (Expectation/Behaviour):
# name="Ab", age=25, role="admin"            --> Name valid, Age valid, Admin access, Registration complete
# name="A", age=25, role="admin"             --> ❌ Name too short, Registration failed
# name="Oladipo", age=15, role="viewer"      --> ❌ Too young, Limited access, Registration failed
# name="Oladipo", age=30, role="superadmin"  --> Admin access (OR pattern works)
# name="Oladipo", age=30, role="wizard"      --> ❌ Unknown role, Registration failed

def control_flow_lab():
    """This is A User Registration & Role Validator Function"""

    # Input Section
    while True:
        try:
            name = input("What is your name: ").strip()
            age = int(input("How old are you: "))
            role = input("What is your role (admin, editor, viewer, guest): ").strip().lower()
        except ValueError:
            print("Numbers Only.")
            continue
        except Exception as e:
            print(f"error as {e}.")
            continue 

    # Validation Section — use if-elif-else
    
    # Validate name:
        if len(name) >= 2 and name.isalpha():
            print("✅ Name valid")
            name_ok = True
        elif len(name) < 2 and name.isalpha():
            print("❌ Name is too short")
            name_ok = False
        elif len(name) >= 2 and not name.isalpha():
            print("❌ Name must be letters only")
            name_ok = False
        else:
            print("❌ Name is invalid")
            name_ok = False

        # Validate age:
        if 18 <= age <= 120:
            print("✅ Age valid")
            age_ok = True
        elif age < 18:
            print("❌ Too young — must be 18+")
            age_ok = False
        else:
            print("❌ Invalid age")
            age_ok = False

        # Role Branching — use match-case
        match role:
            case "admin" | "superadmin":
                print("🔑 Admin access granted — full permissions")
                role_ok = True
            case "editor":
                print("✏️ Editor access granted — can edit content")
                role_ok = True
            case "viewer":
                print("👁️ Limited access — read-only")
                role_ok = True
            case "guest":
                print("View only")
                role_ok = True
            case _:
                print("❌ Unknown role — access denied")
                role_ok = False
                

        output = """
        ---- User Registration & Role Validator ---
Name = {first:10}
Age = {second:^5}
Role = {third:^5}
"""

        if name_ok and age_ok and role_ok:
            print("✅ Registration complete")
        else:
            print("❌ Registration failed — fix errors above")
            

        print(output.format(first=name, second=age, third=role))
    
        break

if __name__=="__main__":
    control_flow_lab()



    

