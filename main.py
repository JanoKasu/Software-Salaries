import functions
import pandas as pd

def main():
	df = pd.read_csv('Salaries.csv')
	exit = False
	while not exit:
		print()
		print('0. Exit')
		print('1. Average Salary By Company')
		print('2. Rating By Company')
		print('3. Job Title Frequency')
		print('4. Give Location Info')

		x = int(input('Input: '))

		if x == 0:
			exit = True
		elif x == 1:
			functions.average_salary_by_company(df)
		elif x == 2:
			functions.rating_by_company(df)
		elif x == 3:
			functions.job_title_frequency(df)
		elif x == 4:
			functions.average_salary_by_location(df)
		else:
			print(x)


if __name__ == '__main__':
	main()