import numpy as np
import pandas as pd
from io import StringIO

#sales_data = pd.read_csv("data/AusApparalSales4thQrt2020.csv")
#sales_data.dropna()


employee_data = [
    {"id": 1, "name": "Alice Smith", "position": "Sales Manager", "salary": 75000},
    {"id": 2, "name": "Bob Johnson", "position": "Software Engineer", "salary": 85000},
    {"id": 3, "name": "Charlie Brown", "position": "Data Analyst", "salary": 65000},
    {"id": 4, "name": "Diana Prince", "position": "Marketing Specialist", "salary": 60000},
    {"id": 5, "name": "Ethan Hunt", "salary": 70000},
    {"id": 6, "name": "Fiona Gallagher", "position": "UX Designer", "salary": 70000},
    {"id": 7, "name": "George Clooney", "position": "Sales Associate", "salary": 55000},
    {"id": 8, "name": "Hannah Montana", "position": "HR Manager", "salary": 80000},
    {"id": 9, "name": "Ian Malcolm", "position": "Business Analyst", "salary": 72000},
    {"id": 10, "name": "Julia Roberts", "position": "Customer Support", "salary": 48000},
]


employee_df = pd.DataFrame(employee_data).set_index(['id'])

# The optimized line directly uses np.where to fill the 'position' column without creating a separate Series.
# This reduces overhead and improves performance by eliminating the need for index alignment.
employee_df['position'] = employee_df['position'].fillna(
    #employee_df['salary'].apply(lambda salary: 'Software Engineer' if salary >= 80000 else 'Sales Manager')
    pd.Series(np.where(employee_df['salary'] >= 80000, 'Software Engineer', 'Sales Manager'), index=employee_df.index)
)

print(employee_df)

#employee_df.dropna(axis=0, inplace=True)
#print(employee_df.iloc[0:5, 0:2])



# The following code uses np.where to select elements from two arrays based on a condition.
# It checks a 2D boolean array ([[True, False], [True, True]]) to determine which elements to choose.
# If the condition is True, it takes the corresponding element from the second array ([[1, 2], [3, 4]]);
# if False, it takes the element from the third array ([[9, 8], [7, 6]]).
# The result will be a new array where each position is filled based on the condition.
'''print(np.where([[True, False], [True, True]],
       [[1, 2], [3, 4]],
       [[9, 8], [7, 6]])
)'''