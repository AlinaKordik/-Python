from application.salary import calculate_salary
from application.db.people import get_employee
from application.db.people_db import people
from datetime import datetime

"""Main file contains all functions"""

print(f'Program generated information at {datetime.now()}')
if __name__ == '__main__':

    while True:
        command = input("Choose your function name: 'salary' or 'employee': ")
        if command == 'salary':
            calculate_salary(people)
            break
        elif command == 'employee':
            get_employee(people)
            break
        else:
            print(f"This '{command}' function does not exist in our system, please choose 'salary' or 'employee'")
            break






