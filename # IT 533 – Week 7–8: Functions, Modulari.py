# IT 533 – Week 7–8: Refactoring Employee Data Program Using Functions
# Nicholas Summerlee
# Professor Heiden
# Fall 2025

import json

# Global constants for validation (from Week 6)

FORBIDDEN_EMAIL_CHARS = list("!\"'#$%^&*()=+,<>/?:;[]{}\\")
FORBIDDEN_ADDRESS_CHARS = list("!\"'@$%^&*_+=<>?;:[]{}")

# R1) Input + validation functions for each field

def get_valid_id():
    while True:
        emp_id = input("Enter Employee ID (7 digits max): ")
        if emp_id.isdigit():
            if len(emp_id) <= 7:
                return emp_id
            else:
                print("Invalid ID. Try again.")
        else:
            print("Invalid ID. Try again.")


def get_valid_name():
    while True:
        emp_name = input("Enter Employee Name: ")
        allowed = True
        if emp_name == "":
            allowed = False
        else:
            i = 0
            while i < len(emp_name):
                ch = emp_name[i]
                if not ch.isalpha():
                    if ch != " " and ch != "-" and ch != "'":
                        allowed = False
                i += 1

        if allowed:
            return emp_name
        else:
            print("Invalid name. Try again.")


def get_valid_email():
    while True:
        emp_email = input("Enter Employee Email: ")
        has_at = "@" in emp_email
        bad_found = False
        i = 0
        while i < len(emp_email):
            ch = emp_email[i]
            if ch in FORBIDDEN_EMAIL_CHARS:
                bad_found = True
            i += 1

        if has_at and not bad_found:
            return emp_email
        else:
            print("Invalid email. Try again.")


def get_valid_address():
    while True:
        emp_address = input("Enter Address (optional): ")
        if emp_address == "":
            return emp_address
        else:
            bad_addr = False
            i = 0
            while i < len(emp_address):
                ch = emp_address[i]
                if ch in FORBIDDEN_ADDRESS_CHARS:
                    bad_addr = True
                i += 1
            if not bad_addr:
                return emp_address
            else:
                print("Invalid address. Try again.")


def get_valid_salary():
    while True:
        raw = input("Enter Salary (18–27): ")
        try:
            emp_salary = float(raw)
            if 18 <= emp_salary <= 27:
                return emp_salary
            else:
                print("Salary out of range. Try again.")
        except:
            print("Invalid salary. Try again.")

def get_employee_record():
    
    #R1) Gather a single employee record using field-specific validation functions. Returns a dictionary representing one employee.
    
    emp_id = get_valid_id()
    emp_name = get_valid_name()
    emp_email = get_valid_email()
    emp_address = get_valid_address()
    emp_salary = get_valid_salary()

    # R2) Store employee record (single record)
    return {
        "id": emp_id,
        "name": emp_name,
        "email": emp_email,
        "address": emp_address,
        "salary": emp_salary
    }


def collect_employees():
    employees = []
    keep_going = True
    while keep_going:
        employee = get_employee_record()
        employees.append(employee)

        # R3) Ask to continue
        answer = input("Add another employee? (y/n): ").lower()
        if answer != "y":
            keep_going = False

    return employees

# R4 & R5) Functions to perform comprehensions

def add_department_to_names(employees, suffix=" IT Department"):
    return [e["name"] + suffix for e in employees]


def increase_salaries(employees, factor=1.30):
    return [round(e["salary"] * factor, 2) for e in employees]

# R6) Build updated list of employee dictionaries using a comprehension. Replaces 'name' and 'salary' with updated values.
def build_updated_employee_list(employees, updated_names, updated_salaries):
    return [
        {
            "id": e["id"],
            "name": updated_names[i],
            "email": e["email"],
            "address": e["address"],
            "salary": updated_salaries[i]
        }
        for i, e in enumerate(employees)
    ]

# JSON output function

def write_employees_to_json(employees, filename="employees.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(employees, f, indent=4)
        print(f"\nEmployee data written to {filename}")
    except Exception as exc:
        print(f"Error writing to JSON file: {exc}")

# R7) Output function

def print_employee_list(employees, header="\nUpdated Employee List:"):
    print(header)
    for e in employees:
        addr = e["address"]
        if addr == "":
            addr = "(none)"
        print(
            "ID:", e["id"],
            ", Name:", e["name"],
            ", Email:", e["email"],
            ", Address:", addr,
            ", Salary: $", "%.2f" % e["salary"],
            sep=""
        )

# Main program driver (top-down design)

def main():
    # Gather all employees with validated input
    employees = collect_employees()

    # Perform transformations via comprehension functions
    updated_names = add_department_to_names(employees)       # R4
    updated_salaries = increase_salaries(employees)          # R5

    # Build updated records
    updated_employees = build_updated_employee_list(
        employees,
        updated_names,
        updated_salaries
    )                                                        # R6

    # Write final list to JSON (new requirement)
    write_employees_to_json(updated_employees)

    # Print updated list to the screen
    print_employee_list(updated_employees)                   # R7


# Standard entry point pattern
if __name__ == "__main__":
    main()
