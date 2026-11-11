# Creating unclean data for practice ( make a copy of original data) 

#deleting 50% values from Open col 
# import pandas as pd

# # Load the Excel file
# file_path = "yahoo_data.xlsx"  # Replace with your actual file path
# df = pd.read_excel(file_path)

# # Remove values in odd-numbered rows (keeping even rows)
# df.loc[df.index % 2 == 0, 'Open'] = None  # Use df.index % 2 == 0 because Python uses 0-based indexing

# # Save the modified file
# df.to_excel("uncleaned_data.xlsx", index=False)

# print("Values from odd rows in Column B have been deleted successfully!")

#deleing 20% values from Volume column
# import pandas as pd
# import numpy as np

# # Load the Excel file
# file_path = "uncleaned_data.xlsx"  # Replace with your actual file path
# df = pd.read_excel(file_path)

# # Define the column where you want to remove values
# column_name = 'Volume'  # Change to the desired column

# # Get total rows and calculate 20% of them
# num_rows = len(df)
# num_to_remove = int(num_rows * 0.2)

# # Randomly select indices to remove values
# random_indices = np.random.choice(df.index, num_to_remove, replace=False)

# # Set selected cell values to NaN
# df.loc[random_indices, column_name] = None

# # Save the modified file
# df.to_excel("uncleaned_data.xlsx", index=False)

# print(f"Randomly removed values from {num_to_remove} cells in column {column_name}!")



# #adding catgorial data  import pandas as pd
# import pandas as pd
# import random
# import string

# # Load the Excel file
# file_path = "uncleaned_data.xlsx"  # Replace with your actual file path
# df = pd.read_excel(file_path)

# # Function to generate a random 5-letter string
# def random_string(length=5):
#     return ''.join(random.choices(string.ascii_letters, k=length))  # Random uppercase & lowercase letters

# # Create a new column 'CatD' with random strings
# df['CatD'] = [random_string() for _ in range(len(df))]

# # Save the modified file
# df.to_excel("catg_data.xlsx", index=False)

# print("New column 'CatD' added with random 5-letter values!")



#deleing 20% catgorail data  from CatD column
# import pandas as pd
# import numpy as np

# # Load the Excel file
# file_path = "catg_data.xlsx"  # Replace with your actual file path
# df = pd.read_excel(file_path)

# # Define the column where you want to remove values
# column_name = 'CatD'  # Change to the desired column

# # Get total rows and calculate 20% of them
# num_rows = len(df)
# num_to_remove = int(num_rows * 0.2)

# # Randomly select indices to remove values
# random_indices = np.random.choice(df.index, num_to_remove, replace=False)

# # Set selected cell values to NaN
# df.loc[random_indices, column_name] = None

# # Save the modified file
# df.to_excel("catg_data.xlsx", index=False)

# print(f"Randomly removed values from {num_to_remove} cells in column {column_name}!")


## gender catgorial data generation
# import pandas as pd
# import random
# import string

# def random_name():
#     length = random.randint(5, 10)  # Name length between 5 to 10 characters
#     return ''.join(random.choices("ABCDX", k=length))  # Random combination of 'A', 'B', 'C', 'D', 'X'

# def random_gender():
#     return random.choice(["Male", "Female"])  # Randomly select Male or Female

# def random_married():
#     return random.choice(["Yes", "No"])  # Randomly select Yes or No

# # Generate 1000 records
# data = {
#     "Name": [random_name() for _ in range(1000)],
#     "Gender": [random_gender() for _ in range(1000)],
#     "Married": [random_married() for _ in range(1000)]
# }

# df = pd.DataFrame(data)

# # Save to Excel file
# df.to_excel("gender_cat_data.xlsx", index=False)

# print("Excel file 'gender_cat_data.xlsx' generated successfully!")



# import pandas as pd
# import random

# # Load existing data
# df = pd.read_excel("gender_cat_data.xlsx")

# # Function to generate random locations
# def random_location():
#     countries = ["USA", "Canada", "UK", "Germany", "France", "India", "China", "Brazil", "Australia", "Japan"]
#     return random.choice(countries)

# # Append new 'Location' column
# df["Location"] = [random_location() for _ in range(len(df))]

# # Save updated file
# df.to_excel("gender_cat_data.xlsx", index=False)

# print("Excel file 'gender_cat_data.xlsx' updated successfully with Location column!")








# import pandas as pd
# import numpy as np
# import random

# # Set seed for reproducibility
# random.seed(42)
# np.random.seed(42)

# # Generate 100 students
# num_students = 100

# # Age: between 18 and 30
# ages = np.random.randint(18, 31, num_students)

# # Experience: between 0 and (Age - 18) years (since no one works before 18)
# experiences = [random.randint(0, age - 18) for age in ages]

# # Salary: Base salary + (experience * multiplier) + (random noise)
# # Example: Base = 15,000, multiplier = 3,000
# base_salary = 15000
# salary = [
#     base_salary + (exp * 3000) + np.random.randint(-2000, 2000)
#     for exp in experiences
# ]

# # Create DataFrame
# df = pd.DataFrame({
#     'Age': ages,
#     'Experience': experiences,
#     'Salary': salary
# })

# # Save to CSV
# df.to_csv('student_data.csv', index=False)

# print("CSV file 'student_data.csv' created with 100 rows.")



# import csv
# import random

# # Function to generate CGPA between 6.0 and 10.0 (realistic)
# def generate_cgpa():
#     return round(random.uniform(6.0, 10.0), 2)

# # Function to generate package based on CGPA
# def generate_package(cgpa):
#     # Basic package + bonus based on CGPA to create positive correlation
#     base_package = 3  # Minimum base package in LPA
#     bonus = (cgpa - 6.0) * random.uniform(2, 3.5)  # Correlated bonus
#     return round(base_package + bonus, 2)

# # File name
# filename = "student_placements.csv"

# # Writing CSV
# with open(filename, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["StudentID", "CGPA", "Package(LPA)"])  # Header
    
#     for student_id in range(1, 101):  # 100 students
#         cgpa = generate_cgpa()
#         package = generate_package(cgpa)
#         writer.writerow([student_id, cgpa, package])

# print(f"CSV file '{filename}' generated with 100 entries.")





# import pandas as pd
# import numpy as np
# import random

# # Set random seed for reproducibility
# np.random.seed(42)

# # Number of records
# num_records = 500

# # Generate base fields
# bedrooms = np.random.randint(1, 6, size=num_records)
# bathrooms = np.round(np.random.uniform(1, 4, size=num_records), 1)
# sqft_living = np.random.randint(500, 4000, size=num_records)
# sqft_lot = np.random.randint(1000, 15000, size=num_records)
# floors = np.round(np.random.choice([1, 1.5, 2, 2.5, 3], size=num_records), 1)
# waterfront = np.random.choice([0, 1], size=num_records, p=[0.95, 0.05])
# view = np.random.randint(0, 5, size=num_records)
# condition = np.random.randint(1, 6, size=num_records)
# yr_built = np.random.randint(1900, 2024, size=num_records)

# # Generate sqft_above and sqft_basement from sqft_living
# sqft_above = []
# sqft_basement = []
# for sqft in sqft_living:
#     above = int(sqft * np.random.uniform(0.6, 0.95))
#     sqft_above.append(above)
#     sqft_basement.append(sqft - above)

# # Generate yr_renovated with valid year logic
# yr_renovated = []
# for year in yr_built:
#     if np.random.rand() < 0.2 and (year + 5) <= 2024:
#         yr_renovated.append(random.randint(year + 5, 2024))
#     else:
#         yr_renovated.append(0)

# # Generate synthetic price based on weighted features
# prices = []
# for i in range(num_records):
#     base_price = (
#         sqft_living[i] * 300 +
#         sqft_lot[i] * 2 +
#         bathrooms[i] * 10000 +
#         bedrooms[i] * 5000 +
#         waterfront[i] * 50000 +
#         view[i] * 10000 +
#         condition[i] * 5000
#     )
#     age = 2024 - yr_built[i]
#     price = base_price * (1 - age * 0.002)  # Depreciation over age
#     prices.append(int(price))

# # Create DataFrame
# df = pd.DataFrame({
#     "bedrooms": bedrooms,
#     "bathrooms": bathrooms,
#     "sqft_living": sqft_living,
#     "sqft_lot": sqft_lot,
#     "floors": floors,
#     "waterfront": waterfront,
#     "view": view,
#     "condition": condition,
#     "sqft_above": sqft_above,
#     "sqft_basement": sqft_basement,
#     "yr_built": yr_built,
#     "yr_renovated": yr_renovated,
#     "price": prices
# })

# # Save to CSV
# df.to_csv("house_prices_data.csv", index=False)
# print("✅ CSV file 'house_prices_data.csv' generated with 500 records.")




# import pandas as pd
# import numpy as np
# import random

# np.random.seed(42)

# n = 500

# # Age between 18 and 60
# ages = np.random.randint(18, 61, size=n)

# # Salary based on age (more realistic relationship)
# salaries = []
# for age in ages:
#     if age < 25:
#         salaries.append(np.random.randint(15000, 40000))
#     elif 25 <= age <= 40:
#         salaries.append(np.random.randint(35000, 100000))
#     else:
#         salaries.append(np.random.randint(25000, 80000))

# # Target variable: Purchased
# purchased = []
# for age, salary in zip(ages, salaries):
#     # Good conditions to purchase
#     if 25 <= age <= 40 and salary >= 50000:
#         prob = 0.85
#     elif salary > 80000:
#         prob = 0.75
#     elif age < 23 or salary < 25000:
#         prob = 0.1
#     else:
#         prob = 0.3
#     purchased.append(1 if random.random() < prob else 0)

# # Check balance of 0s and 1s
# print(f"Class 1 Count: {sum(purchased)} / {n}")

# # Create DataFrame
# df = pd.DataFrame({
#     'Age': ages,
#     'EstimatedSalary': salaries,
#     'Purchased': purchased
# })

# # Save to CSV
# df.to_csv("accurate_subscription_data.csv", index=False)
# print("✅ High-quality dataset saved as 'accurate_subscription_data.csv'")


# import pandas as pd
# import numpy as np
# import random

# # Set random seed for reproducibility
# np.random.seed(42)

# # Generate CGPA between 5.0 to 10.0
# cgpa = np.round(np.random.uniform(5.0, 10.0, 500), 2)

# # Generate exam score between 5.0 to 9.0
# score = np.round(np.random.uniform(5.0, 9.0, 500), 2)

# # Define a placement probability function (sigmoid-like behavior)
# def placement_probability(cgpa, score):
#     # These weights can be tweaked based on expected importance
#     weighted_sum = 0.8 * cgpa + 1.2 * score - 12.5  # bias
#     return 1 / (1 + np.exp(-weighted_sum))

# # Generate placement outcome (1 for placed, 0 for not placed)
# placed = [1 if random.random() < placement_probability(c, s) else 0 for c, s in zip(cgpa, score)]

# # Create DataFrame
# df = pd.DataFrame({
#     "cgpa": cgpa,
#     "score": score,
#     "placed": placed
# })

# # Save to CSV
# df.to_csv("student_placement_data.csv", index=False)
# print("✅ student_placement_data.csv generated with 500 entries.")



import pandas as pd
import numpy as np

def generate_flower_data(filename="flowers.csv", samples_per_class=83):
    np.random.seed(42)  # For reproducibility

    def create_samples(mean, std, species, count):
        data = np.random.normal(loc=mean, scale=std, size=(count, 4))
        df = pd.DataFrame(data, columns=[
            'sepal_length', 'sepal_width', 'petal_length', 'petal_width'
        ])
        df['species'] = species
        return df

    # Define typical ranges based on the Iris dataset
    setosa = create_samples(
        mean=[5.0, 3.4, 1.5, 0.2],
        std=[0.3, 0.2, 0.2, 0.1],
        species='setosa',
        count=samples_per_class
    )

    versicolor = create_samples(
        mean=[5.9, 2.8, 4.2, 1.3],
        std=[0.4, 0.3, 0.3, 0.2],
        species='versicolor',
        count=samples_per_class
    )

    virginica = create_samples(
        mean=[6.5, 3.0, 5.5, 2.0],
        std=[0.4, 0.3, 0.4, 0.2],
        species='virginica',
        count=250 - 2 * samples_per_class  # To ensure exactly 250
    )

    df_all = pd.concat([setosa, versicolor, virginica], ignore_index=True)
    df_all = df_all.sample(frac=1, random_state=42).reset_index(drop=True)  # Shuffle
    df_all.to_csv(filename, index=False)

    print(f"✅ {filename} generated with {len(df_all)} rows.")

# Run it
generate_flower_data()

