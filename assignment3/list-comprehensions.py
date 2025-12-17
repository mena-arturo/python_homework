# -------- Task 3: List Comprehensions Practice --------------------------------------------------------------------
'''
1. Within the assignment3 folder, create a file called list-comprehensions.py.
   Add code that reads the contents of ../csv/employees.csv into a list of lists using the csv module.

2. Using a list comprehension, create a list of the employee names, first_name + space + last_name.
   The list comprehension should iterate through the items in the list read from the csv file.
   Print the resulting list. Skip the item created for the heading of the csv file.

3. Using a list comprehension, create another list from the previous list of names.
   This list should include only those names that contain the letter "e". Print this list.
'''

import assignment2

employees = assignment2.read_employees()

employee_list = [x[1] +"  "+  x[2] for x in employees['rows']]
print ("Employees' name: \n",employee_list,"\n")

employee_list2 = [x for x in employee_list if "e" in x]
print ("Employees with 'e' on their name: \n",employee_list2)
