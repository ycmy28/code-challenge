import pandas as pd
import numpy as np
pd.set_option('display.float_format', lambda x: '%.2f' % x)

#read employees data
dtypes_employees = {'employe_id': int, 'branch_id': int, 'salary': int} #, 'join_date': str, 'resign_date': str}
#parse_dates_employees = ['join_date', 'resign_date']
employees = pd.read_csv('employees.csv', dtype=dtypes_employees, usecols=['employe_id', 'branch_id', 'salary']) #parse_dates=parse_dates_employees,

#read timesheets data
dtypes_timesheets = {'timesheet_id': int, 'employee_id': int, 'date': str, 'checkin': str, 'checkout': str}
parse_dates_timesheets = ['date', 'checkin', 'checkout']
timesheets = pd.read_csv('timesheets.csv', dtype=dtypes_timesheets, parse_dates=parse_dates_timesheets)

employees = employees.drop_duplicates(subset=['employe_id'], keep='last')
timesheets.dropna(subset=['checkout'],inplace=True)

timesheets['working_hours'] = (timesheets.checkout - timesheets.checkin).astype('timedelta64[h]')
merge_df = employees.merge(timesheets, left_on=['employe_id'], right_on=['employee_id'], how='left')

def add_salary_per_hour(df):
    df['date'] = df['date'].dt.to_period('M')
    df_added_field = df.groupby(['date','branch_id'], as_index=False)[["salary", "working_hours"]].sum()
    df_added_field['year'] = df_added_field['date'].dt.year
    df_added_field['month'] = df_added_field['date'].dt.month
    df_added_field['salary_per_hour'] = df_added_field['salary']/df_added_field['working_hours']
    final = df_added_field[['year', 'month', 'branch_id', 'salary_per_hour']].sort_values(by=['year', 'month', 'branch_id'])
    return final

salary_per_hour = add_salary_per_hour(merge_df)
salary_per_hour.append(final, ignore_index = True)






