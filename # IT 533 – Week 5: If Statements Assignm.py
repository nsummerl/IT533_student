# IT 533 – Week 5: If Statements Assignment
# Nicholas Summerlee
# Proffesor Heiden
# Fall 2025

# R1) Mixed raw data
data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# R2 & R3) Build list of dictionaries, remove duplicates
employees = []
for i in range(len(data) - 2):
    if type(data[i]) == int and type(data[i + 1]) == str and type(data[i + 2]) == float:
        emp_id = data[i]
        emp_name = data[i + 1]
        emp_wage = data[i + 2]

        duplicate = False
        for e in employees:
            if e["id"] == emp_id:
                duplicate = True
        if not duplicate:
            employees.append({
                "id": emp_id,
                "name": emp_name,
                "hourly_wage": emp_wage
            })

# R4) Add total_hourly_rate (wage × 1.3)
for e in employees:
    e["total_hourly_rate"] = e["hourly_wage"] * 1.3

# R5) Collect anyone with total between 28.15 and 30.65
underpaid_salaries = []
for e in employees:
    if e["total_hourly_rate"] >= 28.15 and e["total_hourly_rate"] <= 30.65:
        underpaid_salaries.append(e)

# R6) Compute raise per wage range
company_raises = []
for e in employees:
    wage = e["hourly_wage"]
    if wage >= 22 and wage < 24:
        raise_amount = wage * 0.05
    elif wage >= 24 and wage < 26:
        raise_amount = wage * 0.04
    elif wage >= 26 and wage < 28:
        raise_amount = wage * 0.03
    else:
        raise_amount = wage * 0.02

    company_raises.append({
        "name": e["name"],
        "raise": raise_amount
    })

# R7) Print lists
print("Employees with total hourly rate:")
for e in employees:
    print(e)

print("\nUnderpaid salaries (28.15–30.65):")
for u in underpaid_salaries:
    print(u)

print("\nCompany raises:")
for r in company_raises:
    print(r)
