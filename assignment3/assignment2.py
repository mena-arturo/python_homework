import traceback
import csv
import os
from datetime import datetime

# -------- Task 2: Read a CSV File ---------------------------------------------------------------------------------
def read_employees():
    
    csv_file_path="../csv/employees.csv"
    data = {}
    rows = []
    # Using try-except to catch a possible error and avoid
    # the program to crash abruptly
    try:
        with open(csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            #get the first row of the file (the one that contains the headers)  and put it in the dictionary
            data['fields']=next(reader)
            # get the rest of the rows and put them in a list
            for row in reader:
                rows.append(row)
            #insert the list into the dictionary
            data['rows']=rows
        #return the dictionary and we are all set
        return data
    #handle a possible exception
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
