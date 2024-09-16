import numpy as np
import pandas as pd
import re
from matplotlib import pyplot as plt

def _extract_salary_(salary_str):
	salary_range = re.findall(r'\$([\d]+K)', salary_str)
	salary_range = [int(s.replace('K', '')) * 1000 for s in salary_range]
	salary_type = 'Employer est.' if 'Employer est.' in salary_str else 'Glassdoor est.'

	return ((sum(salary_range) / 2), salary_type) if len(salary_range) == 2 else (0, salary_type)


def average_salary_by_company(df):
	df['Salary'] = df['Salary'].astype(str)
	df[['Average Salary', 'Estimate Type']] = df['Salary'].apply(
		lambda x: pd.Series(_extract_salary_(x))
	)
	data = df.sort_values(by = 'Average Salary', ascending=False).head(50)
	data.plot(kind = 'bar', x = 'Company', y = 'Average Salary')
	plt.show()


def rating_by_company(df):
	data = df.sort_values(by = 'Company Score', ascending = False).head(50)
	data.plot(kind = 'bar', x = 'Company', y = 'Company Score')
	plt.show()
    

def job_title_frequency(df):
	data = df['Job Title'].value_counts().head(50)
	data.plot(kind = 'bar', x = 'Job Title', y = 'Frequency')
	plt.show()


def average_salary_by_location(df):
	data = df['Location'].value_counts()
	print(data.head(50))