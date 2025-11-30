import pandas as pd

"""People data"""

people = [
    {
        'name': 'Alina',
        'position': 'Architectural Designer',
        'hourly_rate': 1500,
        'hours_worked': 160,
        'bonus': 20000,
        },
    {
        'name': 'Michael',
        'position': 'Architectural Designer Part 2',
        'hourly_rate': 1800,
        'hours_worked': 10,
        'bonus': 25000,
    },
    {
        'name': 'Polina',
        'position': 'Interior Designer',
        'hourly_rate': 1400,
        'hours_worked': 15,
        'bonus': 10000,
    }
]

df = pd.DataFrame(people)
print("\nDataFrame example:")
print(df)