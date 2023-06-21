name = input()
age = int(input())
town = input()
salary = round(float(input()), 2)

if age < 18:
    age_range = "teen"
elif age >= 70:
    age_range = "elder"
else:
    age_range = "adult"

if salary < 500:
    salary_range = "low"
elif salary >= 2000:
    salary_range = "high"
else:
    salary_range = "medium"


print(f"Name: {name}", end="\n")
print(f"Age: {age}", end="\n")
print(f"Town: {town}", end="\n")
print(f"Salary: ${salary:.2f}", end="\n")
print(f"Age range: {age_range}", end="\n")
print(f"Salary range: {salary_range}", end="\n")

