#As with the previous lessons, you will run unit tests on the assignment pytest -v -x assignment4-test.py.

# -------- Task 1: Introduction to Pandas - Creating and Manipulating DataFrames -----------------------------------
'''
Create a DataFrame from a dictionary:

Use a dictionary containing the following data:
Name: ['Alice', 'Bob', 'Charlie']
Age: [25, 30, 35]
City: ['New York', 'Los Angeles', 'Chicago']
Convert the dictionary into a DataFrame using Pandas.
Print the DataFrame to verify its creation.
save the DataFrame in a variable called task1_data_frame and run the tests.

Add a new column:

Make a copy of the dataFrame you created named task1_with_salary (use the copy() method)
Add a column called Salary with values [70000, 80000, 90000].
Print the new DataFrame and run the tests.

Modify an existing column:

Make a copy of task1_with_salary in a variable named task1_older
Increment the Age column by 1 for each entry.
Print the modified DataFrame to verify the changes and run the tests.

Save the DataFrame as a CSV file:

Save the task1_older DataFrame to a file named employees.csv using to_csv(), do not include an index in
the csv file.
Look at the contents of the CSV file to see how it's formatted.
Run the tests.

'''
import pandas as pd
import string

#Create a data frame from a Dictionary
my_dict ={'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
task1_data_frame = pd.DataFrame(my_dict)

#Add a Column
task1_with_salary=  task1_data_frame.copy()
task1_with_salary['Salary']=[70000, 80000, 90000]
print("Different layers:")
print(f"Whole data frame: task1_with_salary:\n{task1_with_salary}")
print(f"Column (behave like a dictionary) task1_with_salary['City']:\n{task1_with_salary['City']}")
print(f"Row (behave like a series) task1_with_salary['City'][2]:\n{task1_with_salary['City'][2]}")

#Modify an existing column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'].copy() +1
print(f"This is task1_older data frame updated:\n{task1_older}")


#Save the DataFrame as a CSV file
task1_older.to_csv("employees.csv", index=False)

# -------- Task 2: Loading Data from CSV and JSON ------------------------------------------------------------------
'''

Read data from a CSV file:

Load the CSV file from Task 1 into a new DataFrame saved to a variable task2_employees.
Print it and run the tests to verify the contents.

Read data from a JSON file:

Create a JSON file (additional_employees.json). The file adds two new employees. Eve, who is 28, lives in Miami,
and has a salary of 60000, and Frank, who is 40, lives in Seattle, and has a salary of 95000.
Load this JSON file into a new DataFrame and assign it to the variable json_employees.
Print the DataFrame to verify it loaded correctly and run the tests.
Combine DataFrames:

Combine the data from the JSON file into the DataFrame Loaded from the CSV file and save it in the variable
more_employees.

Print the combined Dataframe and run the tests.
'''

#Read data from a CSV file
task2_employees = pd.read_csv('employees.csv')
print(f"This is task2_employees with uploaded data from csv file:\n{task2_employees}")

#Read data from a JSON file
json_employees = pd.read_json('additional_employees.json')
print(f"This is json_employees:\n{json_employees}")

# Combine the data frames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(f"This is more_employes:\n{more_employees}")



# -------- Task 3: Data Inspection - Using Head, Tail, and Info Methods --------------------------------------------
'''
Use the head() method:
Assign the first three rows of the more_employees DataFrame to the variable first_three
Print the variable and run the tests.

Use the tail() method:
Assign the last two rows of the more_employees DataFrame to the variable last_two
Print the variable and run the tests.

Get the shape of a DataFrame:
Assign the shape of the more_employees DataFrame to the variable employee_shape
Print the variable and run the tests

Use the info() method:
Print a concise summary of the DataFrame using the info() method to understand the data types and non-null counts.
'''

# Using the head method
first_three = more_employees.head(3)
print(f"This are the first three rows from more_employees data frame:\n{first_three}")

# Using the tail method
last_two = more_employees.tail(2)
print(f"This are the last two rows from more_employees data frame:\n{last_two}")

#Get the shape of a Data Frame
employee_shape = more_employees.shape
print(f"This is the shape of more_employees:\n{employee_shape}\n\n")

#Using the info() method
print(f"This is the summary of more_employees data frame:\n")
more_employees.info()



# -------- Task 4: Data Cleaning -----------------------------------------------------------------------------------
'''
Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
Print it and run the tests.

Create a copy of the dirty data in the varialble clean_data (use the copy() method). You will use data cleaning
methods to update clean_data.
Remove any duplicate rows from the DataFrame
Print it and run the tests.

Convert Age to numeric and handle missing values
Print it and run the tests.

Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
print it and run the tests.

Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
Print it and run the tests

Convert Hire Date to datetime
Print it and run the tests

Strip extra whitespace and standardize Name and Department as uppercase
Print it and run the tests
'''

#Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
dirty_data = pd.read_csv('dirty_data.csv')
print(f"This is the dirty_data data frame:\n{dirty_data}")

#Create a copy of the dirty data in the varialble clean_data (use the copy() method).
#You will use data cleaning methods to update clean_data.
#Remove any duplicate rows from the DataFrame
clean_data = dirty_data.copy()
duplicates = dirty_data[dirty_data.duplicated()]
print(f"This is the duplicates data frame:\n{duplicates}")
clean_data = clean_data.drop_duplicates()
print(f"This is clean_data without duplicates:\n{clean_data}")

#Convert Age to numeric and handle missing values
print("\nAfter conversion to numeric:")
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors ="coerce")
print(f"This is clean_data with Age converted to numeric:\n{clean_data}")

#Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data['Salary'] = clean_data['Salary'].replace("unknown", pd.NA)
clean_data['Salary'] = clean_data['Salary'].replace("n/a", pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors ="coerce")
print(f"This is clean_data with numbers and known place holders replaced:\n{clean_data}")

#Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
mean_age = clean_data['Age'].mean()
clean_data['Age'] = clean_data['Age'].fillna(mean_age) 
median_salary = clean_data['Salary'].median()
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)
print(f"This is clean_data with missing Salary numeric values filled with the median:\n{clean_data}")

#Convert Hire Date to datetime
clean_data['Hire Date']=pd.to_datetime(clean_data['Hire Date'], format="mixed")
print(f"This is clean_data with Hire Date formated to datetime:\n{clean_data}")

#Strip extra whitespace and standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip()
clean_data['Name'] = clean_data['Name'].str.upper()
clean_data['Department'] = clean_data['Department'].str.upper()
print(f"This is clean_data with Name and Department striped and formated to uppercase:\n{clean_data}")
