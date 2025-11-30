from application.db.people_db import people

"""Function for getting people information from provided data"""

def get_employee(self, name=None, position=None):
    for employee in people:
        print(f"{employee['name']} is {employee['position']} has {employee['hourly_rate']} hourly rate. If you would like to know total salary for each employee please choose 'salary' function.")


