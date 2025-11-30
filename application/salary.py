from application.db.people_db import people

"""Function for calculating salary"""

def calculate_salary(self, bonus=0):
    for person in people:
        total_salary = person['hourly_rate'] * person['hours_worked'] + person['bonus']
        print(f"Заработная плата у {person['name']}: {total_salary} рублей")

