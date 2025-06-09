import csv
import random

# Function to generate CGPA between 6.0 and 10.0 (realistic)
def generate_cgpa():
    return round(random.uniform(6.0, 10.0), 2)

# Function to generate package based on CGPA
def generate_package(cgpa):
    # Basic package + bonus based on CGPA to create positive correlation
    base_package = 3  # Minimum base package in LPA
    bonus = (cgpa - 6.0) * random.uniform(2, 3.5)  # Correlated bonus
    return round(base_package + bonus, 2)

# File name
filename = "student_placements.csv"

# Writing CSV
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["StudentID", "CGPA", "Package(LPA)"])  # Header
    
    for student_id in range(1, 101):  # 100 students
        cgpa = generate_cgpa()
        package = generate_package(cgpa)
        writer.writerow([student_id, cgpa, package])

print(f"CSV file '{filename}' generated with 100 entries.")
