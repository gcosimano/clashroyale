"""
How to test

import get_data

print(get_data.get_data("data/spells"))

"""

import json

def get_data(file_path):
    """
    Pull JSON data from file and return a dictionary
    """

    try: 
        with open(file_path, 'r') as file:     
            data = json.load(file) 
            return data
        
    except FileNotFoundError: 
        print(f"Error: The file '{file_path}' was not found.") 

    except json.JSONDecodeError as e:   
        print(f"Error: The file '{file_path}' isn’t valid JSON.") 
        print(f"JSONDecodeError: {e}")
        print(f"Error occurred at line: {e.lineno}, column: {e.colno}")
        print(f"Position in string: {e.pos}")
        
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")

    
