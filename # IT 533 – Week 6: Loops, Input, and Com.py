# IT 533 – Week 6: Loops, Input, and Comprehension
# Nicholas Summerlee
# Professor Heiden
# Fall 2025

# R1) Gather employee data with validation (re-prompt until valid)
employees = []
forbidden_email = list("!\"'#$%^&*()=+,<>/?:;[]{}\\")
forbidden_address = list("!\"'@$%^&*_+=<>?;:[]{}")

keep_going = True
while keep_going is True:
    # ID
    id_ok = False
    while id_ok is False:
        emp_id = input("Enter Employee ID (7 digits max): ")
        if emp_id.isdigit():
            if len(emp_id) <= 7:
                id_ok = True
            else:
                print("Invalid ID. Try again.")
        else:
            print("Invalid ID. Try again.")

    # Name
    name_ok = False
    while name_ok is False:
        emp_name = input("Enter Employee Name: ")
        allowed = True
        if emp_name == "":
            allowed = False
        else:
            i = 0
            while i < len(emp_name):
                ch = emp_name[i]
                if ch.isalpha() is False:
                    if ch != " ":
                        if ch != "-":
                            if ch != "'":
                                allowed = False
                i = i + 1
        if allowed is True:
            name_ok = True
        else:
            print("Invalid name. Try again.")

    # Email
    email_ok = False
    while email_ok is False:
        emp_email = input("Enter Employee Email: ")
        has_at = "@" in emp_email
        bad_found = False
        i = 0
        while i < len(emp_email):
            ch = emp_email[i]
            if ch in forbidden_email:
                bad_found = True
            i = i + 1
        if has_at is True:
            if bad_found is False:
                email_ok = True
            else:
                print("Invalid email. Try again.")
        else:
            print("Invalid email. Try again.")

    # Address (optional)
    address_ok = False
    while address_ok is False:
        emp_address = input("Enter Address (optional): ")
        if emp_address == "":
            address_ok = True
        else:
            bad_addr = False
            i = 0
            while i < len(emp_address):
                ch = emp_address[i]
                if ch in forbidden_address:
                    bad_addr = True
                i = i + 1
            if bad_addr is False:
                address_ok = True
            else:
                print("Invalid address. Try again.")

    # Salary
    salary_ok = False
    while salary_ok is False:
        raw = input("Enter Salary (18–27): ")
        try:
            emp_salary = float(raw)
            if emp_salary >= 18:
                if emp_salary <= 27:
                    salary_ok = True
                else:
                    print("Salary out of range. Try again.")
            else:
                print("Salary out of range. Try again.")
        except:
            print("Invalid salary. Try again.")

    # R2) Store employee record
    employees.append({
        "id": emp_id,
        "name": emp_name,
        "email": emp_email,
        "address": emp_address,
        "salary": emp_salary
    })

    # R3) Ask to continue
    answer = input("Add another employee? (y/n): ").lower()
    if answer != "y":
        keep_going = False

# R4) Add "IT Department" to each name using a comprehension
updated_names = [e["name"] + " IT Department" for e in employees]

# R5) Increase salary by 30% using a comprehension
updated_salaries = [round(e["salary"] * 1.30, 2) for e in employees]

# R6) Build updated list of dictionaries
updated_employees = [
    {
        "id": e["id"],
        "name": updated_names[i],
        "email": e["email"],
        "address": e["address"],
        "salary": updated_salaries[i]
    }
    for i, e in enumerate(employees)
]

# R7) Print updated information
print("\nUpdated Employee List:")
for e in updated_employees:
    addr = e["address"]
    if addr == "":
        addr = "(none)"
    # Using simple print with commas to avoid advanced formatting
    print("ID:", e["id"], ", Name:", e["name"],
          ", Email:", e["email"], ", Address:", addr,
          ", Salary: $", "%.2f" % e["salary"], sep="")
