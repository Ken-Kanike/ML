# Creating unclean data for practice ( make a copy of original data) 

#deleting 50% values from Open col 
# import pandas as pd

# # Load the Excel file
# file_path = "C:/Users/junai/Desktop/coding/ML/yahoo_data.xlsx"  # Replace with your actual file path
# df = pd.read_excel(file_path)

# # Remove values in odd-numbered rows (keeping even rows)
# df.loc[df.index % 2 == 0, 'Open'] = None  # Use df.index % 2 == 0 because Python uses 0-based indexing

# # Save the modified file
# df.to_excel("C:/Users/junai/Desktop/coding/ML/uncleaned_data.xlsx", index=False)

# print("Values from odd rows in Column B have been deleted successfully!")

#deleing 20% values from Volume column
# import pandas as pd
# import numpy as np

# # Load the Excel file
# file_path = "C:/Users/junai/Desktop/coding/ML/uncleaned_data.xlsx"  # Replace with your actual file path
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
# df.to_excel("C:/Users/junai/Desktop/coding/ML/uncleaned_data.xlsx", index=False)

# print(f"Randomly removed values from {num_to_remove} cells in column {column_name}!")



# #adding catgorial data  import pandas as pd
# import pandas as pd
# import random
# import string

# # Load the Excel file
# file_path = "C:/Users/junai/Desktop/coding/ML/uncleaned_data.xlsx"  # Replace with your actual file path
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
# file_path = "C:/Users/junai/Desktop/coding/ML/catg_data.xlsx"  # Replace with your actual file path
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
# df.to_excel("C:/Users/junai/Desktop/coding/ML/catg_data.xlsx", index=False)

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


