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
